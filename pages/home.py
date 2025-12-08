import streamlit as st

def show_home():
    # Load logo dan convert ke base64
    import base64
    from pathlib import Path
    
    logo_path = Path("static/logo.png")
    if logo_path.exists():
        with open(logo_path, "rb") as img_file:
            logo_base64 = base64.b64encode(img_file.read()).decode()
        logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="hero-logo-inline" alt="Logo">'
    else:
        logo_html = '🎬'
    
    # Hero Section dengan Logo inline
    st.markdown(f"""
        <div class="hero-section">
            <h1 class="hero-title" style="text-align: center !important;">
                {logo_html} Movie Clustering System
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Intro Section
    st.markdown("""
        <div class="intro-section">
            <p class="intro-text">
                Sistem ini menggunakan <strong>K-Means Clustering</strong> untuk mengelompokkan film 
                berdasarkan <strong>Rating</strong> dan <strong>Popularitas</strong>, 
                membantu Anda menemukan insight menarik dari ribuan data film.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature Cards - 3 columns
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Analisis Data</h3>
                <p class="feature-desc">Upload dan proses dataset film dengan mudah</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <h3 class="feature-title">K-Means ML</h3>
                <p class="feature-desc">Clustering otomatis dengan algoritma machine learning</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📈</div>
                <h3 class="feature-title">Visualisasi</h3>
                <p class="feature-desc">Lihat hasil clustering dalam grafik interaktif</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # How it Works Section
    st.markdown("""
        <div class="how-it-works">
            <h2 class="section-title">📋 Cara Menggunakan</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Steps in 2 columns
    col_left, col_right = st.columns(2, gap="large")
    
    with col_left:
        st.markdown("""
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h4 class="step-title">📂 Upload Dataset</h4>
                    <p class="step-desc">Unggah file CSV dengan kolom rating dan popularitas film</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h4 class="step-title">🛠️ Preprocessing</h4>
                    <p class="step-desc">Normalisasi data agar siap diproses oleh algoritma</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h4 class="step-title">🕵️ Clustering Process</h4>
                    <p class="step-desc">Tentukan jumlah cluster dan jalankan K-Means</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        st.markdown("""
            <div class="step-card">
                <div class="step-number">4</div>
                <div class="step-content">
                    <h4 class="step-title">📊 Visualization</h4>
                    <p class="step-desc">Lihat grafik penyebaran cluster film Anda</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="step-card">
                <div class="step-number">5</div>
                <div class="step-content">
                    <h4 class="step-title">🔍 Rekomendasi</h4>
                    <p class="step-desc">Prediksi kategori film baru dan temukan film serupa</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="step-card">
                <div class="step-number">6</div>
                <div class="step-content">
                    <h4 class="step-title">📥 Download</h4>
                    <p class="step-desc">Export hasil analisis dalam format PDF</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("""
        <div class="cta-section">
            <h3 class="cta-title">Siap Memulai Analisis?</h3>
            <p class="cta-subtitle">Mulai eksplorasi data film Anda sekarang juga!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Center button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("🚀 Mulai Analisis Film", type="primary", use_container_width=True):
            st.session_state["page"] = "Upload Dataset"
            st.rerun()