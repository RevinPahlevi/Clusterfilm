import streamlit as st
import pandas as pd

def show_upload_dataset():
    st.title("📂 Upload Dataset Film")
    
    st.markdown(
        """
        <div class="data-card">
            <p>Silakan unggah file <strong>CSV</strong> dataset film. 
            Pastikan dataset memiliki kolom numerik untuk <strong>Rating (vote_average)</strong> dan <strong>Popularitas (popularity)</strong>.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"])

    if uploaded_file is not None:
        try:
            # Gunakan engine python yang lebih fleksibel dan skip baris bermasalah
            df = pd.read_csv(uploaded_file, engine='python', on_bad_lines='warn')
            
            st.session_state["raw_df"] = df

            st.success("✅ Dataset berhasil diupload!")
            
            # Tampilkan metrik data
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Judul Film", f"{df.shape[0]:,}")
            with col2:
                st.metric("Jumlah Kolom", f"{df.shape[1]}")
            with col3:
                # Cek kolom penting
                has_rating = 'vote_average' in df.columns
                has_pop = 'popularity' in df.columns
                status = "Lengkap" if has_rating and has_pop else "Tidak Lengkap"
                st.metric("Status Kolom", status)

            st.markdown("### 🔍 Preview Data")
            st.dataframe(df.head(), use_container_width=True)
            
            # Warning jika kolom tidak ditemukan
            if not (has_rating and has_pop):
                st.warning("⚠️ Perhatian: Kolom 'vote_average' atau 'popularity' tidak ditemukan. Pastikan nama kolom sesuai agar proses clustering berjalan lancar.")

            # Tombol Next
            st.markdown("---")
            col_spacer, col_next = st.columns([8, 2])
            with col_next:
                if st.button("Next: Preprocessing >"):
                    st.session_state["page"] = "Preprocessing"
                    st.rerun()
                
        except Exception as e:
            st.error(f"❌ Error saat membaca file: {e}")