import pandas as pd
import numpy as np
import streamlit as st
import os

@st.cache_data(ttl=900)
def load_data():
    # Load dataset from local path
    file_path = os.path.join(os.path.dirname(__file__), 'space_missions_dataset.csv')
    df_raw = pd.read_csv(file_path)

    # Replace common missing values with np.nan
    df_raw.replace(["None", "none", "N/A", "nan", "", "-", "?"], np.nan, inplace=True)

    # Copy raw data for cleaning
    df_clean = df_raw.copy()
    logs = []

    # Convert 'Launch Date' to datetime
    # Convert 'Launch Date' to datetime
    if 'Launch Date' in df_clean.columns:
        df_clean['Launch Date'] = pd.to_datetime(df_clean['Launch Date'], errors='coerce', dayfirst=False)
        affected = df_clean[df_clean['Launch Date'].isna()].copy()
        if not affected.empty:
            affected["__Action__"] = "Invalid or missing launch date"
            logs.append(affected)
        df_clean.dropna(subset=['Launch Date'], inplace=True)


    # Clean and convert 'Mission Cost (billion USD)' to float
    if 'Mission Cost (billion USD)' in df_clean.columns:
        df_clean['Mission Cost (billion USD)'] = df_clean['Mission Cost (billion USD)'].astype(str)
        df_clean['Mission Cost (billion USD)'] = df_clean['Mission Cost (billion USD)'].str.replace(r'[$,]', '', regex=True)
        df_clean['Mission Cost (billion USD)'] = pd.to_numeric(df_clean['Mission Cost (billion USD)'], errors='coerce')

    # Convert numeric fields safely
    numeric_cols = [
        "Distance from Earth (light-years)",
        "Mission Duration (years)",
        "Mission Cost (billion USD)",
        "Scientific Yield (points)",
        "Crew Size",
        "Mission Success (%)",
        "Fuel Consumption (tons)",
        "Payload Weight (tons)"
    ]

    for col in numeric_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

    # Impute missing values
    for col in df_clean.columns:
        if df_clean[col].isna().sum() == 0:
            continue
        affected = df_clean[df_clean[col].isna()].copy()
        if pd.api.types.is_numeric_dtype(df_clean[col]):
            value = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(value)
            affected["__Action__"] = f"Imputed Median: {value}"
        else:
            value = df_clean[col].mode().iloc[0]
            df_clean[col] = df_clean[col].fillna(value)
            affected["__Action__"] = f"Imputed Mode: '{value}'"
        logs.append(affected)

    # Derive 'Launch Year' column
    df_clean["Launch Year"] = df_clean["Launch Date"].dt.year
    bins = [0, 50, 100, 250, 500, float('inf')]
    labels = ['Very Low Budget', 'Low Budget', 'Moderate Budget', 'High Budget', 'Very High Budget']
    df_clean['Budget Category'] = pd.cut( df_clean['Mission Cost (billion USD)'], bins=bins,labels=labels)
    # Mark risky missions
    df_clean['High Risk'] = df_clean['Mission Success (%)'] < 80
    
    #This shows how efficient the mission is in terms of scientific return per year of operation.
    # Calculate scientific productivity rate
    df_clean['Scientific Yield per Year'] = df_clean['Scientific Yield (points)'] / df_clean['Mission Duration (years)']

    # Combine cleaning logs
    cleaning_log = pd.concat(logs) if logs else pd.DataFrame()
    
    #this adds a column that tells how many each crew memeber cost
    df_clean['Cost per Crew Member'] = df_clean.apply(
    lambda row: row['Mission Cost (billion USD)'] / row['Crew Size']
    if row['Crew Size'] > 0 else np.nan,
    axis=1
    )

    return df_clean, cleaning_log
