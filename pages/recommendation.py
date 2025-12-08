import streamlit as st
import pandas as pd
import numpy as np
from helpers import require_model

def show_recommendation():
    require_model()
    
    # Cek kompatibilitas model dengan fitur
    scaler = st.session_state.get("scaler")
    features = st.session_state["features"]
    
    if scaler is not None:
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
    
    # ===== HEADER SECTION =====
    st.markdown("""
        <div class="reko-header">
            <div class="reko-icon">🔍</div>
            <h1 class="reko-title">Cek Kategori Film</h1>
            <p class="reko-subtitle">Prediksi cluster film berdasarkan karakteristik</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== INFO CARD =====
    st.markdown("""
        <div class="reko-info-card">
            <span class="reko-info-icon">💡</span>
            <span class="reko-info-text">Masukkan karakteristik film untuk melihat masuk ke kategori (cluster) mana film tersebut.</span>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== INPUT SECTION =====
    st.markdown("""
        <div class="input-section-header">
            <span class="ish-icon">🎛️</span>
            <span class="ish-title">Input Karakteristik Film</span>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="input-card">
                <span class="input-card-icon">⭐</span>
                <span class="input-card-title">Rating Film</span>
            </div>
        """, unsafe_allow_html=True)
        rating = st.slider(
            "Rating (0 - 10)", 
            min_value=0.0, 
            max_value=10.0, 
            value=7.0,
            step=0.1,
            help="Rating film dalam skala 0-10",
            label_visibility="collapsed"
        )
        st.markdown(f"""<div class="slider-value">{rating:.1f}<span>/10</span></div>""", unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="input-card">
                <span class="input-card-icon">🔥</span>
                <span class="input-card-title">Popularitas</span>
            </div>
        """, unsafe_allow_html=True)
        pop = st.slider(
            "Popularitas (0 - 1000)", 
            min_value=0.0, 
            max_value=1000.0, 
            value=50.0,
            step=1.0,
            help="Tingkat popularitas film",
            label_visibility="collapsed"
        )
        st.markdown(f"""<div class="slider-value">{pop:.0f}</div>""", unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="input-card">
                <span class="input-card-icon">📊</span>
                <span class="input-card-title">Jumlah Vote</span>
            </div>
        """, unsafe_allow_html=True)
        vote_count = st.slider(
            "Vote Count (0 - 50,000)", 
            min_value=0, 
            max_value=50000, 
            value=1000,
            step=100,
            help="Jumlah vote/rating",
            label_visibility="collapsed"
        )
        st.markdown(f"""<div class="slider-value">{vote_count:,}</div>""", unsafe_allow_html=True)

    # ===== ANALYZE BUTTON =====
    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
    
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        analyze_clicked = st.button("🎬 Analisis Film", type="primary", use_container_width=True)
    
    if analyze_clicked:
        # 1. Ambil Scaler dan Model
        scaler = st.session_state["scaler"]
        model = st.session_state["kmeans_model"]
        
        # 2. Scale data input
        input_data = pd.DataFrame([[rating, pop, vote_count]], columns=features)
        input_scaled = scaler.transform(input_data)
        
        # 3. Prediksi Cluster
        cluster_pred = model.predict(input_scaled)[0]
        
        # 4. Ambil interpretasi cluster
        from helpers import interpret_clusters
        df = st.session_state["clean_df"]
        interpretations = interpret_clusters(df)
        cluster_info = interpretations[cluster_pred]
        
        # ===== RESULT SECTION =====
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        st.markdown("""
            <div class="result-header">
                <span class="result-h-icon">🎯</span>
                <span class="result-h-title">Hasil Analisis</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Prediction Card
        st.markdown(f"""
            <div class="prediction-card">
                <div class="pred-badge">Cluster {cluster_pred}</div>
                <div class="pred-label">{cluster_info['label']}</div>
                <p class="pred-desc">{cluster_info['description']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Stats Row
        stat1, stat2, stat3 = st.columns(3)
        
        with stat1:
            st.markdown(f"""
                <div class="reko-stat-card">
                    <span class="reko-stat-icon">⭐</span>
                    <span class="reko-stat-value">{cluster_info['avg_rating']:.1f}</span>
                    <span class="reko-stat-label">Avg Rating</span>
                </div>
            """, unsafe_allow_html=True)
        
        with stat2:
            st.markdown(f"""
                <div class="reko-stat-card">
                    <span class="reko-stat-icon">🔥</span>
                    <span class="reko-stat-value">{cluster_info['avg_popularity']:.0f}</span>
                    <span class="reko-stat-label">Avg Popularity</span>
                </div>
            """, unsafe_allow_html=True)
        
        with stat3:
            st.markdown(f"""
                <div class="reko-stat-card">
                    <span class="reko-stat-icon">🎬</span>
                    <span class="reko-stat-value">{cluster_info['count']:,}</span>
                    <span class="reko-stat-label">Total Film</span>
                </div>
            """, unsafe_allow_html=True)
        
        # Similar Films
        similar_films = df[df['Cluster'] == cluster_pred]
        
        if 'title' in df.columns:
            st.markdown(f"""
                <div class="films-header">
                    <span class="films-h-icon">🎬</span>
                    <span class="films-h-title">Film Lain di {cluster_info['label']}</span>
                </div>
            """, unsafe_allow_html=True)
            
            top_films = similar_films.nlargest(10, 'vote_average')
            
            # Films grid (2 columns)
            film_cols = st.columns(2)
            for idx, (_, film) in enumerate(top_films.iterrows()):
                col_idx = idx % 2
                with film_cols[col_idx]:
                    st.markdown(f"""
                        <div class="film-item">
                            <span class="film-rank">{idx + 1}</span>
                            <div class="film-info">
                                <span class="film-title">{film['title'][:40]}{'...' if len(str(film['title'])) > 40 else ''}</span>
                                <span class="film-rating">⭐ {film['vote_average']:.1f}</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown(f"#### 📈 Statistik Detail Cluster {cluster_pred}")
            st.dataframe(similar_films[features].describe(), use_container_width=True)
        
        # PDF Download
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        from helpers import generate_recommendation_pdf
        from datetime import datetime
        
        input_dict = {'rating': rating, 'popularity': pop, 'vote_count': vote_count}
        
        pdf_bytes = generate_recommendation_pdf(
            input_data=input_dict,
            cluster_pred=cluster_pred,
            cluster_info=cluster_info,
            similar_films=similar_films,
            features=features
        )
        
        filename = f"Analisis_Film_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        col_dl1, col_dl2, col_dl3 = st.columns([2, 2, 2])
        with col_dl2:
            st.download_button(
                label="📄 Download Laporan PDF",
                data=pdf_bytes,
                file_name=filename,
                mime="application/pdf",
                use_container_width=True,
                type="secondary"
            )