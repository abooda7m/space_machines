# tabs/analysis.py

import streamlit as st
import plotly.express as px

def render(df):
    st.header("🌍 Mission Analysis")

    # Count missions by Target Type
    st.subheader("🔭 Missions by Target Type")
    target_counts = df["Target Type"].value_counts().nlargest(10)
    fig1 = px.bar(
        target_counts,
        x=target_counts.index,
        y=target_counts.values,
        labels={"x": "Target Type", "y": "Number of Missions"},
        title="Top Target Types"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Count missions by Launch Vehicle
    st.subheader("🚀 Most Used Launch Vehicles")
    vehicle_counts = df["Launch Vehicle"].value_counts().nlargest(10)
    fig2 = px.bar(
        vehicle_counts,
        x=vehicle_counts.index,
        y=vehicle_counts.values,
        labels={"x": "Launch Vehicle", "y": "Number of Missions"},
        title="Top 10 Launch Vehicles"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Average Success Rate by Mission Type
    if "Mission Type" in df.columns and "Mission Success (%)" in df.columns:
        st.subheader("✅ Average Success Rate per Mission Type")
        success_by_type = df.groupby("Mission Type")["Mission Success (%)"].mean().sort_values(ascending=False)
        fig3 = px.bar(
            success_by_type,
            x=success_by_type.index,
            y=success_by_type.values,
            labels={"x": "Mission Type", "y": "Avg. Success (%)"},
            title="Success Rate by Mission Type"
        )
        st.plotly_chart(fig3, use_container_width=True)

    st.subheader("🚀 Missions by Type Over the Years")
    missions_by_type = df.groupby(["Launch Year", "Mission Type"]).size().reset_index(name="Count")
    fig = px.bar(
        missions_by_type,
        x="Launch Year",
        y="Count",
        color="Mission Type",
        title="Mission Types per Year",
        labels={"Count": "Number of Missions"},
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("🧭 Unique Mission Types:")
    st.write(df["Mission Type"].unique())
    st.write("🔢 Total Mission Types:", df["Mission Type"].nunique())

