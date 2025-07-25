# tabs/categorical_analysis.py

import streamlit as st
import plotly.express as px

def render(df):
    st.header("📊 Categorical Analysis")

    # 1. Missions by Target Type (Bar)
    st.subheader("🔭 Missions by Target Type")
    target_counts = df["Target Type"].value_counts().sort_values(ascending=False).nlargest(10)
    fig1 = px.bar(
        x=target_counts.index,
        y=target_counts.values,
        labels={"x": "Target Type", "y": "Number of Missions"},
        title="Top Target Types"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Most Used Launch Vehicles
    st.subheader("🚀 Most Used Launch Vehicles")
    vehicle_counts = df["Launch Vehicle"].value_counts().sort_values(ascending=False).nlargest(10)
    fig2 = px.bar(
        x=vehicle_counts.index,
        y=vehicle_counts.values,
        labels={"x": "Launch Vehicle", "y": "Number of Missions"},
        title="Top 10 Launch Vehicles"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # 3. Mission Types Over the Years
    st.subheader("📅 Missions by Type Over the Years")
    missions_by_type = df.groupby(["Launch Year", "Mission Type"]).size().reset_index(name="Count")
    missions_by_type = missions_by_type.sort_values("Count", ascending=False)
    fig3 = px.bar(
        missions_by_type,
        x="Launch Year",
        y="Count",
        color="Mission Type",
        title="Mission Types per Year",
        labels={"Count": "Number of Missions"}
    )
    st.plotly_chart(fig3, use_container_width=True)

    # 4. Avg. Success Rate per Mission Type
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

    # 5. Distribution of Missions by Target Type (Pie)
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
