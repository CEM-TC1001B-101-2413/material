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

c1, c2 = st.columns([0.7, 0.3])

c1.write("La deforestación o desforestación1​ es un proceso provocado por la acción de los humanos, en el que se destruye o agota la superficie forestal,2​3​4​ generalmente con el objetivo de destinar el suelo a otra actividad. En la actualidad, está directamente relacionada con las actividades industriales, como la tala y quema para la expansión de la frontera agrícola para dar lugar a la agricultura intensiva y la ganadería. La expansión de las áreas urbanas y las actividades mineras también impulsan la deforestación. La construcción de carreteras y vías de acceso a bosques cada vez más remotos mediante la tala furtiva contribuye a la deforestación. En menor medida, la agricultura de subsistencia también está involucrada en actividades de deforestación.5​ Según el investigador británico Norman Myers, el 5 % de la deforestación se debe a cría de ganado, el 19 % a la tala excesiva, el 22 % a las plantaciones de árboles (sobre todo al aceite de palma) y el 54 % a la agricultura de tala y quema.6")

c2.image("deforestación.jpg")
c2.caption("Obtenido de: https://www.pexels.com/es-es/foto/vista-de-pajaro-de-la-pila-de-lena-1268076/")

st.video("https://www.youtube.com/watch?v=z4XzCA75JLs")

c3, c4, c5 = st.columns(3)

c3.metric("Índice de deforestación", "35%", "5%")

c4.metric("Gases de efecto invernadero", "500mg", "10mg")

c5.metric("Superficie de bosques", "1000km", "-100km")





