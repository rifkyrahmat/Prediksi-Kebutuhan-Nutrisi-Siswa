import streamlit as st
import pandas as pd
import os
from theme import load_theme


st.set_page_config(
    page_title="Data Siswa",
    page_icon="👨‍🎓",
    layout="wide"
)
load_theme()

# ======================================
# FILE EXCEL
# ======================================

os.makedirs("database", exist_ok=True)

file_data = "database/data_siswa.xlsx"

if not os.path.exists(file_data):

    df = pd.DataFrame(columns=[
        "Nama",
        "Usia",
        "Jenis Kelamin",
        "Berat Badan",
        "Tinggi Badan",
        "Aktivitas"
    ])

    df.to_excel(file_data,index=False)

df = pd.read_excel(file_data)

# ======================================
# FORM INPUT
# ======================================

st.subheader("➕ Tambah Data Siswa")

col1,col2 = st.columns(2)

with col1:

    nama = st.text_input("Nama Siswa")

    usia = st.number_input(
        "Usia",
        min_value=6,
        max_value=18,
        value=12
    )

    jk = st.selectbox(
        "Jenis Kelamin",
        [
            "Laki-laki",
            "Perempuan"
        ]
    )

with col2:

    berat = st.number_input(
        "Berat Badan (kg)",
        min_value=20,
        max_value=100,
        value=35
    )

    tinggi = st.number_input(
        "Tinggi Badan (cm)",
        min_value=100,
        max_value=200,
        value=140
    )

    aktivitas = st.selectbox(
        "Aktivitas",
        [
            "Rendah",
            "Sedang",
            "Tinggi"
        ]
    )

# ======================================
# SIMPAN
# ======================================

if st.button("💾 Simpan Data"):

    data_baru = pd.DataFrame({

        "Nama":[nama],
        "Usia":[usia],
        "Jenis Kelamin":[jk],
        "Berat Badan":[berat],
        "Tinggi Badan":[tinggi],
        "Aktivitas":[aktivitas]

    })

    df = pd.concat(
        [df,data_baru],
        ignore_index=True
    )

    df.to_excel(
        file_data,
        index=False
    )

    st.success("✅ Data berhasil disimpan.")

# ======================================
# TABEL
# ======================================

st.markdown("---")

st.subheader("📋 Data Seluruh Siswa")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ======================================
# JUMLAH SISWA
# ======================================

st.metric(
    "Jumlah Siswa",
    len(df)
)

# ======================================
# HAPUS DATA
# ======================================

st.markdown("---")

if st.button("🗑 Hapus Semua Data"):

    df = pd.DataFrame(columns=df.columns)

    df.to_excel(
        file_data,
        index=False
    )

    st.success("Semua data berhasil dihapus.")
    st.rerun()