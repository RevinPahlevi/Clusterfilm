import streamlit as st
from sklearn.cluster import KMeans
from helpers import require_clean_data, plot_elbow_method

def show_analysis():
    st.title("🕵️ Clustering Process")
    require_clean_data()
    
    df_scaled = st.session_state["scaled_df"]
    features = st.session_state["features"]
    
    # 1. Elbow Method
    with st.expander("📈 Lihat Elbow Method (Cari K Optimal)"):
        st.write("Grafik ini membantu menentukan jumlah cluster terbaik.")
        plot_elbow_method(df_scaled)

    # 2. Konfigurasi K-Means
    st.markdown("### Konfigurasi Model")
    k_clusters = st.slider("Pilih Jumlah Cluster (K)", min_value=2, max_value=10, value=3)

    if st.button("Mulai Clustering"):
        with st.spinner("Sedang mengelompokkan film..."):
            # Latih Model
            model = KMeans(n_clusters=k_clusters, random_state=42, n_init=10)
            X = df_scaled[features]
            model.fit(X)
            
            # Simpan hasil label ke session
            labels = model.labels_
            st.session_state["kmeans_model"] = model
            st.session_state["cluster_labels"] = labels
            
            # Gabungkan label ke dataframe clean untuk analisis
            st.session_state["clean_df"]["Cluster"] = labels
            
        st.success(f"✅ Berhasil membagi film menjadi {k_clusters} cluster!")
        st.rerun()

    # 3. Interpretasi Hasil
    if st.session_state.get("kmeans_model") is not None:
        st.markdown("### 📊 Rata-rata Fitur per Cluster")
        
        # Group by cluster untuk melihat karakteristik
        df_res = st.session_state["clean_df"]
        summary = df_res.groupby("Cluster")[features].mean().reset_index()
        
        st.dataframe(summary.style.background_gradient(cmap="Reds"))
        
        st.info("""
        **Cara Membaca:**
        - Lihat kolom 'vote_average' tertinggi -> Cluster Film Berkualitas.
        - Lihat kolom 'popularity' tertinggi -> Cluster Film Populer/Blockbuster.
        """)