import streamlit as st
import pandas as pd
import numpy as np
from helpers import require_model

def show_recommendation():
    st.title("🔍 Cek Kategori Film")
    require_model()
    
    st.markdown("Masukkan data film baru untuk melihat masuk ke kelompok (cluster) mana film tersebut.")

    col1, col2 = st.columns(2)
    with col1:
        rating = st.number_input("Rating Film (0 - 10)", 0.0, 10.0, 7.0)
    with col2:
        pop = st.number_input("Popularitas", 0.0, 5000.0, 50.0)

    if st.button("Analisis Film"):
        # 1. Ambil Scaler dan Model
        scaler = st.session_state["scaler"]
        model = st.session_state["kmeans_model"]
        
        # 2. Scale data input
        input_data = pd.DataFrame([[rating, pop]], columns=st.session_state["features"])
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