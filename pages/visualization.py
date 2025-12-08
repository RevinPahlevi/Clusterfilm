import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from helpers import require_model, plot_clusters

def show_visualization():
    require_model()
    
    df = st.session_state["clean_df"]
    labels = st.session_state["cluster_labels"]
    centers = st.session_state["kmeans_model"].cluster_centers_
    
    # Import fungsi interpretasi
    from helpers import interpret_clusters, generate_pdf_report
    
    # Dapatkan interpretasi cluster
    interpretations = interpret_clusters(df)
    
    # ===== HEADER SECTION =====
    st.markdown("""
        <div class="viz-header">
            <div class="viz-icon">📊</div>
            <h1 class="viz-title">Visualisasi Hasil Clustering</h1>
            <p class="viz-subtitle">Eksplorasi visual dari pengelompokan film</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ===== SUMMARY STATS =====
    n_clusters = len(interpretations)
    total_films = len(df)
    avg_rating = df['vote_average'].mean()
    
    stat1, stat2, stat3, stat_pdf = st.columns([1, 1, 1, 1])
    
    with stat1:
        st.markdown(f"""
            <div class="viz-stat-card">
                <span class="viz-stat-icon">📊</span>
                <span class="viz-stat-value">{n_clusters}</span>
                <span class="viz-stat-label">Cluster</span>
            </div>
        """, unsafe_allow_html=True)
    
    with stat2:
        st.markdown(f"""
            <div class="viz-stat-card">
                <span class="viz-stat-icon">🎬</span>
                <span class="viz-stat-value">{total_films:,}</span>
                <span class="viz-stat-label">Film</span>
            </div>
        """, unsafe_allow_html=True)
    
    with stat3:
        st.markdown(f"""
            <div class="viz-stat-card">
                <span class="viz-stat-icon">⭐</span>
                <span class="viz-stat-value">{avg_rating:.1f}</span>
                <span class="viz-stat-label">Avg Rating</span>
            </div>
        """, unsafe_allow_html=True)
    
    with stat_pdf:
        # Simple PDF Button - no extra container
        if st.button("📥 Download PDF", type="secondary", use_container_width=True, key="pdf_btn"):
            with st.spinner("Generating..."):
                pdf_bytes = generate_pdf_report(df, interpretations)
                from datetime import datetime
                filename = f"Laporan_Clustering_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                st.download_button(
                    label="⬇️ Simpan File",
                    data=pdf_bytes,
                    file_name=filename,
                    mime="application/pdf",
                    use_container_width=True
                )
    
    st.markdown("<div style='height: 0.8rem;'></div>", unsafe_allow_html=True)
    
    # ===== CHART TABS =====
    tab1, tab2 = st.tabs(["📈 Scatter Plot", "📊 Bar Chart"])

    with tab1:
        # Chart Header
        st.markdown("""
            <div class="chart-header">
                <span class="chart-header-icon">🎯</span>
                <span class="chart-header-title">Persebaran Cluster: Rating vs Popularitas</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Buat mapping cluster ke label untuk legend
        df_plot = df.copy()
        df_plot['Cluster_Label'] = df_plot['Cluster'].map(
            lambda x: f"C{x}: {interpretations[x]['label']}"
        )
        
        fig, ax = plt.subplots(figsize=(10, 5))
        
        sns.scatterplot(
            x=df_plot['vote_average'], 
            y=df_plot['popularity'], 
            hue=df_plot['Cluster_Label'],
            palette='tab10',
            s=60,
            alpha=0.8, 
            edgecolor='white',
            linewidth=0.5,
            ax=ax
        )
        
        ax.set_title('', fontsize=14)
        ax.set_xlabel('Rating (Vote Average)', fontsize=10)
        ax.set_ylabel('Popularitas', fontsize=10)
        ax.grid(True, alpha=0.3, linestyle='--')
        plt.legend(title='Cluster', bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, fontsize=8)
        plt.tight_layout()
        st.pyplot(fig)
        
    with tab2:
        # Chart Header
        st.markdown("""
            <div class="chart-header">
                <span class="chart-header-icon">📊</span>
                <span class="chart-header-title">Distribusi Jumlah Film per Cluster</span>
            </div>
        """, unsafe_allow_html=True)
        
        df_count = df.copy()
        df_count['Cluster_Label'] = df_count['Cluster'].map(
            lambda x: f"C{x}: {interpretations[x]['label']}"
        )
        
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.countplot(x='Cluster_Label', data=df_count, palette='tab10', ax=ax)
        ax.set_ylabel("Jumlah Film", fontsize=10)
        ax.set_xlabel("Cluster", fontsize=10)
        ax.set_title('', fontsize=14)
        ax.grid(True, axis='y', alpha=0.3, linestyle='--')
        plt.xticks(rotation=30, ha='right', fontsize=9)
        plt.tight_layout()
        st.pyplot(fig)
    
    # ===== CLUSTER INTERPRETATION =====
    st.markdown("""
        <div class="interpretation-header">
            <span class="interp-h-icon">📖</span>
            <span class="interp-h-title">Karakteristik Setiap Cluster</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Cluster cards in grid
    cols = st.columns(min(3, n_clusters))
    
    for idx, cluster_id in enumerate(sorted(interpretations.keys())):
        info = interpretations[cluster_id]
        col_idx = idx % 3
        
        with cols[col_idx]:
            # Determine color based on cluster characteristics
            if "Blockbuster" in info['label']:
                card_color = "blockbuster"
            elif "Hidden" in info['label']:
                card_color = "hidden"
            elif "Mainstream" in info['label']:
                card_color = "mainstream"
            elif "Average" in info['label']:
                card_color = "average"
            else:
                card_color = "default"
            
            st.markdown(f"""
                <div class="cluster-card {card_color}">
                    <div class="cluster-card-header">
                        <span class="cluster-badge">C{cluster_id}</span>
                        <span class="cluster-label">{info['label']}</span>
                    </div>
                    <div class="cluster-stats">
                        <div class="cluster-stat-item">
                            <span class="csi-icon">🎬</span>
                            <span class="csi-value">{info['count']:,}</span>
                            <span class="csi-label">Film</span>
                        </div>
                        <div class="cluster-stat-item">
                            <span class="csi-icon">⭐</span>
                            <span class="csi-value">{info['avg_rating']:.1f}</span>
                            <span class="csi-label">Rating</span>
                        </div>
                        <div class="cluster-stat-item">
                            <span class="csi-icon">🔥</span>
                            <span class="csi-value">{info['avg_popularity']:.0f}</span>
                            <span class="csi-label">Popularity</span>
                        </div>
                    </div>
                    <p class="cluster-desc">{info['description']}</p>
                </div>
            """, unsafe_allow_html=True)
    
    # ===== NAVIGATION =====
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    col_spacer, col_next = st.columns([6, 2])
    with col_next:
        if st.button("Next: Rekomendasi ›", type="primary", use_container_width=True, key="viz_next"):
            st.session_state["page"] = "Rekomendasi"
            st.rerun()