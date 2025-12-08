import streamlit as st

def show_about():
    # ===== HEADER SECTION =====
    st.markdown("""
        <div class="about-header">
            <div class="about-icon">📽️</div>
            <h1 class="about-title">Movie Clustering System</h1>
            <p class="about-subtitle">Sistem Pengelompokan Film Berbasis Machine Learning</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== APP DESCRIPTION =====
    st.markdown("""
        <div class="about-desc-card">
            <div class="adc-header">
                <span class="adc-icon">🎬</span>
                <span class="adc-title">Tentang Aplikasi</span>
            </div>
            <p class="adc-text">
                Aplikasi ini dikembangkan untuk membantu memahami pola industri film menggunakan 
                teknik <strong>Unsupervised Learning</strong> dengan algoritma <strong>K-Means Clustering</strong>.
                Dengan mengelompokkan film ke dalam cluster, kita dapat membedakan film 
                <em>"Blockbuster"</em>, <em>"Hidden Gems"</em>, atau film <em>"Average"</em> secara otomatis
                berdasarkan rating dan popularitas.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== TEAM SECTION =====
    st.markdown("""
        <div class="team-header">
            <span class="team-h-icon">👥</span>
            <span class="team-h-title">Tim Pengembang</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Team members data
    team_members = [
        {"name": "Nayla Nurul Afifah", "nim": "2311522002", "icon": "👩‍💻", "color": "pink"},
        {"name": "Revin Pahlevi", "nim": "2311522024", "icon": "👨‍💻", "color": "blue"},
        {"name": "Ahmad Iqbal Ramadhan", "nim": "2311523018", "icon": "👨‍💻", "color": "green"},
    ]
    
    cols = st.columns(3)
    
    for idx, member in enumerate(team_members):
        with cols[idx]:
            st.markdown(f"""
                <div class="team-card {member['color']}">
                    <div class="team-avatar">{member['icon']}</div>
                    <div class="team-name">{member['name']}</div>
                    <div class="team-nim">{member['nim']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    # ===== PROJECT INFO =====
    st.markdown("""
        <div class="project-info">
            <span class="pi-icon">📚</span>
            <span class="pi-text">Proyek ini disusun untuk Tugas Besar Mata Kuliah <strong>Akuisisi Data</strong></span>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== TECHNOLOGY STACK =====
    st.markdown("""
        <div class="tech-header">
            <span class="tech-h-icon">🛠️</span>
            <span class="tech-h-title">Teknologi yang Digunakan</span>
        </div>
    """, unsafe_allow_html=True)
    
    tech_stack = [
        {"name": "Python", "icon": "🐍", "desc": "Core Logic"},
        {"name": "Streamlit", "icon": "🎨", "desc": "User Interface"},
        {"name": "Scikit-Learn", "icon": "🤖", "desc": "K-Means Algorithm"},
        {"name": "Matplotlib", "icon": "📊", "desc": "Visualization"},
        {"name": "Pandas", "icon": "🐼", "desc": "Data Processing"},
        {"name": "ReportLab", "icon": "📄", "desc": "PDF Generation"},
    ]
    
    tech_cols = st.columns(6)
    
    for idx, tech in enumerate(tech_stack):
        with tech_cols[idx]:
            st.markdown(f"""
                <div class="tech-card">
                    <div class="tech-icon">{tech['icon']}</div>
                    <div class="tech-name">{tech['name']}</div>
                    <div class="tech-desc">{tech['desc']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    # ===== FEATURES =====
    st.markdown("""
        <div class="features-header">
            <span class="feat-h-icon">✨</span>
            <span class="feat-h-title">Fitur Utama</span>
        </div>
    """, unsafe_allow_html=True)
    
    feat_cols = st.columns(4)
    
    features = [
        {"icon": "📤", "title": "Upload Dataset", "desc": "Upload data CSV"},
        {"icon": "🔄", "title": "Preprocessing", "desc": "Normalisasi data"},
        {"icon": "📊", "title": "Clustering", "desc": "K-Means Analysis"},
        {"icon": "📥", "title": "Export PDF", "desc": "Laporan lengkap"},
    ]
    
    for idx, feat in enumerate(features):
        with feat_cols[idx]:
            st.markdown(f"""
                <div class="feature-card">
                    <div class="feat-icon">{feat['icon']}</div>
                    <div class="feat-title">{feat['title']}</div>
                    <div class="feat-desc">{feat['desc']}</div>
                </div>
            """, unsafe_allow_html=True)
    
    # ===== FOOTER =====
    st.markdown("""
        <div class="about-footer">
            <p>© 2025 Movie Clustering System</p>
        </div>
    """, unsafe_allow_html=True)