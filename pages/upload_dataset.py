import streamlit as st
import pandas as pd

def show_upload_dataset():
    # Header Section
    st.markdown("""
        <div class="upload-header">
            <h1 class="upload-title">📂 Upload Dataset Film</h1>
            <p class="upload-subtitle">Unggah file CSV dataset film untuk memulai analisis clustering</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Cek apakah dataset sudah ada di session state
    if st.session_state.get("raw_df") is not None:
        df = st.session_state["raw_df"]
        
        # Success message dengan styling custom
        st.markdown("""
            <div class="success-banner">
                <span class="success-icon">✓</span>
                <span class="success-text">Dataset sudah terupload dan siap digunakan!</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Stats Cards
        col1, col2, col3 = st.columns(3)
        
        # Cek kolom penting
        has_rating = 'vote_average' in df.columns
        has_pop = 'popularity' in df.columns
        status = "Lengkap ✓" if has_rating and has_pop else "Tidak Lengkap ⚠"
        status_class = "complete" if has_rating and has_pop else "incomplete"
        
        with col1:
            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-icon">🎬</div>
                    <div class="stat-content">
                        <div class="stat-label">Total Film</div>
                        <div class="stat-value">{df.shape[0]:,}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-icon">📊</div>
                    <div class="stat-content">
                        <div class="stat-label">Jumlah Kolom</div>
                        <div class="stat-value">{df.shape[1]}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
                <div class="stat-card {status_class}">
                    <div class="stat-icon">{'✓' if has_rating and has_pop else '⚠'}</div>
                    <div class="stat-content">
                        <div class="stat-label">Status Kolom</div>
                        <div class="stat-value">{status}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Data Preview Section
        st.markdown("""
            <div class="section-header">
                <span class="section-icon">🔍</span>
                <span class="section-title">Preview Data</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.dataframe(df.head(), use_container_width=True)
        
        # Warning jika kolom tidak ditemukan
        if not (has_rating and has_pop):
            st.markdown("""
                <div class="warning-banner">
                    <span class="warning-icon">⚠</span>
                    <span class="warning-text">Perhatian: Kolom 'vote_average' atau 'popularity' tidak ditemukan. Pastikan nama kolom sesuai.</span>
                </div>
            """, unsafe_allow_html=True)
        
        # Action Buttons
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        
        col_btn1, col_btn2, col_spacer, col_next = st.columns([2, 2, 4, 2])
        
        with col_btn1:
            if st.button("🔄 Ganti Dataset", use_container_width=True, type="secondary"):
                st.session_state["show_uploader"] = True
                st.rerun()
        
        with col_btn2:
            if st.button("🗑️ Hapus Dataset", use_container_width=True, type="secondary"):
                # Clear semua data terkait
                st.session_state["raw_df"] = None
                st.session_state["clean_df"] = None
                st.session_state["scaled_df"] = None
                st.session_state["kmeans_model"] = None
                st.session_state["scaler"] = None
                st.session_state["cluster_labels"] = None
                st.rerun()
        
        with col_next:
            if st.button("Next: Preprocessing ›", use_container_width=True, type="primary"):
                st.session_state["page"] = "Preprocessing"
                st.rerun()
    
    # Tampilkan file uploader jika dataset belum ada atau user mau ganti
    if st.session_state.get("raw_df") is None or st.session_state.get("show_uploader", False):
        if st.session_state.get("show_uploader", False):
            st.markdown("""
                <div class="upload-change-header">
                    <span class="upload-change-icon">📤</span>
                    <span class="upload-change-text">Upload Dataset Baru</span>
                </div>
            """, unsafe_allow_html=True)
        
        # File uploader langsung tanpa custom zone
        uploaded_file = st.file_uploader(
            "Drag and drop file here", 
            type=["csv"], 
            help="Pastikan file memiliki kolom 'vote_average' dan 'popularity'",
            key="dataset_uploader"
        )

        if uploaded_file is not None:
            try:
                # Gunakan engine python yang lebih fleksibel dan skip baris bermasalah
                df = pd.read_csv(uploaded_file, engine='python', on_bad_lines='warn')
                
                st.session_state["raw_df"] = df
                st.session_state["show_uploader"] = False  # Reset flag

                st.markdown("""
                    <div class="success-banner">
                        <span class="success-icon">✓</span>
                        <span class="success-text">Dataset berhasil diupload!</span>
                    </div>
                """, unsafe_allow_html=True)
                st.rerun()  # Refresh untuk menampilkan data baru
                
            except Exception as e:
                st.markdown(f"""
                    <div class="error-banner">
                        <span class="error-icon">✕</span>
                        <span class="error-text">Error saat membaca file: {e}</span>
                    </div>
                """, unsafe_allow_html=True)
