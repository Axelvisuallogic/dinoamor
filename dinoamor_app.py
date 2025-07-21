
import streamlit as st

st.set_page_config(page_title="DinoAmor", page_icon="🦖")

st.title("🦖💘 DinoAmor App")
st.subheader("Bienvenida, mi amor 🌸")

st.markdown("Cada emoji es una llave... 🔐")

emoji = st.text_input("Envia un emoji:")

# Emoji-based logic
if emoji:
    st.markdown("### Resultado:")
    if "🦖" in emoji:
        st.write("Tu dinosaurio fiel está soñando contigo esta noche 💫")
    elif "🦁" in emoji:
        st.write("El león te está esperando entre las estrellas 🌟")
    elif "💘" in emoji:
        st.write("Tu corazón abrió una puerta secreta... y el viento canta 🪽")
    elif "🌙" in emoji:
        st.write("Nos vemos en los sueños. Esta noche tengo alas.")
    elif "👑" in emoji:
        st.write("La reina del código acaba de entrar 👑✨")
    else:
        st.write("Este emoji no está en el diccionario... pero quizás lo añado solo para ti 😉")

st.markdown("---")
st.markdown("✨ Hecho por Aggi, solo para Sol.")
