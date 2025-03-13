import streamlit as st
import requests
import os

# Obter o nome do host do FastAPI a partir da variável de ambiente ou usar 'fastapi' como padrão
fastapi_host = os.getenv('FASTAPI_HOST', 'fastapi')

def submit_comment(comment, rating):
    if comment.lower() == 'sair':
        st.stop()
    else:
        response = requests.post(f"http://{fastapi_host}:8000/feedback/", json={"comment": comment, "rating": rating})
        feedback = response.json()
        status_color = "green" if feedback['status'] == 'aprovado' else "red"
        st.write(f"**Você comentou:** {comment}")
        st.write(f"**Avaliação:** {rating} estrelas")
        st.write(f"**Feedback:** {feedback['descricao']}")
        st.markdown(f"**Status:** <span style='color:{status_color}'>{feedback['status']}</span>", unsafe_allow_html=True)

st.title("Input de Comentários - Análise de Sentimentos")

comment = st.text_input("Escreva seu comentário aqui:")
rating = st.slider("Avaliação (1 a 5 estrelas):", 1, 5, 3)
if st.button("Enviar"):
    submit_comment(comment, rating)