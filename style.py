import streamlit as st

def add_custom_css():
    """
    Menyuntikkan (inject) CSS kustom ke dalam aplikasi Streamlit.
    Tema: Film Clustering - Cream & Navy Modern
    """
    st.markdown(
        """
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
        
        /* ===== COLOR PALETTE =====
           Primary Background: #FAF0CA (Cream)
           Sidebar: #0D3B66 (Navy)
           Accent 1: #F4D35E (Golden Yellow)
           Accent 2: #EE964B (Orange)
           Accent 3: #F95738 (Coral Red)
           Text Dark: #1a1a2e
           Text Light: #ffffff
        ========================== */
        
        /* Global Styles */
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Root Variables */
        :root {
            --bg-cream: #FAF0CA;
            --sidebar-navy: #0D3B66;
            --accent-gold: #F4D35E;
            --accent-orange: #EE964B;
            --accent-coral: #F95738;
            --text-dark: #1a1a2e;
            --text-light: #ffffff;
            --card-white: #ffffff;
            --shadow-soft: 0 8px 32px rgba(13, 59, 102, 0.12);
            --shadow-hover: 0 12px 40px rgba(13, 59, 102, 0.2);
        }
        
        /* Area utama konten */
        .main {
            background: linear-gradient(135deg, #FAF0CA 0%, #f5e6b8 50%, #FAF0CA 100%);
            background-attachment: fixed;
        }
        
        .stApp {
            background: linear-gradient(135deg, #FAF0CA 0%, #f5e6b8 50%, #FAF0CA 100%);
        }
        
        /* Sembunyikan multipage navigation bawaan Streamlit */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        
        /* Sembunyikan navigation pages list */
        [data-testid="stSidebarNavItems"] {
            display: none !important;
        }
        
        /* Sembunyikan section pages dari sidebar */
        section[data-testid="stSidebar"] > div > div:first-child > div:first-child {
            display: none !important;
        }
        
        /* ===== SIDEBAR STYLING ===== */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0D3B66 0%, #0a2d4d 100%);
            padding-top: 0rem;
            box-shadow: 4px 0 20px rgba(13, 59, 102, 0.3);
        }
        
        [data-testid="stSidebar"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            pointer-events: none;
        }
        
        /* Semua teks di sidebar putih */
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        /* Sidebar Title */
        [data-testid="stSidebar"] .stMarkdown h1,
        [data-testid="stSidebar"] .stMarkdown h2,
        [data-testid="stSidebar"] .stMarkdown h3 {
            color: #F4D35E !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Styling button menu sidebar */
        [data-testid="stSidebar"] .stButton > button {
            background: rgba(255, 255, 255, 0.08) !important;
            backdrop-filter: blur(10px);
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px !important;
            text-align: left !important;
            width: 100% !important;
            font-weight: 500 !important;
            padding: 0.75rem 1rem !important;
            margin-bottom: 0.3rem !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            position: relative;
            overflow: hidden;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(244, 211, 94, 0.2) !important;
            border-color: #F4D35E !important;
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(244, 211, 94, 0.3) !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:active {
            transform: translateX(5px) scale(0.98);
        }
        
        /* ===== CARD STYLES ===== */
        /* Card sambutan (Home) */
        .welcome-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(13, 59, 102, 0.15);
            border-left: 5px solid #0D3B66;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        
        .welcome-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(13, 59, 102, 0.2);
        }
        
        .welcome-card::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, rgba(244, 211, 94, 0.1) 0%, transparent 70%);
            pointer-events: none;
        }
        
        .welcome-title {
            font-size: 2rem;
            font-weight: 700;
            color: #0D3B66;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #0D3B66 0%, #1a5490 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Card informasi dataset (Home) */
        .info-card {
            background: linear-gradient(135deg, #0D3B66 0%, #0a2d4d 100%);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(13, 59, 102, 0.3);
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        
        .info-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 40px rgba(13, 59, 102, 0.4);
        }
        
        .info-card::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 150px;
            height: 150px;
            background: radial-gradient(circle, rgba(244, 211, 94, 0.2) 0%, transparent 70%);
            pointer-events: none;
        }
        
        .info-card h4 {
            color: #F4D35E !important;
            font-weight: 700;
        }

        .info-card li {
            border-bottom: 1px solid rgba(255,255,255,0.15);
            padding: 0.6rem 0;
            transition: all 0.2s ease;
        }
        
        .info-card li:hover {
            padding-left: 0.5rem;
            border-color: #F4D35E;
        }
        
        /* ===== BUTTON STYLES ===== */
        .stButton > button {
            background: linear-gradient(135deg, #0D3B66 0%, #1a5490 100%);
            color: white;
            border-radius: 12px;
            font-weight: 600;
            border: none;
            padding: 0.6rem 1.5rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px rgba(13, 59, 102, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s ease;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #1a5490 0%, #0D3B66 100%);
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(13, 59, 102, 0.4);
        }
        
        .stButton > button:hover::before {
            left: 100%;
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }

        /* Secondary Button Style */
        .nav-button-prev {
            background: linear-gradient(135deg, #6c757d 0%, #495057 100%) !important;
        }
        
        /* ===== DATA CARD ===== */
        .data-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 1.8rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(13, 59, 102, 0.1);
            margin-bottom: 1.5rem;
            border: 1px solid rgba(13, 59, 102, 0.08);
            transition: all 0.3s ease;
        }
        
        .data-card:hover {
            box-shadow: 0 8px 30px rgba(13, 59, 102, 0.15);
            border-color: rgba(244, 211, 94, 0.3);
        }
        
        /* ===== METRIC STYLING ===== */
        [data-testid="stMetricValue"] {
            color: #0D3B66;
            font-weight: 700;
            font-size: 1.8rem !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: #495057 !important;
            font-weight: 500;
        }
        
        /* ===== EXPANDER STYLING ===== */
        .streamlit-expanderHeader {
            background: rgba(13, 59, 102, 0.05);
            border-radius: 12px;
            font-weight: 600;
            color: #0D3B66;
        }
        
        .streamlit-expanderHeader:hover {
            background: rgba(13, 59, 102, 0.1);
        }
        
        /* ===== SELECTBOX & INPUT STYLING ===== */
        .stSelectbox > div > div,
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            border-radius: 10px !important;
            border: 2px solid rgba(13, 59, 102, 0.15) !important;
            transition: all 0.3s ease !important;
        }
        
        .stSelectbox > div > div:focus-within,
        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #0D3B66 !important;
            box-shadow: 0 0 0 3px rgba(13, 59, 102, 0.1) !important;
        }
        
        /* ===== DATAFRAME STYLING ===== */
        .stDataFrame {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(13, 59, 102, 0.1);
        }
        
        /* ===== TAB STYLING ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: rgba(13, 59, 102, 0.05);
            padding: 0.5rem;
            border-radius: 12px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 10px;
            font-weight: 500;
            color: #0D3B66;
            padding: 0.5rem 1.5rem;
        }
        
        .stTabs [aria-selected="true"] {
            background: #0D3B66 !important;
            color: white !important;
        }
        
        /* ===== PROGRESS BAR ===== */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #0D3B66 0%, #F4D35E 100%);
        }
        
        /* ===== ALERT/INFO BOXES ===== */
        .stAlert {
            border-radius: 12px;
            border: none;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }
        
        /* ===== MARKDOWN HEADERS ===== */
        .main h1 {
            color: #0D3B66 !important;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
        
        .main h2 {
            color: #0D3B66 !important;
            font-weight: 600;
            border-bottom: 3px solid #F4D35E;
            padding-bottom: 0.5rem;
            display: inline-block;
        }
        
        .main h3 {
            color: #1a5490 !important;
            font-weight: 600;
        }
        
        /* ===== DIVIDER ===== */
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #0D3B66, transparent);
            margin: 2rem 0;
        }
        
        /* ===== FILE UPLOADER ===== */
        [data-testid="stFileUploader"] {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 16px;
            padding: 1.5rem;
            border: 2px dashed rgba(13, 59, 102, 0.3);
            transition: all 0.3s ease;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #0D3B66;
            background: rgba(255, 255, 255, 1);
        }
        
        /* ===== SCROLLBAR ===== */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #FAF0CA;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #0D3B66 0%, #1a5490 100%);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #0D3B66;
        }
        
        /* ===== ANIMATION KEYFRAMES ===== */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .main .block-container {
            animation: fadeInUp 0.5s ease-out;
        }
        
        /* ===== TOOLTIP ===== */
        [data-testid="stTooltipIcon"] {
            color: #0D3B66;
        }
        
        </style>
        """,
        unsafe_allow_html=True,
    )