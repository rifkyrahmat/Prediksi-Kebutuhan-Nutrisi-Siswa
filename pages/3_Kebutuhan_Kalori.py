import streamlit as st
import pandas as pd
from theme import load_theme
# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Kebutuhan Kalori",
    page_icon="🔥",
    layout="wide"
)
load_theme()

# =====================================================
# JUDUL
# =====================================================

st.title("🔥 Standar Kebutuhan Kalori")

st.write("""
Halaman ini menampilkan **referensi kebutuhan energi harian siswa berdasarkan usia**.
Data ini digunakan sebagai acuan dalam proses prediksi kebutuhan nutrisi pada aplikasi MBG.
""")

st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_excel("database/kebutuhan_kalori.xlsx")

# =====================================================
# STATISTIK
# =====================================================

col1,col2,col3 = st.columns(3)

col1.metric(
    "Jumlah Data",
    len(df)
)

col2.metric(
    "Kalori Minimum",
    f"{df['Kalori'].min():.0f} Kkal"
)

col3.metric(
    "Kalori Maksimum",
    f"{df['Kalori'].max():.0f} Kkal"
)

st.markdown("---")

# =====================================================
# TABEL
# =====================================================

st.subheader("📋 Tabel Kebutuhan Kalori")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# =====================================================
# GRAFIK
# =====================================================

st.subheader("📈 Grafik Kebutuhan Kalori Berdasarkan Usia")

grafik = df.set_index("Umur")

st.line_chart(
    grafik,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# KESIMPULAN
# =====================================================

st.info("""
### 📌 Keterangan

- Semakin bertambah usia siswa, kebutuhan energi harian cenderung meningkat.
- Data ini merupakan **referensi**, sedangkan hasil prediksi pada halaman **Prediksi** dihitung menggunakan algoritma **XGBoost** berdasarkan usia, jenis kelamin, berat badan, tinggi badan, dan tingkat aktivitas.
""")