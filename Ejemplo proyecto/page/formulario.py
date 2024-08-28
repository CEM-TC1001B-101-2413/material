import streamlit as st
import pandas as pd

st.title("Formulario")

formulario = st.form(key="formulario", clear_on_submit=True)

nombre = formulario.text_input("Nombre")
edad = formulario.number_input("Edad",
                               min_value=0,
                               max_value=120,
                               value=18,
                               format="%d")
satisfaccion = formulario.slider("Satisfacción",
                                 min_value=0,
                                 max_value=10,
                                 step=1,
                                 value=5)
compartir = formulario.radio("¿Desea compartir sus datos",
                             ["Sí", "No"])

estados_mexico = [
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", 
    "Chiapas", "Chihuahua", "Coahuila", "Colima", "Ciudad de México", 
    "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", 
    "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", 
    "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", 
    "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
]

estado = formulario.selectbox("Selecciona tu estado",
                              estados_mexico)

formulario.write("Selecciona los idiomas que hablas")

español = formulario.checkbox("Español", value=True)
ingles = formulario.checkbox("Inglés")
aleman = formulario.checkbox("Alemán")
frances = formulario.checkbox("Francés")
portugues = formulario.checkbox("Portugués")

submit = formulario.form_submit_button("Guardar")

if submit:
    # Pares: "Nombre columna archivo": variable_codigo
    nueva_fila = pd.DataFrame([{
        "Nombre": nombre,
        "Edad": edad,
        "Satisfacción": satisfaccion,
        "Compartir": compartir,
        "Estado": estado,
        "Español": "Sí" if español else "No",
        "Inglés": "Sí" if ingles else "No",
        "Alemán": "Sí" if aleman else "No",
        "Francés": "Sí" if frances else "No",
        "Portugués": "Sí" if portugues else "No"
        }])
    df = pd.read_csv("data/datos.csv")
    df = pd.concat([df, nueva_fila], ignore_index=True)
    df.to_csv("data/datos.csv", index=False)
    formulario.success("Registro exitoso")







