import streamlit as st
import pandas as pd
import numpy as np
from helpers import require_model

def show_recommendation():
    st.title("🔍 Cek Kategori Film")
    require_model()
    
    # Cek kompatibilitas model dengan fitur
    scaler = st.session_state.get("scaler")
    features = st.session_state["features"]
    
    if scaler is not None:
        # Cek apakah scaler dilatih dengan jumlah fitur yang sama
        if hasattr(scaler, 'n_features_in_') and scaler.n_features_in_ != len(features):
            st.error(f"""
            ⚠️ **Model tidak kompatibel!**
            
            Model saat ini dilatih dengan **{scaler.n_features_in_} fitur**, 
            tapi konfigurasi sekarang menggunakan **{len(features)} fitur** ({', '.join(features)}).
            
            **Silakan lakukan langkah berikut:**
            1. Kembali ke **Preprocessing** dan jalankan ulang
            2. Lakukan **Clustering Process** ulang
            3. Kembali ke halaman ini
            """)
            st.stop()
    
    st.markdown("Masukkan data film baru untuk melihat masuk ke kelompok (cluster) mana film tersebut.")

    col1, col2, col3 = st.columns(3)
    with col1:
        rating = st.number_input("Rating Film (0 - 10)", 0.0, 10.0, 7.0)
    with col2:
        pop = st.number_input("Popularitas", 0.0, 5000.0, 50.0)
    with col3:
        vote_count = st.number_input("Jumlah Vote", 0, 50000, 1000)

    if st.button("Analisis Film"):
        # 1. Ambil Scaler dan Model
        scaler = st.session_state["scaler"]
        model = st.session_state["kmeans_model"]
        
        # 2. Scale data input (3 fitur: vote_average, popularity, vote_count)
        input_data = pd.DataFrame([[rating, pop, vote_count]], columns=features)
        input_scaled = scaler.transform(input_data)
        
        # 3. Prediksi Cluster
        cluster_pred = model.predict(input_scaled)[0]
        
        st.success(f"🎥 Film ini masuk ke **Cluster {cluster_pred}**")
        
        # 4. Rekomendasi Film Serupa
        df = st.session_state["clean_df"]
        similar_films = df[df['Cluster'] == cluster_pred]
        
        # Jika ada kolom judul
        if 'title' in df.columns:
            st.markdown(f"### Film lain di Cluster {cluster_pred}:")
            st.write(", ".join(similar_films['title'].head(10).tolist()))
        else:
            st.markdown(f"### Statistik Cluster {cluster_pred}:")
            st.write(similar_films.describe())