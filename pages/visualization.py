import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from helpers import require_model, plot_clusters

def show_visualization():
    st.title("📊 Visualisasi Hasil Clustering")
    require_model()
    
    df = st.session_state["clean_df"]
    labels = st.session_state["cluster_labels"]
    centers = st.session_state["kmeans_model"].cluster_centers_

    tab1, tab2 = st.tabs(["Scatter Plot", "Jumlah Film"])

    with tab1:
        st.markdown("#### Persebaran Film (Rating vs Popularitas)")
        plot_clusters(df, labels, centers)
        
    with tab2:
        st.markdown("#### Jumlah Film per Cluster")
        fig, ax = plt.subplots()
        sns.countplot(x='Cluster', data=df, palette='viridis', ax=ax)
        ax.set_ylabel("Jumlah Film")
        st.pyplot(fig)