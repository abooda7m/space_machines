# tabs/categorical_analysis.py

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from babel.numbers import format_decimal

    

    # Fancy card component
def fancy_card(title: str, value: str, color: str = "#112841"):
    st.markdown(f"""
        <div style="background-color: {color}; padding: 15px; border-radius: 16px; 
                    text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.25); 
                    border: 1px solid #33475b; margin-bottom: 12px;">
            <h3 style="margin: 0; color: #ffffff; font-weight: 600;">{title}</h3>
            <h5 style="margin: 0; color: #5fa8d3;">{value}</h5>
        </div>
    """, unsafe_allow_html=True)
    

# Render function
def render(df):
    st.header("📊 Categorical Analysis")

    #  Launch Vehicles Overview (Fancy Cards)
    st.subheader(" Launch Vehicles Overview")
    launch_counts = df["Launch Vehicle"].value_counts().reset_index()
    launch_counts.columns = ["Launch Vehicle", "Count"]
    cols = st.columns(min(4, len(launch_counts)))
    for idx, row in launch_counts.iterrows():
        with cols[idx % 4]:
            fancy_card(row["Launch Vehicle"], f"{row['Count']} Missions")

    #  Mission Types Overview (Fancy Cards)
    st.subheader(" Mission Types Overview")
    mission_counts = df["Mission Type"].value_counts().reset_index()
    mission_counts.columns = ["Mission Type", "Count"]
    cols2 = st.columns(min(4, len(mission_counts)))
    for idx, row in mission_counts.iterrows():
        with cols2[idx % 4]:
            fancy_card(row["Mission Type"], f"{row['Count']} Missions")

    st.markdown("---")

    # 📊 Mission Success & Failure Rates (Indicators)
    st.subheader("📊 Mission Success & Failure Rates")
    success_rate = df["Mission Success (%)"].mean()
    failure_rate = 100 - success_rate

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        fig_success = go.Figure(go.Indicator(
            mode="gauge+number",
            value=success_rate,
            number={"suffix": "%", "font": {"size": 36, "color": "green"}},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "bgcolor": "white",
                "borderwidth": 2,
                "bordercolor": "gray"
            },
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "✅ Success Rate", "font": {"size": 18}}
        ))
        fig_success.update_layout(height=250, margin=dict(t=30, b=0))
        st.plotly_chart(fig_success, use_container_width=True)

    with col2:
        fig_failure = go.Figure(go.Indicator(
            mode="gauge+number",
            value=failure_rate,
            number={"suffix": "%", "font": {"size": 36, "color": "red"}},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "red"},
                "bgcolor": "white",
                "borderwidth": 2,
                "bordercolor": "gray"
            },
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "❌ Failure Rate", "font": {"size": 18}}
        ))
        fig_failure.update_layout(height=250, margin=dict(t=30, b=0))
        st.plotly_chart(fig_failure, use_container_width=True)

    with col3:
        total_cost = df["Mission Cost (billion USD)"].sum()
        formatted_cost = f"${format_decimal(total_cost, format='#,##0.00')} Billion"
        st.markdown(
            f"""
            <div style="background-color:#79bbe2; padding:25px; border-radius:10px; text-align:center;">
                <h5 style="margin-bottom:10px;">💰 Total Mission Cost</h5>
                <p style="font-size:24px; font-weight:bold; color:#333;">{formatted_cost}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -------------------------------------------------------
    # 1. Mission Types Over the Years
    # -------------------------------------------------------
    st.subheader("📅 Missions by Type Over the Years")
    missions_by_type = df.groupby(["Launch Year", "Mission Type"]).size().reset_index(name="Count")
    missions_by_type = missions_by_type.sort_values("Count", ascending=False)
    fig3 = px.bar(
        missions_by_type,
        x="Launch Year",
        y="Count",
        color="Mission Type",
        title="Mission Types per Year",
        labels={"Count": "Number of Missions"},
      
    )
    st.plotly_chart(fig3, use_container_width=True)

    # -------------------------------------------------------
    # 2. Avg. Success Rate per Mission Type
    # -------------------------------------------------------
    st.subheader("✅ Avg. Success Rate per Mission Type")
    if "Mission Type" in df.columns and "Mission Success (%)" in df.columns:
        success_by_type = df.groupby("Mission Type")["Mission Success (%)"].mean().sort_values(ascending=False)
        fig4 = px.bar(
            x=success_by_type.index,
            y=success_by_type.values,
            labels={"x": "Mission Type", "y": "Avg. Success (%)"},
            title="Success Rate by Mission Type"
        )
        st.plotly_chart(fig4, use_container_width=True)
        
    # -------------------------------------------------------
    # 3. Distribution of Missions by Target Type (Pie)
    # -------------------------------------------------------
    st.subheader("🧭 Distribution of Missions by Target Type")
    pie_counts = df['Target Type'].value_counts().sort_values(ascending=False).reset_index()
    pie_counts.columns = ['Target Type', 'Count']

    fig5 = px.pie(
        pie_counts,
        values='Count',
        names='Target Type',
        title='Insight: Distribution of Missions by Target Type',
        hole=0.3
    )
    st.plotly_chart(fig5, use_container_width=True)




