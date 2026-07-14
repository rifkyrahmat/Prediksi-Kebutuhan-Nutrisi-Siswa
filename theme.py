import streamlit as st

def load_theme():

    st.markdown("""
    <style>

    /* ===========================================
       Background
    =========================================== */

    .main{
        background-color: var(--background-color);
    }

    /* ===========================================
       Judul
    =========================================== */

    h1,h2,h3{
        color: var(--primary-color);
        font-weight:700;
    }

    /* ===========================================
       Metric Card
    =========================================== */

    [data-testid="metric-container"]{
        background-color: var(--secondary-background-color);
        border-radius:15px;
        padding:18px;
        border-left:8px solid var(--primary-color);
        box-shadow:0 4px 12px rgba(0,0,0,0.10);
    }

    /* ===========================================
       Tombol
    =========================================== */

    .stButton>button{
        width:100%;
        height:50px;
        border-radius:10px;
        background:#43A047;
        color:white;
        font-size:17px;
        font-weight:bold;
        border:none;
    }

    .stButton>button:hover{
        background:#2E7D32;
        color:white;
    }

    /* ===========================================
       Sidebar
    =========================================== */

    [data-testid="stSidebar"]{
        background-color: var(--secondary-background-color);
    }

    /* ===========================================
       Input Box
    =========================================== */

    .stTextInput input,
    .stNumberInput input{
        border-radius:10px;
    }

    /* ===========================================
       Selectbox
    =========================================== */

    .stSelectbox{
        border-radius:10px;
    }

    /* ===========================================
       Dataframe
    =========================================== */

    .stDataFrame{
        border-radius:10px;
    }

    /* ===========================================
       Responsive HP
    =========================================== */

    @media (max-width:768px){

        h1{
            font-size:28px;
        }

        h2{
            font-size:22px;
        }

        h3{
            font-size:18px;
        }

        .stButton>button{
            height:45px;
            font-size:15px;
        }

        [data-testid="metric-container"]{
            padding:12px;
        }

    }

    </style>
    """, unsafe_allow_html=True)