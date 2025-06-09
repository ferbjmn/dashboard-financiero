import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(layout="wide", page_title="Dashboard Financiero con IA")
st.markdown("<h1 style='text-align: center;'>📊 Dashboard Financiero con IA - Comparación de Empresas</h1>", unsafe_allow_html=True)

# CSS personalizado para modo oscuro
st.markdown("""
    <style>
    body {
        background-color: #111111;
        color: #FFFFFF;
    }
    .stTextInput > div > div > input {
        background-color: #333333;
        color: white;
    }
    .stDataFrame {
        background-color: #222222;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Entrada de tickers
tickers_input = st.text_input("🧾 Escribí los tickers separados por coma:", value="AAPL,MSFT,GOOGL")
tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]

# Variables de mercado
rf = 0.04
rm = 0.09
kd = 0.06
tc = 0.25

resultados = []
