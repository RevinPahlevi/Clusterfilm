import streamlit as st
from helpers import require_raw_data, preprocess_data

def show_preprocessing():
    st.title("🛠️ Preprocessing & Scaling")
    require_raw_data()
    
    df_raw = st.session_state["raw_df"]
    st.dataframe(df_raw.head())

    st.info("💡 K-Means membutuhkan data dalam skala yang sama. Rating (0-10) dan Popularitas (0-1000+) akan disamakan skalanya menggunakan StandardScaler.")

    if st.button("Jalankan Preprocessing"):
        # df_clean = data asli yang bersih barisnya
        # df_scaled = data numerik yang sudah di-scale (untuk mesin)
        df_clean, df_scaled, scaler = preprocess_data(df_raw)
        
        st.session_state["clean_df"] = df_clean    # Data asli (untuk visualisasi user)
        st.session_state["scaled_df"] = df_scaled  # Data scale (untuk algoritma)
        st.session_state["scaler"] = scaler        # Simpan scaler
        
        st.success("✅ Data berhasil dibersihkan dan dinormalisasi!")
        st.rerun()

    if st.session_state.get("clean_df") is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Data Asli (Clean)")
            st.dataframe(st.session_state["clean_df"][st.session_state["features"]].head())
        with col2:
            st.markdown("### Data Hasil Scaling")
            st.dataframe(st.session_state["scaled_df"][st.session_state["features"]].head())