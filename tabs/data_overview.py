import streamlit as st

def render(df):
    st.header("📡 Mission Data Overview")

    # Section: About Dataset
    st.markdown("""
    ### 🛰️ About the Dataset

    This dataset is a **synthetic yet realistic** simulation of space missions. It includes structured details on launch dates, mission types, destination targets, mission costs, success rates, fuel consumption, payloads, and more.

    🔍 Although the data is not sourced from real-world missions, it is designed to mimic realistic conditions and diversity found in actual space programs, making it ideal for:

    - Exploratory Data Analysis (EDA)
    - Machine Learning experimentation
    - Visualization and dashboard building
    - Educational and academic projects

    This dashboard allows us to explore:
    - What kinds of missions are launched (e.g., colonization, research)
    - Which targets are most common (e.g., planets, moons, exoplanets)
    - How success rate and scientific yield vary across mission types
    - Trends in mission costs, crew sizes, and technologies over time

    ---
    """)

    # Section: Sample of the Data
    st.subheader("📋 Sample of the Data")
    st.dataframe(df.head(10), use_container_width=True)

    # Section: Quick Info
    st.markdown(f"""
    **🔢 Dataset Shape:** `{df.shape[0]} rows × {df.shape[1]} columns`  
    **🧾 Available Columns:** `{', '.join(df.columns)}`  
    """)
