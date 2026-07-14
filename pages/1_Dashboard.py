import streamlit as st
import pandas as pd
import os
from theme import load_theme

# ======================================================
# KONFIGURASI HALAMAN
# ======================================================

st.set_page_config(
    page_title="Dashboard MBG",
    page_icon="🏠",
    layout="wide"
)
load_theme()

# ======================================================
# JUDUL
# ======================================================

st.title("🏠 Dashboard Sistem Prediksi Nutrisi MBG")

st.markdown("""
Selamat datang di **Sistem Prediksi Kebutuhan Nutrisi Siswa Program Makan Bergizi Gratis (MBG)**.

Dashboard ini menampilkan ringkasan hasil prediksi nutrisi siswa yang dihasilkan menggunakan algoritma **XGBoost**.
""")

st.divider()
# ======================================================
# LOAD DATA
# ======================================================

laporan_path = "database/laporan.xlsx"

if os.path.exists(laporan_path):

    try:
        df = pd.read_excel(laporan_path)
    except:
        df = pd.DataFrame()

else:

    df = pd.DataFrame()

# ======================================================
# HITUNG STATISTIK
# ======================================================

total = len(df)

if total > 0:

    menu_besar = df["Rekomendasi"].astype(str).str.contains("Besar", case=False).sum()
    menu_kecil = df["Rekomendasi"].astype(str).str.contains("Kecil", case=False).sum()

    rata_kalori = df["Kalori"].mean()

    kalori_tertinggi = df["Kalori"].max()

    kalori_terendah = df["Kalori"].min()

    rata_protein = df["Protein"].mean()

else:

    menu_besar = 0
    menu_kecil = 0
    rata_kalori = 0
    kalori_tertinggi = 0
    kalori_terendah = 0
    rata_protein = 0

# ======================================================
# CARD
# ======================================================

c1, c2, c3 = st.columns(3)

c1.metric(
    "📋 Total Prediksi",
    total
)

c2.metric(
    "🍽️ Menu Besar",
    menu_besar
)

c3.metric(
    "🥗 Menu Kecil",
    menu_kecil
)

st.markdown("")

c4, c5, c6 = st.columns(3)

c4.metric(
    "🔥 Rata-rata Kalori",
    f"{rata_kalori:.0f} Kkal"
)

c5.metric(
    "⬆️ Kalori Tertinggi",
    f"{kalori_tertinggi:.0f} Kkal"
)

c6.metric(
    "⬇️ Kalori Terendah",
    f"{kalori_terendah:.0f} Kkal"
)

# ======================================================
# GRAFIK
# ======================================================

kiri, kanan = st.columns(2)

with kiri:

    st.subheader("📈 Kalori Setiap Siswa")

    if total > 0:

        chart = df[["Nama", "Kalori"]].set_index("Nama")

        st.bar_chart(chart)

    else:

        st.info("Belum ada data.")

with kanan:

    st.subheader("🥧 Distribusi Menu")

    if total > 0:

        pie = pd.DataFrame({
            "Menu":[
                "Menu Besar",
                "Menu Kecil"
            ],
            "Jumlah":[
                menu_besar,
                menu_kecil
            ]
        })

        st.bar_chart(
            pie.set_index("Menu")
        )

    else:

        st.info("Belum ada data.")

st.markdown("---")

# ======================================================
# DATA TERBARU
# ======================================================

st.subheader("📄 Data Prediksi Terbaru")

if total > 0:

    st.dataframe(
        df.tail(10),
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("Belum ada data prediksi.")

st.markdown("---")

st.caption("Sistem Prediksi Kebutuhan Nutrisi Siswa Program MBG menggunakan algoritma XGBoost.")