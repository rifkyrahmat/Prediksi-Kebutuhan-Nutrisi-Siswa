import streamlit as st
from theme import load_theme

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Sistem Prediksi Nutrisi MBG",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_theme()


# ==========================================
# HEADER
# ==========================================

st.title("🥗 Sistem Prediksi Kebutuhan Nutrisi")
st.subheader("Program Makan Bergizi Gratis (MBG)")

st.markdown("---")

# ==========================================
# DESKRIPSI
# ==========================================

st.markdown("""
<div class='box'>

### 📖 Tentang Aplikasi

Aplikasi ini digunakan untuk memprediksi kebutuhan nutrisi siswa menggunakan algoritma **Extreme Gradient Boosting (XGBoost)**.

Prediksi dilakukan berdasarkan:

- 👦 Usia
- 🚻 Jenis Kelamin
- ⚖️ Berat Badan
- 📏 Tinggi Badan
- 🏃 Tingkat Aktivitas

Hasil prediksi meliputi:

- 🔥 Kalori
- 🥩 Protein
- 🥑 Lemak
- 🍚 Karbohidrat

Selanjutnya sistem akan memberikan rekomendasi **Menu Besar** atau **Menu Kecil** sesuai kebutuhan nutrisi siswa.

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# FITUR
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 📊 Dashboard

Melihat informasi umum sistem.
""")

with col2:
    st.success("""
### 🤖 Prediksi

Melakukan prediksi kebutuhan nutrisi siswa.
""")

with col3:
    st.warning("""
### 📄 Laporan

Menyimpan seluruh hasil prediksi ke Excel.
""")

st.markdown("---")

# ==========================================
# FOOTER
# ==========================================

st.caption("© 2026 | Sistem Prediksi Kebutuhan Nutrisi Program Makan Bergizi Gratis (MBG) menggunakan XGBoost")