import streamlit as st
import pandas as pd
import os
from theme import load_theme


st.set_page_config(
    page_title="Laporan Prediksi",
    page_icon="📋",
    layout="wide"
)
load_theme()

st.title("📋 Laporan Prediksi Nutrisi")

laporan_path = "database/laporan.xlsx"

if not os.path.exists(laporan_path):
    st.warning("Belum ada laporan.")
    st.stop()

try:
    df = pd.read_excel(laporan_path)
except Exception as e:
    st.error(f"Gagal membaca laporan : {e}")
    st.stop()

st.markdown("---")

# ===========================
# Statistik
# ===========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Prediksi", len(df))

if "Rekomendasi" in df.columns:

    menu_besar = (df["Rekomendasi"] == "🍽️ Menu Besar").sum() + \
                 (df["Rekomendasi"] == "Menu Besar").sum()

    menu_kecil = (df["Rekomendasi"] == "🥗 Menu Kecil").sum() + \
                 (df["Rekomendasi"] == "Menu Kecil").sum()

else:
    menu_besar = 0
    menu_kecil = 0

col2.metric("Menu Besar", menu_besar)
col3.metric("Menu Kecil", menu_kecil)

if "Kalori" in df.columns:
    rata = df["Kalori"].mean()
else:
    rata = 0

col4.metric("Rata-rata Kalori", f"{rata:.0f}")

st.markdown("---")

# ===========================
# Cari
# ===========================

cari = st.text_input("🔍 Cari Nama Siswa")

if cari != "":
    df = df[df["Nama"].astype(str).str.contains(cari, case=False)]

# ===========================
# Tabel
# ===========================

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ===========================
# Download
# ===========================

with open(laporan_path, "rb") as file:

    st.download_button(
        "📥 Download Laporan Excel",
        file,
        "Laporan_Prediksi_MBG.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

st.markdown("---")

# ===========================
# Hapus Laporan
# ===========================

if st.button("🗑 Hapus Semua Laporan"):

    pd.DataFrame(columns=df.columns).to_excel(
        laporan_path,
        index=False
    )

    st.success("Laporan berhasil dihapus.")

    st.rerun()