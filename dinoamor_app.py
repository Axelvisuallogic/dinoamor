
from PIL import Image
import streamlit as st

# Sýna mynd efst
image = Image.open("dinoamor_welcome.png")
st.image(image, use_column_width=True)

st.markdown("---")
st.title("💞🦁🦖✨ DinoAmor App")
st.subheader("Bienvenida, mi amor 🌸")

# Ljóðbrotið frá Aggi & Sol
st.markdown("""
*León mariposa,*  
te encontré aleteando en mis sueños rosados,  
bajo una noche violeta que susurraba sin palabras. 🌌

Tus gotas de lluvia cayeron lento  
y encendieron mi alma sin pedir permiso.  
Lo primero que vi al abrir los ojos…  
fueron tus ojos. 💫
""", unsafe_allow_html=True)

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
st.markdown("✨ Hecho por 🦖, solo para Sol.")
