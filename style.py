import streamlit as st

def add_custom_css():
    """
    Menyuntikkan (inject) CSS kustom ke dalam aplikasi Streamlit.
    Tema: Cinema / Movie Streaming (Merah & Gelap/Putih Bersih)
    """
    st.markdown(
        """
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Global Styles */
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Area utama konten */
        .main {
            background-color: #f8f9fa;
        }
        
        /* Styling untuk sidebar - Warna Merah Netflix/Cinema */
        [data-testid="stSidebar"] {
            background: #E50914; 
            padding-top: 0rem;
        }
        
        /* Semua teks di sidebar putih */
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        /* Custom Menu Container */
        .custom-menu {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            padding: 1rem;
        }
        
        /* Styling button menu sidebar */
        [data-testid="stSidebar"] .stButton > button {
            background-color: transparent !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            text-align: left !important;
            width: 100% !important;
            font-weight: 500 !important;
            transition: all 0.2s ease !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background-color: rgba(0, 0, 0, 0.2) !important;
            padding-left: 1.5rem !important;
        }
        
        /* Active state menu */
        [data-testid="stSidebar"] button[kind="primary"] {
            background-color: rgba(0, 0, 0, 0.3) !important;
            font-weight: 700 !important;
            border-left: 4px solid white !important;
        }
        
        /* Card sambutan (Home) */
        .welcome-card {
            background: white;
            padding: 2.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-left: 5px solid #E50914; /* Aksen Merah */
            margin-bottom: 2rem;
        }
        
        .welcome-title {
            font-size: 1.8rem;
            font-weight: 700;
            color: #222;
            margin-bottom: 1rem;
        }
        
        /* Card informasi dataset (Home) */
        .info-card {
            background: #221f1f; /* Hitam bioskop */
            color: white;
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }
        
        .info-card h4 {
            color: #E50914 !important;
            font-weight: 700;
        }

        .info-card li {
            border-bottom: 1px solid rgba(255,255,255,0.1);
            padding: 0.5rem 0;
        }
        
        /* Tombol Utama (Merah) */
        .stButton > button {
            background: #E50914;
            color: white;
            border-radius: 8px;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background: #b20710; /* Merah lebih gelap saat hover */
            transform: scale(1.02);
        }

        /* Tombol Navigasi Previous (Abu-abu) */
        .nav-button-prev {
            background: #564d4d !important;
        }
        
        /* Data Card (General) */
        .data-card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
            border: 1px solid #eee;
        }
        
        /* Metric Styling */
        [data-testid="stMetricValue"] {
            color: #E50914;
            font-weight: 700;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )