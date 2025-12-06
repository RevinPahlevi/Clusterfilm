import streamlit as st

def show_about():
    st.title("ℹ Tentang Aplikasi")

    st.markdown(
        """
        <div class="welcome-card">
            <h3>🎬 Sistem Clustering Film Berdasarkan Rating & Popularitas</h3>
            <p style="color: #555;">
                Aplikasi ini dikembangkan untuk membantu memahami pola industri film menggunakan teknik <strong>Unsupervised Learning</strong>.
                Dengan mengelompokkan film ke dalam cluster, kita dapat membedakan film <em>"Blockbuster"</em>, <em>"Hidden Gems"</em>, atau film <em>"Niche"</em> secara otomatis.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    # KOLOM KIRI: TIM
    with col1:
        st.markdown("### 👥 Tim Pengembang")
        st.markdown(
            """
            <div class="data-card">
                <ul style="list-style: none; padding: 0; line-height: 2;">
                    <li>👤 <strong>Anggota 1</strong> — [NIM]</li>
                    <li>👤 <strong>Anggota 2</strong> — [NIM]</li>
                    <li>👤 <strong>Anggota 3</strong> — [NIM]</li>
                </ul>
                <p style="font-size: 0.9rem; color: #777; margin-top: 1rem;">
                    *Proyek ini disusun untuk Mata Kuliah Data Mining / Machine Learning.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # KOLOM KANAN: TEKNOLOGI
    with col2:
        st.markdown("### 🛠️ Teknologi")
        st.markdown(
            """
            <div class="data-card">
                <ul style="line-height: 2;">
                    <li>🐍 <strong>Python</strong> (Core Logic)</li>
                    <li>🎨 <strong>Streamlit</strong> (User Interface)</li>
                    <li>🤖 <strong>Scikit-Learn</strong> (K-Means Algorithm)</li>
                    <li>📊 <strong>Matplotlib & Seaborn</strong> (Visualisasi Data)</li>
                    <li>🐼 <strong>Pandas</strong> (Data Manipulation)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    st.markdown("---")
    st.caption("© 2025 Movie Clustering System. Developed with Streamlit.")