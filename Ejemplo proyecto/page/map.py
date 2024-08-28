import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos_mapa():
    df = pd.read_csv("data/estados_mexico.csv")
    return df

df = cargar_datos_mapa()

st.title("Ejemplo de mapa")

st.map(df, latitude="Latitud", longitude="Longitud")

