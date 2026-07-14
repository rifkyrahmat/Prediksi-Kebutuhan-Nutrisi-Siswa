import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Menu Makanan",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Menu Makanan MBG")
st.markdown("---")

# ==========================
# Membuat database
# ==========================

if not os.path.exists("database"):
    os.makedirs("database")

if not os.path.exists("database/menu_makanan.xlsx"):

    df = pd.DataFrame({
        "Kategori": ["Menu Besar", "Menu Kecil"],
        "Energi (Kkal)": [545.4, 365.9],
        "Protein (g)": [18.8, 13.7],
        "Lemak (g)": [16.9, 12.8],
        "Karbohidrat (g)": [78.2, 47.9],
        "Serat (g)": [4.2, 2.7]
    })

    df.to_excel(
        "database/menu_makanan.xlsx",
        index=False
    )

menu = pd.read_excel("database/menu_makanan.xlsx")


st.markdown("---")

col1, col2 = st.columns(2)

# ==========================
# MENU BESAR
# ==========================

with col1:

    st.success("🍛 MENU BESAR")

    st.metric("Energi", "545.4 Kkal")
    st.metric("Protein", "18.8 g")
    st.metric("Lemak", "16.9 g")
    st.metric("Karbohidrat", "78.2 g")
    st.metric("Serat", "4.2 g")

# ==========================
# MENU KECIL
# ==========================

with col2:

    st.info("🥛 MENU KECIL")

    st.metric("Energi", "365.9 Kkal")
    st.metric("Protein", "13.7 g")
    st.metric("Lemak", "12.8 g")
    st.metric("Karbohidrat", "47.9 g")
    st.metric("Serat", "2.7 g")