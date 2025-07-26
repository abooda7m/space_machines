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
       {"Column": "Mission ID", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Mission Name", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Launch Date", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Target Type", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Target Name", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Mission Type", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Distance from Earth (light-years)", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Mission Duration (years)", "Role": "Dependent", "Depends_On": "Distance from Earth (light-years), Mission Type"},
       {"Column": "Mission Cost (billion USD)", "Role": "Dependent", "Depends_On": "Mission Duration, Payload Weight, Mission Type, Launch Date, Crew Size"},
       {"Column": "Scientific Yield (points)", "Role": "Dependent", "Depends_On": "Mission Duration, Mission Type"},
       {"Column": "Crew Size", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Mission Success (%)", "Role": "Dependent", "Depends_On": "Mission Type, Launch Vehicle, Mission Cost"},
       {"Column": "Fuel Consumption (tons)", "Role": "Dependent", "Depends_On": "Distance from Earth, Payload Weight"},
       {"Column": "Payload Weight (tons)", "Role": "Dependent", "Depends_On": "Crew Size, Mission Type"},
       {"Column": "Launch Vehicle", "Role": "Independent", "Depends_On": "-"},
       {"Column": "Risk", "Role": "Dependent", "Depends_On": "Payload Weight, Distance from Earth, Mission Type"},
       {"Column": "Scientific_Yield_Per_Year", "Role": "Dependent", "Depends_On": "Scientific Yield, Mission Duration"},
       {"Column": "Cost_Per_Crew_Member", "Role": "Dependent", "Depends_On": "Mission Cost, Crew Size"}
    ]   
    columns_df = pd.DataFrame(columns_info)

    # Split into dependent and independent
    dependent_vars = columns_df[columns_df["Role"] == "Dependent"]
    independent_vars = columns_df[columns_df["Role"] == "Independent"]

    # --- Display Dependent Variables ---
    st.subheader("🧮 Dependent Variables")
    st.dataframe(dependent_vars.reset_index(drop=True).rename_axis('').set_index(pd.Index(range(1, len(dependent_vars)+1))), use_container_width=True)
    st.caption("These variables are influenced by one or more independent features.")

    # --- Display Independent Variables ---
    st.subheader("🎯 Independent Variables")
    st.dataframe(independent_vars.reset_index(drop=True).rename_axis('').set_index(pd.Index(range(1, len(independent_vars)+1))), use_container_width=True)

    st.caption("These variables serve as inputs or predictors for modeling.")
