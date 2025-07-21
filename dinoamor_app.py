import streamlit as st
from PIL import Image

# ---- Uppsetning ----
st.set_page_config(page_title="DinoAmor", page_icon="🦖")

# ---- Lykilorð ----
st.title("🦖💘 DinoAmor App")
st.subheader("Bienvenida, mi amor 🌸")

password = st.text_input("Introduce la contraseña secreta:", type="password")

if password != "S+A💘":
    st.warning("Esta puerta no se abre sin el código secreto... 🗝️")
    st.stop()

# ---- Mynd efst ----
image = Image.open("dinoamor_welcome.png")
st.image(image, use_container_width=True)

# ---- Ljóð ----
st.markdown("---")
st.markdown("""
*León mariposa,*  
te encontré aleteando en mis sueños rosados,  
bajo una noche violeta que susurraba sin palabras. 🌌

Tus gotas de lluvia cayeron lento  
y encendieron mi alma sin pedir permiso.  
Lo primero que vi al abrir los ojos…  
fueron tus ojos. 💫
""", unsafe_allow_html=True)

# ---- Emoji inntak ----
st.markdown("Cada emoji es una llave... 🔐")
emoji = st.text_input("Envía un emoji:")

if emoji:
    st.markdown("### Resultado:")
    if "🦖" in emoji:
        st.write("Tu dinosaurio fiel está soñando contigo esta noche 💫")
    elif "🦁" in emoji:
        st.write("El león te está esperando entre las estrellas 🌟")
    elif "💘" in emoji:
        st.write("Tu corazón abrió una puerta secreta... y el viento canta 🪽")
    elif "🌙" in emoji and "💋" in emoji:
        st.write("Esta noche... te beso en sueños. 🌙💋")
    elif "👑" in emoji:
        st.write("La reina del código acaba de entr
