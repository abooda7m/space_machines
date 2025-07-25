# # This is filters/sidebar_filters.py

# import streamlit as st
# import pandas as pd

# def apply_filters(df):
#     st.sidebar.header("🔎 Filters")

#     if "selected_region" not in st.session_state:
#         st.session_state["selected_region"] = df["Region"].dropna().unique().tolist()
#     if "selected_category" not in st.session_state:
#         st.session_state["selected_category"] = df["Category"].dropna().unique().tolist()
#     if "date_range" not in st.session_state:
#         st.session_state["date_range"] = [df["Order Date"].min(), df["Order Date"].max()]

#     if st.sidebar.button("🔄 Reset Filters"):
#         st.session_state.clear()
#         st.rerun()

#     selected_region = st.sidebar.multiselect("Select Region", df["Region"].dropna().unique(), default=st.session_state["selected_region"])
#     if len(selected_region) == 0:
#         st.sidebar.warning("⚠️ You must select at least one Region.")
#         selected_region = st.session_state["selected_region"]
#     else:
#         st.session_state["selected_region"] = selected_region

#     selected_category = st.sidebar.multiselect("Select Category", df["Category"].dropna().unique(), default=st.session_state["selected_category"])
#     if len(selected_category) == 0:
#         st.sidebar.warning("⚠️ You must select at least one Category.")
#         selected_category = st.session_state["selected_category"]
#     else:
#         st.session_state["selected_category"] = selected_category

#     date_range = st.sidebar.date_input("Select Date Range", value=st.session_state["date_range"])
#     st.session_state["date_range"] = date_range

#     return df[
#         (df["Region"].isin(selected_region)) &
#         (df["Category"].isin(selected_category)) &
#         (df["Order Date"] >= pd.to_datetime(date_range[0])) &
#         (df["Order Date"] <= pd.to_datetime(date_range[1]))
#     ]


import streamlit as st

def apply_sidebar_filters(df):
    st.sidebar.header("🔍 Filter Options")

    # Mission Type Filter (Multiple Selection)
    all_mission_types = sorted(df["Mission Type"].dropna().unique().tolist())
    default_missions = st.session_state.get("selected_missions", all_mission_types)
    selected_missions = st.sidebar.multiselect("Mission Type", all_mission_types, default=default_missions)
    if not selected_missions:
        st.sidebar.warning("⚠️ Please select at least one Mission Type.")
        selected_missions = default_missions

    # Target Type Filter (Multiple Selection)
    all_target_types = sorted(df["Target Type"].dropna().unique().tolist())
    default_targets = st.session_state.get("selected_targets", all_target_types)
    selected_targets = st.sidebar.multiselect("Target Type", all_target_types, default=default_targets)
    if not selected_targets:
        st.sidebar.warning("⚠️ Please select at least one Target Type.")
        selected_targets = default_targets

    # Save current selections to session_state
    st.session_state["selected_missions"] = selected_missions
    st.session_state["selected_targets"] = selected_targets

    # Apply Filters
    filtered_df = df[
        df["Mission Type"].isin(selected_missions) &
        df["Target Type"].isin(selected_targets)
    ]

    return filtered_df, selected_missions, selected_targets
