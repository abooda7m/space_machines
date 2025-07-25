import streamlit as st
import pandas as pd

def render(df):
    st.header("📡 Mission Data Overview")

    # --- About the Dataset ---
    st.markdown("""
    ### 🌌 About the Dataset

    This dataset presents a **realistic simulation** of global space missions, including numerical and categorical data on mission characteristics, costs, outcomes, and targets.

    It is ideal for:
    - Exploratory Data Analysis (EDA)
    - Building dashboards and visual reports
    - Educational and ML experimentation

    You'll be able to explore:
    - Mission types and target destinations
    - Trends in cost, crew size, and success rate
    - Scientific yield across different durations
    - Fuel efficiency vs. distance and payload
    ---
    """)

    # --- Sample Data ---
    st.subheader("📋 Sample of the Data")
    st.dataframe(df.head(10), use_container_width=True)

    # --- Dataset Shape Info ---
    st.markdown(f"""
    **📐 Dataset Shape:** `{df.shape[0]} rows × {df.shape[1]} columns`
    """)

    # --- Variable Roles ---
    columns_info = [
        {"Column": "Rocket_Cost", "Role": "Dependent", "Depends_On": "Mission_Duration, Payload_Mass, Launch_Date"},
        {"Column": "Mission_Status", "Role": "Dependent", "Depends_On": "Organisation, Mission_Type, Rocket, Rocket_Cost"},
        {"Column": "Organisation", "Role": "Independent", "Depends_On": "-"},
        {"Column": "Mission_Type", "Role": "Independent", "Depends_On": "-"},
        {"Column": "Rocket", "Role": "Independent", "Depends_On": "-"},
        {"Column": "Country", "Role": "Independent", "Depends_On": "-"},
        {"Column": "Payload_Mass", "Role": "Independent", "Depends_On": "-"},
        {"Column": "Mission_Duration", "Role": "Independent", "Depends_On": "-"},
        {"Column": "Launch_Date", "Role": "Independent", "Depends_On": "-"},
    ]
    columns_df = pd.DataFrame(columns_info)

    # Split into dependent and independent
    dependent_vars = columns_df[columns_df["Role"] == "Dependent"]
    independent_vars = columns_df[columns_df["Role"] == "Independent"]

    # --- Display Dependent Variables ---
    st.subheader("🧮 Dependent Variables")
    st.dataframe(dependent_vars, use_container_width=True)
    st.caption("These variables are influenced by one or more independent features.")

    # --- Display Independent Variables ---
    st.subheader("🎯 Independent Variables")
    st.dataframe(independent_vars, use_container_width=True)
    st.caption("These variables serve as inputs or predictors for modeling.")
