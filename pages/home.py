import streamlit as st

def show_home():
    # Judul utama
    st.markdown("<h1 style='text-align: center;'>🎬 Movie Clustering System</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    # KONTEN KIRI: Penjelasan & Alur
    with col1:
        st.markdown(
            """
            <div class="welcome-card">
                <div class="welcome-title">Temukan Pola Tersembunyi dalam Data Film!</div>
                <p style="color: #555; line-height: 1.6;">
                    Sistem ini menggunakan <strong>Machine Learning (K-Means Clustering)</strong> untuk mengelompokkan ribuan film 
                    berdasarkan dua indikator utama: <strong>Rating (Kualitas)</strong> dan <strong>Popularitas (Tren)</strong>.
                </p>
                <p style="color: #555; line-height: 1.6;">
                    <strong>Alur Penggunaan Aplikasi:</strong>
                </p>
                <ol style="line-height: 1.8; color: #333;">
                    <li>📂 <strong>Upload Dataset</strong> - Unggah data film (CSV) dengan kolom rating & popularitas.</li>
                    <li>🛠️ <strong>Preprocessing</strong> - Normalisasi data agar siap diproses mesin.</li>
                    <li>🕵️ <strong>Clustering Process</strong> - Tentukan jumlah cluster (kelompok) dan jalankan K-Means.</li>
                    <li>📊 <strong>Visualization</strong> - Lihat grafik penyebaran cluster film.</li>
                    <li>🔍 <strong>Rekomendasi</strong> - Cari tahu kategori film baru & temukan film serupa.</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Tombol Mulai
        if st.button("🚀 Mulai Analisis Film", use_container_width=False):
            st.session_state["page"] = "Upload Dataset"
            st.rerun()
    
    # KONTEN KANAN: Info Dataset
    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h4>📊 Spesifikasi Data</h4>
                <ul style="list-style: none; padding: 0;">
                    <li>🎬 <strong>Topik:</strong> Clustering Film</li>
                    <li>🔢 <strong>Algoritma:</strong> K-Means</li>
                    <li>🎯 <strong>Tujuan:</strong> Segmentasi Film</li>
                    <li>📈 <strong>Fitur Utama:</strong>
                        <ul>
                            <li>Vote Average (Rating)</li>
                            <li>Popularity (Jumlah View/Interaksi)</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )