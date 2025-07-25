# # home.py

# # Import necessary libraries and modules
# import streamlit as st
# import pandas as pd

# # Import custom data loader
# from data.load_data import load_data

# # Import dashboard tabs
# from tabs import (
#     data_overview,
#     analysis,
# )

# # Configure Streamlit page
# st.set_page_config(page_title="Space Missions Dashboard", layout="wide")
# st.title("🚀 Global Space Missions Dashboard")

# # Load the cleaned dataset and cleaning log
# df, cleaning_log_df = load_data()

# # Define main navigation tabs (2 only)
# tab0, tab1 = st.tabs([
#     "📡 Mission Data Overview",
#     "🌍 Mission Analysis",
# ])

# # Render tab contents
# with tab0:
#     data_overview.render(df)

# with tab1:
#     analysis.render(df)





# home.py

import streamlit as st
import pandas as pd

from data.load_data import load_data
from tabs import data_overview, categorical_analysis, numerical_analysis
from filters.sidebar_filters import apply_sidebar_filters

st.set_page_config(page_title="Space Missions Dashboard", layout="wide")
st.title("🚀 Global Space Missions Dashboard")

# Load data and apply filters
df, cleaning_log = load_data()
df_filtered, selected_mission, selected_target = apply_sidebar_filters(df)

# Define tabs
tab0, tab1, tab2 = st.tabs([
    "📡 Mission Data Overview",
    "📊 Categorical Analysis",
    "📈 Numerical Analysis"
])

# Render tabs
with tab0:
    data_overview.render(df_filtered)

with tab1:
    categorical_analysis.render(df_filtered)

with tab2:
    numerical_analysis.render(df_filtered)
