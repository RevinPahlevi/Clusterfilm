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
        
        
        /* Area utama konten - Gradasi Diagonal: Biru (Kiri Atas) → Cream (Kanan Bawah) */
        .main {
            background: linear-gradient(135deg, 
                #0D3B66 0%, 
                #1a4d7a 10%,
                #2d5f8d 20%,
                #5a87ad 35%,
                #8aacc8 50%,
                #b8c8d9 65%,
                #d4dde8 80%,
                #e8eef3 90%,
                #FAF0CA 100%
            );
            background-attachment: fixed;
            min-height: 100vh;
            position: relative;
        }
        
        .main::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 10% 10%, rgba(13, 59, 102, 0.15) 0%, transparent 30%),
                radial-gradient(circle at 90% 90%, rgba(250, 240, 202, 0.2) 0%, transparent 40%);
            pointer-events: none;
            z-index: 0;
        }
        
        .stApp {
            background: linear-gradient(135deg, 
                #0D3B66 0%, 
                #1a4d7a 10%,
                #2d5f8d 20%,
                #5a87ad 35%,
                #8aacc8 50%,
                #b8c8d9 65%,
                #d4dde8 80%,
                #e8eef3 90%,
                #FAF0CA 100%
            );
            background-attachment: fixed;
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
            background: linear-gradient(180deg, #0D3B66 0%, #0a2d4d 50%, #08253d 100%);
            padding-top: 1rem;
            box-shadow: 4px 0 30px rgba(13, 59, 102, 0.4);
            position: relative;
        }
        
        /* Subtle pattern overlay */
        [data-testid="stSidebar"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 50%, rgba(244, 211, 94, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(244, 211, 94, 0.03) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }
        
        /* Logo container - rata tengah */
        [data-testid="stSidebar"] [data-testid="stImage"] {
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            margin-bottom: 0.5rem;
        }
        
        /* Logo styling - ukuran kecil, posisi tengah */
        [data-testid="stSidebar"] img {
            display: inline-block !important;
            width: 100px !important;
            height: auto !important;
            margin: 0 !important;
            padding: 0.5rem !important;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }
        
        [data-testid="stSidebar"] img:hover {
            transform: scale(1.08);
            box-shadow: 0 8px 25px rgba(244, 211, 94, 0.3);
            background: rgba(255, 255, 255, 0.12);
        }
        
        /* Semua teks di sidebar putih */
        [data-testid="stSidebar"] * {
            color: white !important;
            position: relative;
            z-index: 1;
        }
        
        /* Sidebar Title - removed, keeping styles for other h tags */
        
        [data-testid="stSidebar"] .stMarkdown h2,
        [data-testid="stSidebar"] .stMarkdown h3 {
            color: #F4D35E !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Sidebar separator/divider */
        [data-testid="stSidebar"] hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(244, 211, 94, 0.4), transparent);
            margin: 1rem 0 1.5rem 0;
        }
        
        /* Styling button menu sidebar - compact */
        [data-testid="stSidebar"] .stButton > button {
            background: rgba(255, 255, 255, 0.06) !important;
            backdrop-filter: blur(10px);
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 12px !important;
            text-align: left !important;
            width: 100% !important;
            font-weight: 500 !important;
            font-size: 0.85rem !important;
            padding: 0.65rem 0.9rem !important;
            margin-bottom: 0.4rem !important;
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1) !important;
            position: relative;
            overflow: hidden;
            letter-spacing: 0.2px;
        }
        
        /* Subtle shine effect on button */
        [data-testid="stSidebar"] .stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.6s ease;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: linear-gradient(135deg, rgba(244, 211, 94, 0.15) 0%, rgba(244, 211, 94, 0.25) 100%) !important;
            border-color: rgba(244, 211, 94, 0.5) !important;
            transform: translateX(6px) scale(1.01);
            box-shadow: 
                -2px 0 0 0 #F4D35E,
                0 6px 20px rgba(244, 211, 94, 0.25) !important;
            color: #F4D35E !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover::before {
            left: 100%;
        }
        
        [data-testid="stSidebar"] .stButton > button:active {
            transform: translateX(6px) scale(0.98);
            transition: all 0.1s ease;
        }
        
        /* ===== ACTIVE/PRIMARY BUTTON (Current Page) ===== */
        [data-testid="stSidebar"] .stButton > button[kind="primary"],
        [data-testid="stSidebar"] .stButton > button[data-baseweb="button"][kind="primary"] {
            background: linear-gradient(135deg, rgba(244, 211, 94, 0.25) 0%, rgba(244, 211, 94, 0.35) 100%) !important;
            border: 1px solid rgba(244, 211, 94, 0.6) !important;
            border-left: 4px solid #F4D35E !important;
            color: #F4D35E !important;
            font-weight: 600 !important;
            box-shadow: 
                0 4px 15px rgba(244, 211, 94, 0.2),
                inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        }
        
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
            background: linear-gradient(135deg, rgba(244, 211, 94, 0.3) 0%, rgba(244, 211, 94, 0.4) 100%) !important;
            border-color: rgba(244, 211, 94, 0.7) !important;
            box-shadow: 
                -4px 0 0 0 #F4D35E,
                0 6px 20px rgba(244, 211, 94, 0.3) !important;
        }
        
        
        /* ===== HOME PAGE STYLES - Minimalist Blue & Cream ===== */
        
        /* Hero Section */
        .hero-section {
            background: linear-gradient(135deg, #0D3B66 0%, #1a4d7a 50%, #0D3B66 100%);
            padding: 1.2rem 1rem;
            border-radius: 14px;
            text-align: center;
            margin-bottom: 0.8rem;
            position: relative;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(13, 59, 102, 0.25);
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 30%, rgba(250, 240, 202, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(244, 211, 94, 0.08) 0%, transparent 50%);
            pointer-events: none;
        }
        
        /* Hero Logo Inline */
        .hero-logo-inline {
            width: 50px;
            height: auto;
            vertical-align: text-bottom;
            margin-right: 0.5rem;
            margin-bottom: -2px;
            filter: drop-shadow(0 3px 8px rgba(0, 0, 0, 0.3));
            display: inline-block;
        }
        
        .hero-title {
            font-size: 1.8rem;
            font-weight: 800;
            color: #FAF0CA;
            margin-bottom: 0.5rem;
            text-shadow: 0 3px 12px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 1;
            text-align: center;
            display: inline-block;
            width: 100%;
        }
        
        .hero-subtitle {
            font-size: 0.88rem;
            color: rgba(250, 240, 202, 0.9);
            font-weight: 400;
            max-width: 550px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
            line-height: 1.3;
            text-align: center;
        }
        
        /* Intro Section */
        .intro-section {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.85) 0%, rgba(250, 240, 202, 0.75) 100%);
            border-left: 3px solid #F4D35E;
            padding: 0.7rem 1.2rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            backdrop-filter: blur(10px);
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.1);
        }
        
        .intro-text {
            font-size: 0.88rem;
            color: #1a1a2e;
            font-weight: 500;
            line-height: 1.5;
            margin: 0;
            text-align: center;
        }
        
        /* Feature Cards - 3 Column */
        .feature-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.88) 100%);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(13, 59, 102, 0.15);
            border-radius: 14px;
            padding: 0.9rem 0.7rem;
            text-align: center;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            box-shadow: 0 5px 18px rgba(0, 0, 0, 0.12);
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, #0D3B66 0%, #F4D35E 100%);
            transform: scaleX(0);
            transition: transform 0.4s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 28px rgba(0, 0, 0, 0.18);
            border-color: rgba(244, 211, 94, 0.4);
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 255, 255, 0.92) 100%);
        }
        
        .feature-card:hover::before {
            transform: scaleX(1);
        }
        
        .feature-icon {
            font-size: 2.3rem;
            margin-bottom: 0.5rem;
            filter: drop-shadow(0 2px 5px rgba(13, 59, 102, 0.3));
        }
        
        .feature-title {
            font-size: 1.15rem !important;
            font-weight: 900 !important;
            color: #0a2540 !important;
            margin-bottom: 0.5rem !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.15) !important;
            letter-spacing: 0.3px !important;
            background: linear-gradient(135deg, rgba(13, 59, 102, 0.08) 0%, rgba(244, 211, 94, 0.08) 100%);
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
            display: inline-block;
            text-align: center !important;
        }
        
        .feature-desc {
            font-size: 0.8rem;
            color: #2d3748;
            font-weight: 500;
            line-height: 1.4;
            margin: 0;
            text-align: center !important;
        }
        
        /* How it Works Section */
        .how-it-works {
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .section-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #0D3B66;
            margin-bottom: 1rem;
            position: relative;
            display: inline-block;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 50%;
            transform: translateX(-50%);
            width: 60%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #F4D35E, transparent);
            border-radius: 2px;
        }
        
        /* Step Cards */
        .step-card {
            display: flex;
            gap: 0.7rem;
            align-items: flex-start;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.88) 100%);
            border: 2px solid rgba(13, 59, 102, 0.12);
            border-radius: 12px;
            padding: 0.7rem 0.9rem;
            margin-bottom: 0.5rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.1);
        }
        
        .step-card::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(180deg, #0D3B66 0%, #F4D35E 100%);
            transform: scaleY(0);
            transition: transform 0.3s ease;
        }
        
        .step-card:hover {
            transform: translateX(5px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
            border-color: rgba(244, 211, 94, 0.4);
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 255, 255, 0.92) 100%);
        }
        .step-content {
            flex: 1;
        }
        
        .step-title {
            font-size: 1.05rem !important;
            font-weight: 900 !important;
            color: #0a2540 !important;
            margin: 0 0 0.3rem 0 !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.15) !important;
            letter-spacing: 0.3px !important;
            background: linear-gradient(135deg, rgba(13, 59, 102, 0.08) 0%, rgba(244, 211, 94, 0.08) 100%);
            padding: 0.2rem 0.5rem;
            border-radius: 5px;
            display: inline-block;
            text-align: center !important;
        }
        
        .step-desc {
            font-size: 0.78rem;
            color: #2d3748;
            font-weight: 500;
            line-height: 1.4;
            margin: 0;
            text-align: center !important;
        }
        
        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(250, 240, 202, 0.8) 100%);
            border: 2px dashed rgba(13, 59, 102, 0.3);
            border-radius: 14px;
            padding: 1.3rem 1.2rem;
            text-align: center;
            margin-bottom: 0.8rem;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.1);
        }
        
        .cta-title {
            font-size: 1.5rem !important;
            font-weight: 900 !important;
            color: #0a2540 !important;
            margin-bottom: 0.5rem !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.15) !important;
            letter-spacing: 0.3px !important;
        }
        
        .cta-subtitle {
            font-size: 0.9rem !important;
            color: #1a1a2e !important;
            font-weight: 600 !important;
            margin: 0 !important;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* ===== UPLOAD DATASET PAGE STYLES ===== */
        
        /* Upload Header */
        .upload-header {
            text-align: center;
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(250, 240, 202, 0.7) 100%);
            border-radius: 16px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }
        
        .upload-title {
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #0D3B66 0%, #1a5490 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 0 0 0.5rem 0;
        }
        
        .upload-subtitle {
            font-size: 1rem;
            color: #495057;
            font-weight: 500;
            margin: 0;
        }
        
        /* Upload Zone */
        .upload-zone {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(250, 240, 202, 0.85) 100%);
            border: 3px dashed rgba(13, 59, 102, 0.3);
            border-radius: 20px;
            padding: 3rem 2rem;
            text-align: center;
            transition: all 0.4s ease;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }
        
        .upload-zone::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 50% 50%, rgba(244, 211, 94, 0.1) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }
        
        .upload-zone:hover {
            border-color: #0D3B66;
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(250, 240, 202, 0.95) 100%);
            box-shadow: 0 8px 30px rgba(13, 59, 102, 0.15);
        }
        
        .upload-zone:hover::before {
            opacity: 1;
        }
        
        /* Compact Upload Zone */
        .upload-zone-compact {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(250, 240, 202, 0.85) 100%);
            border: 3px dashed rgba(13, 59, 102, 0.3);
            border-radius: 16px;
            padding: 1.8rem 1.5rem;
            text-align: center;
            transition: all 0.4s ease;
            margin-bottom: 1rem;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        
        .upload-zone-compact::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 50% 50%, rgba(244, 211, 94, 0.1) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }
        
        .upload-zone-compact:hover {
            border-color: #0D3B66;
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(250, 240, 202, 0.95) 100%);
            box-shadow: 0 6px 20px rgba(13, 59, 102, 0.15);
        }
        
        .upload-zone-compact:hover::before {
            opacity: 1;
        }
        
        .upload-icon-large {
            font-size: 4rem;
            margin-bottom: 1rem;
            animation: floatUpDown 3s ease-in-out infinite;
        }
        
        .upload-icon-medium {
            font-size: 2.8rem;
            margin-bottom: 0.7rem;
            animation: floatUpDown 3s ease-in-out infinite;
        }
        
        @keyframes floatUpDown {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        
        .upload-text-primary {
            font-size: 1.3rem;
            font-weight: 700;
            color: #0D3B66;
            margin-bottom: 0.5rem;
        }
        
        .upload-text-main {
            font-size: 1.1rem;
            font-weight: 700;
            color: #0D3B66;
            margin-bottom: 0.4rem;
        }
        
        .upload-text-secondary {
            font-size: 1rem;
            color: #6c757d;
            margin-bottom: 1rem;
        }
        
        .upload-text-sub {
            font-size: 0.9rem;
            color: #6c757d;
            margin-bottom: 0.7rem;
        }
        
        .upload-hint {
            font-size: 0.85rem;
            color: #F4D35E;
            font-weight: 600;
            background: rgba(13, 59, 102, 0.08);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            display: inline-block;
            margin-top: 0.5rem;
        }
        
        .upload-hint-compact {
            font-size: 0.75rem;
            color: #F4D35E;
            font-weight: 600;
            background: rgba(13, 59, 102, 0.08);
            padding: 0.4rem 0.8rem;
            border-radius: 15px;
            display: inline-block;
            margin-top: 0.4rem;
        }
        
        /* ===== CUSTOM FILE UPLOADER STYLING ===== */
        
        /* Main file uploader container */
        .main [data-testid="stFileUploader"] {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(250, 240, 202, 0.85) 100%) !important;
            border: 3px dashed rgba(13, 59, 102, 0.3) !important;
            border-radius: 16px !important;
            padding: 2rem 1.5rem !important;
            transition: all 0.4s ease !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08) !important;
        }
        
        .main [data-testid="stFileUploader"]:hover {
            border-color: #0D3B66 !important;
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(250, 240, 202, 0.95) 100%) !important;
            box-shadow: 0 6px 20px rgba(13, 59, 102, 0.15) !important;
        }
        
        /* File uploader section (drop zone) */
        .main [data-testid="stFileUploader"] section {
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
        }
        
        /* File uploader drag-drop area */
        .main [data-testid="stFileUploader"] section > div {
            background: linear-gradient(135deg, #0D3B66 0%, #1a5490 100%) !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 1.5rem 1.2rem !important;
            box-shadow: 0 4px 12px rgba(13, 59, 102, 0.25) !important;
            transition: all 0.3s ease !important;
        }
        
        .main [data-testid="stFileUploader"] section > div:hover {
            background: linear-gradient(135deg, #1a5490 0%, #0D3B66 100%) !important;
            box-shadow: 0 6px 18px rgba(13, 59, 102, 0.35) !important;
            transform: translateY(-2px) !important;
        }
        
        /* Text inside uploader */
        .main [data-testid="stFileUploader"] section > div > div {
            color: white !important;
        }
        
        .main [data-testid="stFileUploader"] section small {
            color: rgba(250, 240, 202, 0.9) !important;
            font-weight: 500 !important;
        }
        
        /* Browse files button */
        .main [data-testid="stFileUploader"] button {
            background: linear-gradient(135deg, #F4D35E 0%, #f0c93d 100%) !important;
            color: #0D3B66 !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            padding: 0.6rem 1.5rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 3px 10px rgba(244, 211, 94, 0.3) !important;
        }
        
        .main [data-testid="stFileUploader"] button:hover {
            background: linear-gradient(135deg, #f0c93d 0%, #F4D35E 100%) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 5px 15px rgba(244, 211, 94, 0.4) !important;
        }
        
        /* Uploaded file display */
        .main [data-testid="stFileUploader"] section + div {
            background: rgba(255, 255, 255, 0.9) !important;
            border: 2px solid rgba(13, 59, 102, 0.15) !important;
            border-radius: 10px !important;
            padding: 0.8rem 1rem !important;
            margin-top: 1rem !important;
        }
        
        
        /* Stats Cards */
        .stat-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.88) 100%);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(13, 59, 102, 0.12);
            border-radius: 16px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }
        
        .stat-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
            border-color: rgba(244, 211, 94, 0.4);
        }
        
        .stat-card.complete {
            border-left: 4px solid #28a745;
        }
        
        .stat-card.incomplete {
            border-left: 4px solid #ffc107;
        }
        
        .stat-icon {
            font-size: 2.5rem;
            flex-shrink: 0;
        }
        
        .stat-content {
            flex: 1;
            text-align: left;
        }
        
        .stat-label {
            font-size: 0.85rem;
            color: #6c757d;
            font-weight: 500;
            margin-bottom: 0.3rem;
        }
        
        .stat-value {
            font-size: 1.8rem;
            font-weight: 800;
            color: #0D3B66;
            line-height: 1;
        }
        
        /* Section Header */
        .section-header {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin: 2rem 0 1rem 0;
            padding: 1rem 1.5rem;
            background: linear-gradient(135deg, #0D3B66 0%, #1a5490 100%);
            border-left: 5px solid #F4D35E;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(13, 59, 102, 0.25);
        }
        
        .section-icon {
            font-size: 1.5rem;
        }
        
        .section-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: white;
            margin: 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Override Streamlit Dataframe Styling */
        .main .stDataFrame {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(13, 59, 102, 0.15);
        }
        
        .main .stDataFrame > div {
            border-radius: 12px;
        }
        
        /* Dataframe headers */
        .main .stDataFrame th {
            background: linear-gradient(135deg, #0D3B66 0%, #1a5490 100%) !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 0.8rem !important;
            border-bottom: 2px solid #F4D35E !important;
        }
        
        /* Dataframe rows */
        .main .stDataFrame td {
            background: rgba(255, 255, 255, 0.95) !important;
            padding: 0.7rem !important;
            border-bottom: 1px solid rgba(13, 59, 102, 0.1) !important;
        }
        
        .main .stDataFrame tr:nth-child(even) td {
            background: rgba(250, 240, 202, 0.3) !important;
        }
        
        .main .stDataFrame tr:hover td {
            background: rgba(250, 240, 202, 0.5) !important;
        }
        
        /* Banner Notifications */
        .success-banner {
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            border: 2px solid #28a745;
            border-radius: 12px;
            padding: 1rem 1.5rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            box-shadow: 0 4px 15px rgba(40, 167, 69, 0.2);
        }
        
        .success-icon {
            font-size: 1.5rem;
            color: #28a745;
            font-weight: 800;
            background: white;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        
        .success-text {
            font-size: 1rem;
            color: #155724;
            font-weight: 600;
            flex: 1;
        }
        
        .warning-banner {
            background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
            border: 2px solid #ffc107;
            border-radius: 12px;
            padding: 1rem 1.5rem;
            margin-top: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            box-shadow: 0 4px 15px rgba(255, 193, 7, 0.2);
        }
        
        .warning-icon {
            font-size: 1.5rem;
            color: #ffc107;
            font-weight: 800;
            background: white;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        
        .warning-text {
            font-size: 0.95rem;
            color: #856404;
            font-weight: 600;
            flex: 1;
        }
        
        .error-banner {
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
            border: 2px solid #dc3545;
            border-radius: 12px;
            padding: 1rem 1.5rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            box-shadow: 0 4px 15px rgba(220, 53, 69, 0.2);
        }
        
        .error-icon {
            font-size: 1.5rem;
            color: #dc3545;
            font-weight: 800;
            background: white;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        
        .error-text {
            font-size: 0.95rem;
            color: #721c24;
            font-weight: 600;
            flex: 1;
        }
        
        /* Upload Change Header */
        .upload-change-header {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin: 1.5rem 0 1rem 0;
            padding: 0.8rem 1.2rem;
            background: linear-gradient(135deg, rgba(244, 211, 94, 0.15) 0%, rgba(13, 59, 102, 0.1) 100%);
            border-left: 4px solid #F4D35E;
            border-radius: 10px;
        }
        
        .upload-change-icon {
            font-size: 1.5rem;
        }
        
        .upload-change-text {
            font-size: 1.2rem;
            font-weight: 700;
            color: #0D3B66;
            margin: 0;
        }
        
        /* ===== PREMIUM BUTTON STYLES (Main Content Only) ===== */
        
        /* Primary Button - Golden Yellow Theme */
        .main .stButton > button[kind="primary"],
        .main .stButton > button[data-testid="baseButton-primary"] {
            background: linear-gradient(135deg, #F4D35E 0%, #f0c93d 50%, #eabb2d 100%) !important;
            color: #0D3B66 !important;
            border: 2px solid rgba(13, 59, 102, 0.2) !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            font-size: 1rem !important;
            padding: 0.75rem 1.8rem !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 
                0 4px 15px rgba(244, 211, 94, 0.4),
                0 2px 8px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.5) !important;
            position: relative !important;
            overflow: hidden !important;
            text-shadow: 0 1px 2px rgba(255, 255, 255, 0.3) !important;
        }
        
        .main .stButton > button[kind="primary"]::before,
        .main .stButton > button[data-testid="baseButton-primary"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s ease;
        }
        
        .main .stButton > button[kind="primary"]:hover,
        .main .stButton > button[data-testid="baseButton-primary"]:hover {
            background: linear-gradient(135deg, #eabb2d 0%, #f0c93d 50%, #F4D35E 100%) !important;
            border-color: rgba(13, 59, 102, 0.4) !important;
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 
                0 8px 25px rgba(244, 211, 94, 0.5),
                0 4px 15px rgba(0, 0, 0, 0.15),
                inset 0 1px 0 rgba(255, 255, 255, 0.6),
                0 0 20px rgba(244, 211, 94, 0.3) !important;
        }
        
        .main .stButton > button[kind="primary"]:hover::before,
        .main .stButton > button[data-testid="baseButton-primary"]:hover::before {
            left: 100%;
        }
        
        .main .stButton > button[kind="primary"]:active,
        .main .stButton > button[data-testid="baseButton-primary"]:active {
            transform: translateY(-1px) scale(0.99) !important;
            box-shadow: 
                0 4px 15px rgba(244, 211, 94, 0.4),
                0 2px 8px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* Secondary Button - mirip sidebar tapi lebih terang */
        .main .stButton > button[kind="secondary"],
        .main .stButton > button[data-testid="baseButton-secondary"] {
            background: linear-gradient(135deg, rgba(13, 59, 102, 0.85) 0%, rgba(26, 77, 122, 0.8) 100%) !important;
            backdrop-filter: blur(10px) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            padding: 0.7rem 1.5rem !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 3px 12px rgba(13, 59, 102, 0.25) !important;
            position: relative !important;
            overflow: hidden !important;
        }
        
        .main .stButton > button[kind="secondary"]::before,
        .main .stButton > button[data-testid="baseButton-secondary"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s ease;
        }
        
        .main .stButton > button[kind="secondary"]:hover,
        .main .stButton > button[data-testid="baseButton-secondary"]:hover {
            background: linear-gradient(135deg, rgba(26, 77, 122, 0.9) 0%, rgba(13, 59, 102, 0.85) 100%) !important;
            border-color: rgba(255, 255, 255, 0.25) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 5px 18px rgba(13, 59, 102, 0.35) !important;
        }
        
        .main .stButton > button[kind="secondary"]:hover::before,
        .main .stButton > button[data-testid="baseButton-secondary"]:hover::before {
            left: 100%;
        }
        
        .main .stButton > button[kind="secondary"]:active,
        .main .stButton > button[data-testid="baseButton-secondary"]:active {
            transform: translateY(0) !important;
            box-shadow: 0 3px 12px rgba(13, 59, 102, 0.25) !important;
        }
        
        /* Default Button styles (fallback for main content) */
        .main .stButton > button {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(250, 240, 202, 0.85) 100%) !important;
            color: #0D3B66 !important;
            border: 2px solid rgba(13, 59, 102, 0.15) !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 0.7rem 1.5rem !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08) !important;
        }
        
        .main .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12) !important;
            border-color: rgba(13, 59, 102, 0.3) !important;
        }
        
        .main .stButton > button:active {
            transform: translateY(0) !important;
        }
        
        
        
        
        
        /* ===== OLD CARD STYLES (for other pages) ===== */
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