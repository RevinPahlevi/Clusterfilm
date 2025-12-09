import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# --- HELPER: CEK DATA ---
def require_raw_data():
    if st.session_state.get("raw_df") is None:
        st.warning("⚠️ Silakan upload dataset terlebih dahulu di menu **Upload Dataset**.")
        st.stop()

def require_clean_data():
    if st.session_state.get("clean_df") is None:
        st.warning("⚠️ Silakan lakukan preprocessing data terlebih dahulu.")
        st.stop()

def require_model():
    if st.session_state.get("kmeans_model") is None:
        st.warning("⚠️ Model belum dilatih. Silakan lakukan clustering di menu **Analisis Data**.")
        st.stop()

# --- HELPER: KONVERSI FORMAT ANGKA ---
def convert_numeric_columns(df: pd.DataFrame, columns: list):
    """
    Mengkonversi kolom dengan format angka string (1.175.267) ke float.
    Format dengan titik sebagai pemisah ribuan akan dikonversi ke numerik.
    """
    df = df.copy()
    for col in columns:
        if col in df.columns:
            # Cek apakah kolom berupa string
            if df[col].dtype == 'object':
                # Hapus titik pemisah ribuan dan ganti koma dengan titik (jika ada)
                df[col] = df[col].astype(str).str.replace('.', '', regex=False)
                df[col] = df[col].str.replace(',', '.', regex=False)
                # Konversi ke numeric, error jadi NaN
                df[col] = pd.to_numeric(df[col], errors='coerce')
            else:
                # Pastikan sudah numeric
                df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# --- HELPER: PREPROCESSING (SCALING) ---
def preprocess_data(df: pd.DataFrame):
    """
    Membersihkan data dan melakukan Scaling (Normalisasi).
    K-Means sangat sensitif terhadap skala data.
    """
    df = df.copy()
    features = st.session_state["features"]
    
    # Validasi kolom
    missing_cols = [c for c in features if c not in df.columns]
    if missing_cols:
        st.error(f"❌ Kolom berikut tidak ditemukan: {missing_cols}")
        st.stop()

    # Konversi kolom fitur ke format numerik (handle format 1.175.267)
    df = convert_numeric_columns(df, features)

    # Ambil kolom fitur saja + Judul (untuk info tooltip nanti)
    # Jika dataset punya judul film, kita sertakan, jika tidak skip
    cols_to_keep = features.copy()
    if 'title' in df.columns:
        cols_to_keep.append('title')
    elif 'original_title' in df.columns:
        cols_to_keep.append('original_title')
        df.rename(columns={'original_title': 'title'}, inplace=True)
    
    df = df[cols_to_keep].dropna()

    # Lakukan Scaling hanya pada kolom numerik (fitur)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[features])
    
    # Simpan hasil scaling ke dataframe baru
    df_scaled = pd.DataFrame(scaled_data, columns=features, index=df.index)
    
    # Jika ada judul, gabungkan kembali
    if 'title' in df.columns:
        df_scaled['title'] = df['title']

    return df, df_scaled, scaler

# --- HELPER: PLOT ELBOW METHOD ---
def plot_elbow_method(df_scaled):
    from sklearn.cluster import KMeans
    
    wcss = [] # Within-Cluster Sum of Square
    K_range = range(1, 11)
    
    features = st.session_state["features"]
    X = df_scaled[features]

    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(K_range, wcss, marker='o', linestyle='--', color='#E50914') # Warna Merah Netflix
    ax.set_title('Elbow Method (Menentukan Jumlah Cluster Optimal)')
    ax.set_xlabel('Jumlah Cluster (k)')
    ax.set_ylabel('Inersia (WCSS)')
    st.pyplot(fig)

# --- HELPER: SCATTER PLOT CLUSTER ---
def plot_clusters(df, labels, centers):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Scatter plot data points
    sns.scatterplot(
        x=df['vote_average'], 
        y=df['popularity'], 
        hue=labels, 
        palette='viridis', 
        s=60, 
        alpha=0.7, 
        ax=ax
    )
    
    # Plot Centroids (Pusat Cluster) - Harus di-inverse transform jika mau akurat di plot asli
    # Tapi untuk simplifikasi visualisasi, kita plot berdasarkan warna label saja cukup jelas
    
    ax.set_title('Distribusi Cluster Film: Rating vs Popularitas', fontsize=14)
    ax.set_xlabel('Rating (Vote Average)')
    ax.set_ylabel('Popularitas')
    plt.legend(title='Cluster')
    st.pyplot(fig)

# --- HELPER: INTERPRETASI CLUSTER ---
def interpret_clusters(df_clean):
    """
    Memberikan interpretasi/label UNIK untuk setiap cluster berdasarkan karakteristiknya.
    Menggunakan sistem ranking untuk memastikan tidak ada duplikasi label.
    
    Returns:
        dict: {cluster_id: {'label': str, 'description': str, 'avg_rating': float, 'avg_popularity': float}}
    """
    features = st.session_state["features"]
    
    # Hitung rata-rata fitur per cluster
    cluster_stats = df_clean.groupby("Cluster")[features].mean().reset_index()
    
    # Normalisasi rating dan popularity ke skala 0-1 untuk perbandingan fair
    rating_min = cluster_stats['vote_average'].min()
    rating_max = cluster_stats['vote_average'].max()
    pop_min = cluster_stats['popularity'].min()
    pop_max = cluster_stats['popularity'].max()
    
    # Hindari division by zero
    rating_range = rating_max - rating_min if rating_max != rating_min else 1
    pop_range = pop_max - pop_min if pop_max != pop_min else 1
    
    cluster_stats['rating_norm'] = (cluster_stats['vote_average'] - rating_min) / rating_range
    cluster_stats['pop_norm'] = (cluster_stats['popularity'] - pop_min) / pop_range
    
    # Buat skor komposit (rating lebih penting, bobot 60:40)
    cluster_stats['composite_score'] = cluster_stats['rating_norm'] * 0.6 + cluster_stats['pop_norm'] * 0.4
    
    # Ranking berdasarkan skor komposit (tertinggi = rank 1)
    cluster_stats['rank'] = cluster_stats['composite_score'].rank(ascending=False, method='first').astype(int)
    
    # Definisi label berdasarkan jumlah cluster
    n_clusters = len(cluster_stats)
    
    # Label pool dengan prioritas (akan dipilih berdasarkan ranking)
    label_definitions = [
        {
            'label': "🌟 Blockbuster",
            'description': "Film berkualitas tinggi dengan popularitas sangat baik. Film-film yang banyak ditonton dan mendapat rating bagus."
        },
        {
            'label': "💎 Hidden Gems", 
            'description': "Film berkualitas tinggi namun kurang populer. Mungkin film indie atau kurang promosi namun berkualitas."
        },
        {
            'label': "🎬 Mainstream",
            'description': "Film populer dengan kualitas cukup baik. Film komersial yang banyak ditonton dan cukup disukai."
        },
        {
            'label': "📽️ Average Films",
            'description': "Film dengan rating dan popularitas rata-rata. Film standar yang tidak terlalu menonjol."
        },
        {
            'label': "📺 Populer Kontroversial",
            'description': "Film populer namun rating rendah. Mungkin banyak ditonton tapi kurang disukai kritikus."
        },
        {
            'label': "🎞️ Niche/Low Quality",
            'description': "Film dengan rating dan popularitas rendah. Film dengan target audiens terbatas atau kualitas kurang."
        },
    ]
    
    interpretations = {}
    
    for _, row in cluster_stats.iterrows():
        cluster_id = int(row['Cluster'])
        avg_rating = row['vote_average']
        avg_popularity = row['popularity']
        avg_vote_count = row.get('vote_count', 0)
        rank = int(row['rank'])
        
        # Pilih label berdasarkan ranking (rank 1 = label terbaik)
        # Jika cluster lebih banyak dari label, gunakan modulo
        label_idx = min(rank - 1, len(label_definitions) - 1)
        selected_label = label_definitions[label_idx]
        
        interpretations[cluster_id] = {
            'label': selected_label['label'],
            'description': selected_label['description'],
            'avg_rating': round(avg_rating, 2),
            'avg_popularity': round(avg_popularity, 2),
            'avg_vote_count': round(avg_vote_count, 2) if avg_vote_count else 0,
            'count': len(df_clean[df_clean['Cluster'] == cluster_id])
        }
    
    return interpretations

# --- HELPER: GENERATE PDF REPORT ---
def generate_pdf_report(df_clean, interpretations):
    """
    Generate PDF report dengan visualisasi dan interpretasi cluster.
    
    Returns:
        bytes: PDF file dalam format bytes untuk download
    """
    from matplotlib.backends.backend_pdf import PdfPages
    import io
    from datetime import datetime
    
    # Create BytesIO buffer untuk PDF
    pdf_buffer = io.BytesIO()
    
    with PdfPages(pdf_buffer) as pdf:
        # === PAGE 1: Cover Page ===
        fig = plt.figure(figsize=(8.5, 11))
        fig.text(0.5, 0.7, 'Laporan Clustering Film', 
                ha='center', va='center', fontsize=28, fontweight='bold')
        fig.text(0.5, 0.6, 'Analisis K-Means Clustering', 
                ha='center', va='center', fontsize=18)
        fig.text(0.5, 0.5, f'Tanggal: {datetime.now().strftime("%d %B %Y")}',
                ha='center', va='center', fontsize=14)
        fig.text(0.5, 0.4, f'Total Film: {len(df_clean):,}',
                ha='center', va='center', fontsize=14)
        fig.text(0.5, 0.35, f'Jumlah Cluster: {len(interpretations)}',
                ha='center', va='center', fontsize=14)
        plt.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # === PAGE 2: Scatter Plot ===
        fig, ax = plt.subplots(figsize=(11, 8.5))
        
        # Mapping cluster ke label
        df_plot = df_clean.copy()
        df_plot['Cluster_Label'] = df_plot['Cluster'].map(
            lambda x: f"C{x}: {interpretations[x]['label']}"
        )
        
        sns.scatterplot(
            x=df_plot['vote_average'], 
            y=df_plot['popularity'], 
            hue=df_plot['Cluster_Label'],
            palette='tab10',
            s=80,
            alpha=0.8,
            edgecolor='white',
            linewidth=0.5,
            ax=ax
        )
        
        ax.set_title('Distribusi Cluster Film: Rating vs Popularitas', 
                    fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Rating (Vote Average)', fontsize=12)
        ax.set_ylabel('Popularitas', fontsize=12)
        ax.grid(True, alpha=0.3, linestyle='--')
        plt.legend(title='Cluster', bbox_to_anchor=(1.05, 1), loc='upper left', 
                  frameon=True, shadow=True)
        plt.tight_layout()
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # === PAGE 3: Bar Chart ===
        fig, ax = plt.subplots(figsize=(11, 8.5))
        
        df_count = df_clean.copy()
        df_count['Cluster_Label'] = df_count['Cluster'].map(
            lambda x: f"C{x}: {interpretations[x]['label']}"
        )
        
        sns.countplot(x='Cluster_Label', data=df_count, palette='tab10', ax=ax)
        ax.set_ylabel("Jumlah Film", fontsize=12)
        ax.set_xlabel("Cluster", fontsize=12)
        ax.set_title("Distribusi Jumlah Film per Cluster", 
                    fontsize=16, fontweight='bold', pad=20)
        ax.grid(True, axis='y', alpha=0.3, linestyle='--')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # === PAGE 4+: Interpretasi per Cluster ===
        for cluster_id in sorted(interpretations.keys()):
            info = interpretations[cluster_id]
            
            fig = plt.figure(figsize=(8.5, 11))
            fig.text(0.5, 0.85, f"Cluster {cluster_id}: {info['label']}", 
                    ha='center', va='center', fontsize=20, fontweight='bold')
            
            # Informasi cluster
            y_pos = 0.75
            fig.text(0.1, y_pos, f"Jumlah Film: {info['count']:,}", 
                    fontsize=14, fontweight='bold')
            
            y_pos -= 0.08
            fig.text(0.1, y_pos, f"Rating Rata-rata: {info['avg_rating']:.2f}/10", 
                    fontsize=14)
            
            y_pos -= 0.08
            fig.text(0.1, y_pos, f"Popularitas Rata-rata: {info['avg_popularity']:.1f}", 
                    fontsize=14)
            
            y_pos -= 0.08
            fig.text(0.1, y_pos, f"Vote Count Rata-rata: {info['avg_vote_count']:.0f}", 
                    fontsize=14)
            
            # Deskripsi
            y_pos -= 0.12
            fig.text(0.1, y_pos, "Karakteristik:", 
                    fontsize=14, fontweight='bold')
            
            y_pos -= 0.06
            # Word wrap untuk deskripsi
            import textwrap
            wrapped_desc = textwrap.fill(info['description'], width=70)
            fig.text(0.1, y_pos, wrapped_desc, 
                    fontsize=12, va='top')
            
            plt.axis('off')
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()
        
        # Set metadata
        d = pdf.infodict()
        d['Title'] = 'Laporan Clustering Film'
        d['Author'] = 'Movie Clustering System'
        d['Subject'] = 'Analisis K-Means Clustering'
        d['Keywords'] = 'Clustering, Film, K-Means'
        d['CreationDate'] = datetime.now()
    
    # Get PDF bytes
    pdf_buffer.seek(0)
    return pdf_buffer.getvalue()

# --- HELPER: GENERATE RECOMMENDATION PDF ---
def generate_recommendation_pdf(input_data, cluster_pred, cluster_info, similar_films, features):
    """
    Generate PDF report untuk hasil rekomendasi film.
    
    Args:
        input_data: dict dengan keys 'rating', 'popularity', 'vote_count'
        cluster_pred: int, cluster yang diprediksi
        cluster_info: dict, informasi cluster dari interpretations
        similar_films: DataFrame, film-film serupa di cluster yang sama
        features: list, nama fitur yang digunakan
    
    Returns:
        bytes: PDF file dalam format bytes untuk download
    """
    from matplotlib.backends.backend_pdf import PdfPages
    import io
    from datetime import datetime
    
    # Create BytesIO buffer untuk PDF
    pdf_buffer = io.BytesIO()
    
    with PdfPages(pdf_buffer) as pdf:
        # === PAGE 1: Hasil Analisis ===
        fig = plt.figure(figsize=(8.5, 11))
        
        # Title
        fig.text(0.5, 0.85, 'Laporan Analisis Film', 
                ha='center', va='center', fontsize=24, fontweight='bold')
        fig.text(0.5, 0.80, f"Tanggal: {datetime.now().strftime('%d %B %Y, %H:%M')}", 
                ha='center', va='center', fontsize=12, color='gray')
        
        # Input Data
        y_pos = 0.70
        fig.text(0.5, y_pos, 'Data Input Film', 
                ha='center', va='center', fontsize=18, fontweight='bold')
        
        y_pos -= 0.08
        fig.text(0.2, y_pos, f"⭐ Rating:", fontsize=14, fontweight='bold')
        fig.text(0.5, y_pos, f"{input_data['rating']:.1f}/10", fontsize=14)
        
        y_pos -= 0.06
        fig.text(0.2, y_pos, f"🔥 Popularitas:", fontsize=14, fontweight='bold')
        fig.text(0.5, y_pos, f"{input_data['popularity']:.1f}", fontsize=14)
        
        y_pos -= 0.06
        fig.text(0.2, y_pos, f"📊 Jumlah Vote:", fontsize=14, fontweight='bold')
        fig.text(0.5, y_pos, f"{input_data['vote_count']:,}", fontsize=14)
        
        # Hasil Prediksi
        y_pos -= 0.12
        fig.text(0.5, y_pos, 'Hasil Analisis', 
                ha='center', va='center', fontsize=18, fontweight='bold')
        
        y_pos -= 0.08
        fig.text(0.5, y_pos, f"Cluster {cluster_pred}: {cluster_info['label']}", 
                ha='center', va='center', fontsize=16, 
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        # Deskripsi Cluster
        y_pos -= 0.10
        import textwrap
        wrapped_desc = textwrap.fill(cluster_info['description'], width=60)
        fig.text(0.5, y_pos, wrapped_desc, 
                ha='center', va='top', fontsize=12, style='italic')
        
        # Statistik Cluster
        y_pos -= 0.15
        fig.text(0.5, y_pos, 'Statistik Cluster', 
                ha='center', va='center', fontsize=16, fontweight='bold')
        
        y_pos -= 0.08
        fig.text(0.2, y_pos, f"⭐ Rating Rata-rata:", fontsize=12, fontweight='bold')
        fig.text(0.6, y_pos, f"{cluster_info['avg_rating']:.2f}/10", fontsize=12)
        
        y_pos -= 0.05
        fig.text(0.2, y_pos, f"🔥 Popularitas Rata-rata:", fontsize=12, fontweight='bold')
        fig.text(0.6, y_pos, f"{cluster_info['avg_popularity']:.1f}", fontsize=12)
        
        y_pos -= 0.05
        fig.text(0.2, y_pos, f"📊 Total Film di Cluster:", fontsize=12, fontweight='bold')
        fig.text(0.6, y_pos, f"{cluster_info['count']:,} film", fontsize=12)
        
        plt.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # === PAGE 2: Rekomendasi Film (jika ada) ===
        if 'title' in similar_films.columns and len(similar_films) > 0:
            top_films = similar_films.nlargest(15, 'vote_average')
            
            fig = plt.figure(figsize=(8.5, 11))
            fig.text(0.5, 0.92, f'Film Rekomendasi di {cluster_info["label"]}', 
                    ha='center', va='center', fontsize=20, fontweight='bold')
            fig.text(0.5, 0.88, f'Top 15 Film Berdasarkan Rating', 
                    ha='center', va='center', fontsize=14, style='italic')
            
            y_pos = 0.82
            for idx, (_, film) in enumerate(top_films.iterrows(), 1):
                title = film['title']
                if len(title) > 50:
                    title = title[:47] + "..."
                    
                rating = film['vote_average']
                
                # Alternating background color
                bg_color = '#f0f0f0' if idx % 2 == 0 else 'white'
                
                fig.text(0.08, y_pos, f"{idx}.", fontsize=11, fontweight='bold')
                fig.text(0.12, y_pos, title, fontsize=11)
                fig.text(0.85, y_pos, f"⭐ {rating:.1f}", fontsize=11, 
                        ha='right', fontweight='bold')
                
                # Draw subtle line
                if idx < len(top_films):
                    plt.plot([0.08, 0.92], [y_pos - 0.02, y_pos - 0.02], 
                            'k-', alpha=0.1, linewidth=0.5)
                
                y_pos -= 0.045
                
                if y_pos < 0.1:
                    break
            
            plt.axis('off')
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()
        
        # Set metadata
        d = pdf.infodict()
        d['Title'] = 'Laporan Analisis Film'
        d['Author'] = 'Movie Clustering System'
        d['Subject'] = 'Hasil Rekomendasi Film'
        d['CreationDate'] = datetime.now()
    
    # Get PDF bytes
    pdf_buffer.seek(0)
    return pdf_buffer.getvalue()