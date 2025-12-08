import streamlit as st
from state import init_session_state
from style import add_custom_css

# Import Pages
from pages.home import show_home
from pages.upload_dataset import show_upload_dataset
from pages.preprocessing import show_preprocessing
from pages.analysis import show_analysis
from pages.visualization import show_visualization
from pages.recommendation import show_recommendation
from pages.about import show_about

st.set_page_config(page_title="Film Clustering System", layout="wide")
init_session_state()
add_custom_css() # Gunakan style.py yang sama, atau sesuaikan warna

# --- SIDEBAR ---
with st.sidebar:
    # Logo - centered dan lebih kecil
    st.image("static/logo.png", width=100)
    st.markdown("---")
    
    menu = ["Home", "Upload Dataset", "Preprocessing", "Clustering Process", "Visualization", "Rekomendasi", "About"]
    
    # Get current page
    current_page = st.session_state.get("page", "Home")
    
    for item in menu:
        # Set button type based on active page
        button_type = "primary" if item == current_page else "secondary"
        
        if st.button(item, type=button_type, use_container_width=True, key=f"nav_{item}"):
            st.session_state["page"] = item
            st.rerun()

# --- ROUTER ---
page = st.session_state["page"]

if page == "Home": show_home()
elif page == "Upload Dataset": show_upload_dataset()
elif page == "Preprocessing": show_preprocessing()
elif page == "Clustering Process": show_analysis() # Dahulu Analysis
elif page == "Visualization": show_visualization()
elif page == "Rekomendasi": show_recommendation() # Dahulu Prediction
elif page == "About": show_about()