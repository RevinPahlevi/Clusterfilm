import streamlit as st

def init_session_state():
    # Halaman default
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    # Dataframes
    if "raw_df" not in st.session_state:
        st.session_state["raw_df"] = None
    if "clean_df" not in st.session_state:
        st.session_state["clean_df"] = None

    # Model & Scaler (Penting untuk K-Means)
    if "kmeans_model" not in st.session_state:
        st.session_state["kmeans_model"] = None
    if "scaler" not in st.session_state:
        st.session_state["scaler"] = None
    if "cluster_labels" not in st.session_state:
        st.session_state["cluster_labels"] = None

    # Fitur yang digunakan untuk clustering - SELALU set ulang
    st.session_state["features"] = [
        "vote_average",  # Rating
        "popularity",    # Popularitas
        "vote_count"     # Jumlah Vote
    ]