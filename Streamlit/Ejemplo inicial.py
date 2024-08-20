import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos_csv(archivo):
    df = pd.read_csv(archivo)
    return df

@st.cache_data
def cargar_datos_excel(archivo):
    df = pd.read_excel(archivo)
    return df

df = cargar_datos_csv("corregido.csv")

st.title("Mi primer sitio")

st.markdown("""## Usando Markdown
---
Listado ordenado:
1. Primer elemento
2. Segundo elemento
3. Tercer elemento

Listado no ordenado:
- Primer elemento
- Segundo elemento
- Tercer elemento""")

st.write("Deforestation in Federal Conservation Units")
# df.head(n) -> Muestra las primeras n filas
st.dataframe(df.head(20))
st.caption("Obtenido desde: https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadstserofcsv")