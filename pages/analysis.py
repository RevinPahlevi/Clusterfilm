import streamlit as st
from sklearn.cluster import KMeans
from helpers import require_clean_data, plot_elbow_method

def show_analysis():
    require_clean_data()
    
    df_scaled = st.session_state["scaled_df"]
    features = st.session_state["features"]
    
    # ===== HEADER SECTION =====
    st.markdown("""
        <div class="clustering-header">
            <div class="clustering-icon">🕵️</div>
            <h1 class="clustering-title">Clustering Process</h1>
            <p class="clustering-subtitle">Kelompokkan film menggunakan algoritma K-Means</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== WHAT IS K-MEANS =====
    st.markdown("""
        <div class="kmeans-info-card">
            <div class="kmeans-info-header">
                <span class="kmeans-info-icon">🤖</span>
                <span class="kmeans-info-title">Apa itu K-Means?</span>
            </div>
            <p class="kmeans-info-text">
                K-Means adalah algoritma <strong>unsupervised learning</strong> yang mengelompokkan 
                data ke dalam <strong>K cluster</strong> berdasarkan kesamaan fitur. 
                Film dengan rating dan popularitas serupa akan masuk ke cluster yang sama.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== STEP 1: ELBOW METHOD =====
    st.markdown("""
        <div class="step-section">
            <div class="step-badge">1</div>
            <div class="step-info">
                <span class="step-name">Tentukan Jumlah Cluster Optimal</span>
                <span class="step-desc">Gunakan Elbow Method untuk menemukan nilai K terbaik</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📈 Lihat Grafik Elbow Method", expanded=False):
        st.markdown("""
            <div class="elbow-explanation">
                <p>📌 <strong>Cara membaca grafik:</strong> Pilih titik dimana penurunan mulai melambat 
                (membentuk "siku"). Biasanya K=3 atau K=4 adalah pilihan yang baik.</p>
            </div>
        """, unsafe_allow_html=True)
        plot_elbow_method(df_scaled)
    
    # ===== STEP 2: KONFIGURASI =====
    st.markdown("""
        <div class="step-section">
            <div class="step-badge">2</div>
            <div class="step-info">
                <span class="step-name">Konfigurasi & Jalankan Clustering</span>
                <span class="step-desc">Pilih jumlah cluster dan mulai proses clustering</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Config Card
    st.markdown("""
        <div class="config-card">
            <div class="config-header">
                <span class="config-icon">⚙️</span>
                <span class="config-title">Pengaturan Model</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        k_clusters = st.slider(
            "Pilih Jumlah Cluster (K)", 
            min_value=2, 
            max_value=10, 
            value=3,
            help="Tentukan berapa banyak kelompok untuk membagi film"
        )
    
    with col2:
        st.markdown(f"""
            <div class="cluster-preview">
                <div class="preview-value">{k_clusters}</div>
                <div class="preview-label">Cluster</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Clustering Button
    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
    
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🚀 Mulai Clustering", type="primary", use_container_width=True):
            with st.spinner("🔄 Mengelompokkan film..."):
                # Train Model
                model = KMeans(n_clusters=k_clusters, random_state=42, n_init=10)
                X = df_scaled[features]
                model.fit(X)
                
                # Save results
                labels = model.labels_
                st.session_state["kmeans_model"] = model
                st.session_state["cluster_labels"] = labels
                st.session_state["clean_df"]["Cluster"] = labels
                
            st.success(f"✅ Berhasil membagi film menjadi {k_clusters} cluster!")
            st.rerun()

    # ===== STEP 3: HASIL =====
    if st.session_state.get("kmeans_model") is not None:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        st.markdown("""
            <div class="step-section success-step">
                <div class="step-badge success-badge">✓</div>
                <div class="step-info">
                    <span class="step-name">Hasil Clustering</span>
                    <span class="step-desc">Analisis karakteristik setiap cluster</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Results Summary
        df_res = st.session_state["clean_df"]
        summary = df_res.groupby("Cluster")[features].mean().reset_index()
        n_clusters = len(summary)
        
        # Stats Cards
        stat1, stat2, stat3 = st.columns(3)
        
        with stat1:
            st.markdown(f"""
                <div class="result-stat-card">
                    <div class="result-stat-icon">📊</div>
                    <div class="result-stat-value">{n_clusters}</div>
                    <div class="result-stat-label">Total Cluster</div>
                </div>
            """, unsafe_allow_html=True)
        
        with stat2:
            st.markdown(f"""
                <div class="result-stat-card">
                    <div class="result-stat-icon">🎬</div>
                    <div class="result-stat-value">{len(df_res):,}</div>
                    <div class="result-stat-label">Film Diproses</div>
                </div>
            """, unsafe_allow_html=True)
        
        with stat3:
            avg_per_cluster = len(df_res) // n_clusters
            st.markdown(f"""
                <div class="result-stat-card">
                    <div class="result-stat-icon">📈</div>
                    <div class="result-stat-value">~{avg_per_cluster:,}</div>
                    <div class="result-stat-label">Rata-rata/Cluster</div>
                </div>
            """, unsafe_allow_html=True)
        
        # Results Table Header
        st.markdown("""
            <div class="results-table-header">
                <span class="table-header-icon">📋</span>
                <span class="table-header-text">Rata-rata Fitur per Cluster</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.dataframe(summary.style.background_gradient(cmap="Blues"), use_container_width=True)
        
        # Interpretation Card
        st.markdown("""
            <div class="interpretation-card">
                <div class="interp-header">
                    <span class="interp-icon">💡</span>
                    <span class="interp-title">Cara Membaca Hasil</span>
                </div>
                <div class="interp-content">
                    <div class="interp-item">
                        <span class="interp-bullet">⭐</span>
                        <span>Cluster dengan <strong>vote_average tertinggi</strong> → Film Berkualitas</span>
                    </div>
                    <div class="interp-item">
                        <span class="interp-bullet">🔥</span>
                        <span>Cluster dengan <strong>popularity tertinggi</strong> → Film Populer/Blockbuster</span>
                    </div>
                    <div class="interp-item">
                        <span class="interp-bullet">📊</span>
                        <span>Cluster dengan <strong>vote_count tertinggi</strong> → Film Banyak Ditonton</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Navigation
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        col_spacer, col_next = st.columns([6, 2])
        with col_next:
            if st.button("Next: Visualization ›", type="primary", use_container_width=True, key="clustering_next"):
                st.session_state["page"] = "Visualization"
                st.rerun()