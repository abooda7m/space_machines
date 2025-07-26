# tabs/numerical_analysis.py
import streamlit as st
import plotly.express as px
import pandas as pd

def render(df):
    st.header("📈 Numerical Analysis")

    # -------------------------------------------------------
    # 1. Summary Table of Numerical Columns (excluding datetime)
    # -------------------------------------------------------
    st.subheader("📋 Summary of Numerical Columns")
    numeric_df = df.select_dtypes(include=['number'])
    st.dataframe(numeric_df.describe().round(2), use_container_width=True)
    
    
    # -------------------------------------------------------
    # 2. Avg Mission Cost by Payload Weight Group (Binned Bar Chart)
    # -------------------------------------------------------
    st.subheader("📦 Avg Mission Cost by Payload Weight Group")

    # Create bins for Payload Weight (e.g., every 10 tons)
    df["Payload Bin"] = pd.cut(df["Payload Weight (tons)"], bins=range(0, 110, 10))

    # Group by bin and calculate average Mission Cost
    avg_cost_by_bin = df.groupby("Payload Bin")["Mission Cost (billion USD)"].mean().reset_index()
    avg_cost_by_bin["Payload Bin"] = avg_cost_by_bin["Payload Bin"].astype(str)

    # Create a cleaner bar chart
    fig3 = px.bar(
        avg_cost_by_bin,
        x="Payload Bin",
        y="Mission Cost (billion USD)",
        title="Avg Mission Cost by Payload Weight Group",
        labels={
            "Payload Bin": "Payload Weight Range (tons)",
            "Mission Cost (billion USD)": "Avg Cost (Billion USD)"
        }
    )

    # Customize layout
    fig3.update_layout(
        xaxis_title="Payload Weight Range (tons)",
        yaxis_title="Avg Cost (Billion USD)",
        yaxis_tickformat="$,.2f",
        bargap=0.2
    )

    # Display chart
    st.plotly_chart(fig3, use_container_width=True)


    # -------------------------------------------------------
    # 4. Mission Success Rate by Budget Category (Sorted Desc)
    # -------------------------------------------------------
    st.subheader("📊 Mission Success Rate by Budget Category")
    df_budget_grouped = df.groupby("Budget Category")["Mission Success (%)"].mean().reset_index()
    df_budget_grouped = df_budget_grouped.sort_values("Mission Success (%)", ascending=False)

    fig4 = px.bar(
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
    fig4.update_layout(
        xaxis_title="Budget Category",
        yaxis_title="Success (%)",
        showlegend=False
    )
    st.plotly_chart(fig4, use_container_width=True)
    
  

    # -------------------------------------------------------
    # 5. Avg Scientific Yield vs Mission Duration (Rounded)
    # -------------------------------------------------------
    st.subheader("📊 Avg Scientific Yield vs Mission Duration (Rounded)")
    df["Duration Year"] = df["Mission Duration (years)"].round()
    avg_yield_by_duration = df.groupby("Duration Year")["Scientific Yield (points)"].mean().reset_index()

    fig5 = px.line(
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
    fig5.update_traces(
        text=avg_yield_by_duration["Scientific Yield (points)"].round(1),
        textposition="top center"
    )
    st.plotly_chart(fig5, use_container_width=True)
    st.caption("Scientific yield shows fluctuations across different mission durations without a clear upward or downward trend.")


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



    # -------------------------------------------------------
    # 8. Fuel Consumption vs Distance from Earth (Line Chart)
    # -------------------------------------------------------
    
    st.subheader("⛽ Fuel Consumption vs Distance from Earth (Line Chart)")
    
    # Sort the DataFrame by distance to ensure a smooth line plot
    df_sorted = df.sort_values("Distance from Earth (light-years)")
    
    # Create a line chart to show the relationship between distance and fuel consumption
    fig8 = px.line(
        df_sorted,
        x="Distance from Earth (light-years)",
        y="Fuel Consumption (tons)",
        title="Fuel Consumption vs Distance from Earth (Line Chart)",
        labels={
            "Distance from Earth (light-years)": "Distance from Earth (light-years)",
            "Fuel Consumption (tons)": "Fuel Consumption (tons)"
        }
    )
    
    # Update axis labels for better readability
    fig8.update_layout(
        xaxis_title="Distance from Earth (light-years)",
        yaxis_title="Fuel Consumption (tons)"
    )
    
    # Display the line chart in the Streamlit app
    st.plotly_chart(fig8, use_container_width=True)
    st.caption("Fuel consumption increases as mission distance from Earth increases.")

    