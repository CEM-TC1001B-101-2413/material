import streamlit as st
import pandas as pd

def cargar_encuesta():
    df = pd.read_csv("data/datos.csv")
    # df.tail(n) -> Muestra las últimas n filas del archivo
    return df.tail(10)

df = cargar_encuesta()

st.title("Página de inicio")

st.write("Últimas 10 respuestas de nuestra encuesta")

st.dataframe(df)