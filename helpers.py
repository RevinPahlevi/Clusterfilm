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