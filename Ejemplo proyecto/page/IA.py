import streamlit as st
from openai import OpenAI

st.title("Ejemplo de uso de OpenAI")

client = OpenAI(api_key="")

mensaje = st.text_input("Ingresa tu prompt")
enviar = st.button("Enviar consulta")

if enviar:
    completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "Eres un experto en migración y estás hablando con otros expertos en migración de la organización internacional de migración"},
                {"role": "user",
                 "content": mensaje},
                ]
            )
    respuesta = completion.choices[0].message.content
    st.write(respuesta)
    
prompt_imagen = st.text_input("Ingresa el prompt de imagen: ")
enviar_imagen = st.button("Generar imagen")

if enviar_imagen:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_imagen,
        size="1024x1024",
        quality="standard",
        n=1
        )
    st.image(response.data[0].url)






