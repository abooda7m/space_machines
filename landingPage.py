import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Space Missions EDA | Space Analytics",
    page_icon="🚀",
    layout="centered"
)

# Title and welcome message
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color:#1f77b4;'>Welcome to the Space Missions EDA</h1>
        <h3>Explore, Analyze, and Visualize Humanity's Greatest Missions</h3>
        <p style='max-width: 600px; margin: auto; font-size: 18px; color: gray;'>
            This interactive dashboard allows you to dive deep into the history of global space missions, analyze trends across agencies and technologies, 
            and uncover insights behind mission outcomes, targets, and scientific achievements.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Centered Launch button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Launch Dashboard"):
        st.switch_page("pages/home.py")  # adjust path based on your routing
