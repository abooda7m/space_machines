# tabs/numerical_analysis.py

import streamlit as st
import plotly.express as px

def render(df):
    st.header("📈 Numerical Analysis")

    # -------------------------------------------------------
    # 1. Summary Table of Numerical Columns (excluding datetime)
    # -------------------------------------------------------
    st.subheader("📋 Summary of Numerical Columns")
    numeric_df = df.select_dtypes(include=['number'])
    st.dataframe(numeric_df.describe().round(2), use_container_width=True)
    
    
    # -------------------------------------------------------
    # 2. Average Mission Cost per Year
    # -------------------------------------------------------
    st.subheader("💸 Average Mission Cost per Year")
    df_sorted = df.sort_values("Launch Date")
    df_sorted["Launch Year"] = df_sorted["Launch Date"].dt.year
    avg_cost_per_year = df_sorted.groupby("Launch Year")["Mission Cost (billion USD)"].mean().reset_index()

    fig2 = px.line(
        avg_cost_per_year,
        x="Launch Year",
        y="Mission Cost (billion USD)",
        markers=True,
        title="Avg. Mission Cost per Year",
        labels={"Mission Cost (billion USD)": "Avg Cost (Billion USD)"}
    )
    fig2.update_layout(
        xaxis_title="Year",
        yaxis_title="Avg Cost (Billion USD)",
        yaxis_tickformat="$,.2f"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # -------------------------------------------------------
    # 3. Mission Cost vs Payload Weight (Bar Chart)
    # -------------------------------------------------------
    st.subheader("📦 Relationship Between Mission Cost and Payload Weight")
    fig6 = px.bar(
        df,
        x="Payload Weight (tons)",
        y="Mission Cost (billion USD)",
        title="Relationship Between Mission Cost and Payload Weight",
        labels={
            "Payload Weight (tons)": "Payload Weight (tons)",
            "Mission Cost (billion USD)": "Mission Cost (Billion USD)"
        }
    )
    fig6.update_layout(
        xaxis_title="Payload Weight (tons)",
        yaxis_title="Mission Cost (Billion USD)",
        yaxis_tickformat="$,.2f",
        bargap=0.2
    )
    st.plotly_chart(fig6, use_container_width=True)

    # -------------------------------------------------------
    # 4. Mission Success Rate by Budget Category (Sorted Desc)
    # -------------------------------------------------------
    st.subheader("📊 Mission Success Rate by Budget Category")
    df_budget_grouped = df.groupby("Budget Category")["Mission Success (%)"].mean().reset_index()
    df_budget_grouped = df_budget_grouped.sort_values("Mission Success (%)", ascending=False)

    fig3 = px.bar(
        df_budget_grouped,
        x="Budget Category",
        y="Mission Success (%)",
        color="Budget Category",
        title="Avg Mission Success Rate by Budget Category",
        labels={
            "Budget Category": "Budget Category",
            "Mission Success (%)": "Avg Success Rate (%)"
        }
    )
    fig3.update_layout(
        xaxis_title="Budget Category",
        yaxis_title="Success (%)",
        showlegend=False
    )
    st.plotly_chart(fig3, use_container_width=True)

    # -------------------------------------------------------
    # 5. Avg Scientific Yield vs Mission Duration (Rounded)
    # -------------------------------------------------------
    st.subheader("📊 Avg Scientific Yield vs Mission Duration (Rounded)")
    df["Duration Year"] = df["Mission Duration (years)"].round()
    avg_yield_by_duration = df.groupby("Duration Year")["Scientific Yield (points)"].mean().reset_index()

    fig4 = px.line(
        avg_yield_by_duration,
        x="Duration Year",
        y="Scientific Yield (points)",
        markers=True,
        title="Avg Scientific Yield vs Mission Duration",
        labels={
            "Duration Year": "Mission Duration (rounded years)",
            "Scientific Yield (points)": "Avg Scientific Yield"
        }
    )
    fig4.update_traces(
        text=avg_yield_by_duration["Scientific Yield (points)"].round(1),
        textposition="top center"
    )
    st.plotly_chart(fig4, use_container_width=True)

    # -------------------------------------------------------
    # 6. Avg Mission Success vs Crew Size Group
    # -------------------------------------------------------
    st.subheader("🧑‍🚀 Avg Mission Success vs Crew Size Group")
    df["Crew Group"] = (df["Crew Size"] // 10) * 10
    avg_success_by_crew = df.groupby("Crew Group")["Mission Success (%)"].mean().reset_index()

    fig5 = px.line(
        avg_success_by_crew,
        x="Crew Group",
        y="Mission Success (%)",
        markers=True,
        title="Avg Mission Success vs Crew Size Group",
        labels={
            "Crew Group": "Crew Size Group",
            "Mission Success (%)": "Avg Success (%)"
        }
    )
    fig5.update_traces(
        text=avg_success_by_crew["Mission Success (%)"].round(1),
        textposition="top center"
    )
    st.plotly_chart(fig5, use_container_width=True)

    # -------------------------------------------------------
    # 7. Mission Duration vs Distance from Earth (Regression)
    # -------------------------------------------------------
    st.subheader("🪐 Mission Duration vs Distance from Earth")
    fig7 = px.scatter(
        df,
        x="Distance from Earth (light-years)",
        y="Mission Duration (years)",
        color="Mission Success (%)",
        color_continuous_scale="viridis",
        opacity=0.7,
        trendline="ols",
        title="Mission Duration vs Distance from Earth (with Regression Line)",
        labels={
            "Distance from Earth (light-years)": "Distance from Earth (light-years)",
            "Mission Duration (years)": "Mission Duration (years)",
            "Mission Success (%)": "Mission Success (%)"
        }
    )
    fig7.update_layout(
        xaxis_title="Distance from Earth (light-years)",
        yaxis_title="Mission Duration (years)"
    )
    st.plotly_chart(fig7, use_container_width=True)
