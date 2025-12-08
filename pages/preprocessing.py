import streamlit as st
from helpers import require_raw_data, preprocess_data

def show_preprocessing():
    require_raw_data()
    
    df_raw = st.session_state["raw_df"]
    features = st.session_state["features"]
    
    # ===== HEADER SECTION =====
    st.markdown("""
        <div class="preprocessing-header">
            <div class="preprocessing-icon">🛠️</div>
            <h1 class="preprocessing-title">Preprocessing & Scaling</h1>
            <p class="preprocessing-subtitle">Persiapkan data untuk algoritma K-Means Clustering</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== INFO SECTION - Why Scaling? =====
    st.markdown("""
        <div class="scaling-info-card">
            <div class="info-header">
                <span class="info-icon">💡</span>
                <span class="info-title">Mengapa Perlu Scaling?</span>
            </div>
            <div class="info-content">
                <p>K-Means Clustering sangat sensitif terhadap <strong>skala data</strong>. 
                Tanpa normalisasi, fitur dengan nilai besar (seperti Popularitas: 0-1000+) 
                akan mendominasi perhitungan jarak dibanding fitur dengan nilai kecil 
                (seperti Rating: 0-10).</p>
                <div class="scaling-visual">
                    <div class="scale-before">
                        <span class="scale-label">Sebelum</span>
                        <div class="scale-bars">
                            <div class="bar rating-bar" style="width: 10%;">Rating: 0-10</div>
                            <div class="bar popularity-bar" style="width: 100%;">Popularity: 0-1000+</div>
                        </div>
                    </div>
                    <div class="scale-arrow">→</div>
                    <div class="scale-after">
                        <span class="scale-label">Sesudah</span>
                        <div class="scale-bars">
                            <div class="bar rating-bar-after" style="width: 50%;">Rating: -2 to 2</div>
                            <div class="bar popularity-bar-after" style="width: 50%;">Popularity: -2 to 2</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== RAW DATA PREVIEW =====
    st.markdown("""
        <div class="data-section-header">
            <span class="section-badge">📊</span>
            <span class="section-text">Preview Data Mentah</span>
            <span class="data-count">{} baris</span>
        </div>
    """.format(len(df_raw)), unsafe_allow_html=True)
    
    st.dataframe(df_raw.head(5), use_container_width=True)
    
    # ===== FEATURES INFO =====
    st.markdown("""
        <div class="features-info">
            <span class="features-label">📌 Fitur yang digunakan:</span>
            <div class="features-tags">
                <span class="feature-tag">⭐ vote_average</span>
                <span class="feature-tag">🔥 popularity</span>
                <span class="feature-tag">📊 vote_count</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== PROCESS BUTTON =====
    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
    
    col_left, col_center, col_right = st.columns([2, 3, 2])
    with col_center:
        if st.button("⚡ Jalankan Preprocessing", type="primary", use_container_width=True, key="run_preprocessing"):
            with st.spinner("🔄 Memproses data..."):
                # df_clean = data asli yang bersih barisnya
                # df_scaled = data numerik yang sudah di-scale (untuk mesin)
                df_clean, df_scaled, scaler = preprocess_data(df_raw)
                
                st.session_state["clean_df"] = df_clean    # Data asli (untuk visualisasi user)
                st.session_state["scaled_df"] = df_scaled  # Data scale (untuk algoritma)
                st.session_state["scaler"] = scaler        # Simpan scaler
                
                st.success("✅ Data berhasil dibersihkan dan dinormalisasi!")
                st.rerun()

    # ===== HASIL PREPROCESSING =====
    if st.session_state.get("clean_df") is not None:
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
        
        # Success Banner
        st.markdown("""
            <div class="preprocessing-success-banner">
                <div class="success-checkmark">✓</div>
                <div class="success-content">
                    <span class="success-title">Preprocessing Berhasil!</span>
                    <span class="success-desc">Data telah dinormalisasi menggunakan StandardScaler</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Comparison Section Header
        st.markdown("""
            <div class="comparison-header">
                <h2 class="comparison-title">📊 Perbandingan Data</h2>
                <p class="comparison-desc">Lihat perbedaan nilai sebelum dan sesudah scaling</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Two Column Comparison
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            st.markdown("""
                <div class="data-card before-card">
                    <div class="card-header before-header">
                        <span class="card-icon">📋</span>
                        <span class="card-title">Data Asli (Clean)</span>
                    </div>
                    <p class="card-desc">Nilai original setelah pembersihan</p>
                </div>
            """, unsafe_allow_html=True)
            st.dataframe(
                st.session_state["clean_df"][features].head(), 
                use_container_width=True
            )
        
        with col2:
            st.markdown("""
                <div class="data-card after-card">
                    <div class="card-header after-header">
                        <span class="card-icon">🔄</span>
                        <span class="card-title">Data Hasil Scaling</span>
                    </div>
                    <p class="card-desc">Nilai normalisasi (mean=0, std=1)</p>
                </div>
            """, unsafe_allow_html=True)
            st.dataframe(
                st.session_state["scaled_df"][features].head(), 
                use_container_width=True
            )
        
        # Statistics Cards
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        
        clean_df = st.session_state["clean_df"]
        
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        
        with stat_col1:
            st.markdown(f"""
                <div class="stat-metric-card">
                    <div class="metric-icon">🎬</div>
                    <div class="metric-value">{len(clean_df):,}</div>
                    <div class="metric-label">Total Film</div>
                </div>
            """, unsafe_allow_html=True)
        
        with stat_col2:
            st.markdown(f"""
                <div class="stat-metric-card">
                    <div class="metric-icon">📊</div>
                    <div class="metric-value">{len(features)}</div>
                    <div class="metric-label">Fitur Digunakan</div>
                </div>
            """, unsafe_allow_html=True)
        
        with stat_col3:
            removed = len(df_raw) - len(clean_df)
            st.markdown(f"""
                <div class="stat-metric-card">
                    <div class="metric-icon">🗑️</div>
                    <div class="metric-value">{removed:,}</div>
                    <div class="metric-label">Baris Dihapus</div>
                </div>
            """, unsafe_allow_html=True)
        
        # Next Button
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
        
        col_spacer1, col_next, col_spacer2 = st.columns([5, 2, 1])
        with col_next:
            if st.button("Next: Clustering Process ›", type="primary", use_container_width=True, key="preprocessing_next"):
                st.session_state["page"] = "Clustering Process"
                st.rerun()