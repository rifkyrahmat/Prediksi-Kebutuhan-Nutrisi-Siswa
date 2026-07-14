import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime
from theme import load_theme

# ======================================================
# KONFIGURASI HALAMAN
# ======================================================

st.set_page_config(
    page_title="Prediksi Nutrisi MBG",
    page_icon="🍽️",
    layout="wide"
)

load_theme()

# ======================================================
# LOAD MODEL XGBOOST
# ======================================================

try:
    model = joblib.load("models/model_xgboost.pkl")
except Exception:
    st.error("❌ Model XGBoost tidak ditemukan.")
    st.stop()

# ======================================================
# MEMBUAT DATABASE
# ======================================================

os.makedirs("database", exist_ok=True)

laporan_path = "database/laporan.xlsx"

if not os.path.exists(laporan_path):

    laporan_awal = pd.DataFrame(columns=[
        "Nama",
        "Usia",
        "Jenis Kelamin",
        "Berat",
        "Tinggi",
        "Aktivitas",
        "Kalori",
        "Protein",
        "Lemak",
        "Karbohidrat",
        "Rekomendasi",
        "Waktu"
    ])

    laporan_awal.to_excel(
        laporan_path,
        index=False,
        engine="openpyxl"
    )

# ======================================================
# JUDUL
# ======================================================

st.title("🍽️ Prediksi Kebutuhan Nutrisi Siswa")

st.write("""
Masukkan data siswa untuk memperoleh prediksi kebutuhan nutrisi
menggunakan algoritma **XGBoost**.
""")

st.divider()

# ======================================================
# INPUT DATA
# ======================================================

st.subheader("📝 Input Data Siswa")

kiri, kanan = st.columns(2)

with kiri:

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

with kanan:

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

# ======================================================
# KONVERSI INPUT
# ======================================================

jk_value = 1 if jk == "Laki-laki" else 0

aktivitas_value = {
    "Rendah": 1,
    "Sedang": 2,
    "Tinggi": 3
}[aktivitas]

st.markdown("##")

prediksi_btn = st.button(
    "🚀 Prediksi Kebutuhan Nutrisi",
    use_container_width=True
)

# ======================================================
# MULAI PREDIKSI
# ======================================================

if prediksi_btn:

    # -----------------------------
    # VALIDASI INPUT
    # -----------------------------

    if nama.strip() == "":
        st.error("⚠️ Nama siswa harus diisi.")
        st.stop()

    # -----------------------------
    # DATA UNTUK MODEL
    # -----------------------------

    data = [[
        usia,
        jk_value,
        berat,
        tinggi,
        aktivitas_value
    ]]

    # -----------------------------
    # LOADING
    # -----------------------------

    with st.spinner("🔄 Sedang memprediksi kebutuhan nutrisi..."):

        progress = st.progress(0)

        for i in range(100):
            progress.progress(i + 1)

        hasil = model.predict(data)

        progress.empty()

    # -----------------------------
    # HASIL PREDIKSI
    # -----------------------------

    kalori = float(hasil[0][0])
    protein = float(hasil[0][1])
    lemak = float(hasil[0][2])
    karbohidrat = float(hasil[0][3])

    st.success("✅ Prediksi berhasil dilakukan menggunakan model XGBoost.")

    st.divider()
    
    # ======================================================
    # HASIL PREDIKSI
    # ======================================================

    st.subheader("📊 Hasil Prediksi Nutrisi")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🔥 Kalori",
        f"{kalori:.0f} Kkal"
    )

    c2.metric(
        "🥩 Protein",
        f"{protein:.1f} gram"
    )

    c3.metric(
        "🥑 Lemak",
        f"{lemak:.1f} gram"
    )


    c4.metric(
     "🍚 Karbohidrat",
     f"{karbohidrat:.1f} gram"
    )

    st.divider()

    # ======================================================
    # INFORMASI SISWA
    # ======================================================

    st.subheader("👤 Informasi Siswa")

    kiri, kanan = st.columns(2)

    with kiri:

     st.write(f"**Nama :** {nama}")
     st.write(f"**Usia :** {usia} tahun")
     st.write(f"**Jenis Kelamin :** {jk}")

    with kanan:

     st.write(f"**Berat Badan :** {berat} kg")
     st.write(f"**Tinggi Badan :** {tinggi} cm")
     st.write(f"**Aktivitas :** {aktivitas}")

    st.divider()

    # ======================================================
    # GRAFIK
    # ======================================================

    st.subheader("📈 Grafik Hasil Prediksi")

    grafik = pd.DataFrame({

      "Nutrisi":[
            "Kalori",
            "Protein",
            "Lemak",
            "Karbohidrat"
        ],

        "Nilai":[
            kalori,
            protein,
            lemak,
            karbohidrat
        ]

    })

    st.bar_chart(
        grafik.set_index("Nutrisi"),
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # REKOMENDASI MENU
    # ======================================================

    if kalori >= 2500:

        rekomendasi = "🍽️ Menu Besar"

        st.success(f"### Rekomendasi : {rekomendasi}")

    else:

        rekomendasi = "🥗 Menu Kecil"

        st.info(f"### Rekomendasi : {rekomendasi}")

    # ======================================================
    # SIMPAN KE DATABASE LAPORAN
    # ======================================================

    try:
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        data_baru = pd.DataFrame([{
            "Nama": nama,
            "Usia": usia,
            "Jenis Kelamin": jk,
            "Berat": berat,
            "Tinggi": tinggi,
            "Aktivitas": aktivitas,
            "Kalori": kalori,
            "Protein": protein,
            "Lemak": lemak,
            "Karbohidrat": karbohidrat,
            "Rekomendasi": rekomendasi,
            "Waktu": waktu_sekarang
        }])
        
        laporan_path = "database/laporan.xlsx"
        if os.path.exists(laporan_path):
            df_laporan = pd.read_excel(laporan_path)
            df_laporan = pd.concat([df_laporan, data_baru], ignore_index=True)
        else:
            df_laporan = data_baru
            
        df_laporan.to_excel(laporan_path, index=False, engine="openpyxl")
    except Exception as e:
        st.error(f"⚠️ Gagal menyimpan data laporan: {e}")

    st.info(f"""
    ### 📌 Ringkasan Prediksi

    Berdasarkan data yang dimasukkan, sistem memprediksi bahwa **{nama}**
    membutuhkan sekitar **{kalori:.0f} Kkal** energi per hari.

    Kebutuhan nutrisi yang diprediksi adalah:

    - 🔥 Kalori : **{kalori:.0f} Kkal**
    - 🥩 Protein : **{protein:.1f} gram**
    - 🥑 Lemak : **{lemak:.1f} gram**
    - 🍚 Karbohidrat : **{karbohidrat:.1f} gram**

    Berdasarkan hasil tersebut, sistem merekomendasikan **{rekomendasi}**
    untuk Program Makan Bergizi Gratis (MBG).
    """)

    st.divider()