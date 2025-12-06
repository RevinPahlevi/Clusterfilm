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
    st.title("🎬 MovieClusters")
    st.markdown("---")
    
    menu = ["Home", "Upload Dataset", "Preprocessing", "Clustering Process", "Visualization", "Rekomendasi", "About"]
    
    for item in menu:
        if st.button(item, use_container_width=True):
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