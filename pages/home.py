# pages/home.py
import streamlit as st
import pandas as pd

from data.load_data import load_data
from tabs import data_overview, categorical_analysis, numerical_analysis , prediction
from filters.sidebar_filters import apply_sidebar_filters

st.set_page_config(page_title="Space Missions Dashboard", layout="wide")
st.title("🚀 Global Space Missions Dashboard")

# Load data and apply filters
df, cleaning_log = load_data()
df_filtered, selected_mission, selected_target = apply_sidebar_filters(df)

# Define tabs
tab0, tab1, tab2 , tab3  = st.tabs([
    "📡 Mission Data Overview",
    "📊 Categorical Analysis",
    "📈 Numerical Analysis",
    "🔮 Prediction "
])

# Render tabs
with tab0:
    data_overview.render(df_filtered)

with tab1:
    categorical_analysis.render(df_filtered)

with tab2:
    numerical_analysis.render(df_filtered)
    
with tab3:
    prediction.render(df_filtered)
