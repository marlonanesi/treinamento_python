import streamlit as st
import requests
import os

# Obter o nome do host do FastAPI a partir da variável de ambiente ou usar 'fastapi' como padrão
fastapi_host = os.getenv('FASTAPI_HOST', 'localhost')

def submit_comment(comment, rating):
    response = requests.post(f"http://{fastapi_host}:8000/feedback/", json={"comment": comment, "rating": rating})
    feedback = response.json()
    st.markdown(f"**Status:** <span style='color:green'>{feedback['status']}</span>", unsafe_allow_html=True)

def display_feedback():
    st.subheader("Feedbacks Salvos")
    response = requests.get(f"http://{fastapi_host}:8000/get-feedback/")
    feedback_list = response.json()
    
    for feedback_dict in feedback_list:
        st.write(f"**ID:** {feedback_dict['id']}")
        st.write(f"**Comentário:** {feedback_dict['comment']}")
        st.write(f"**Avaliação:** {feedback_dict['rating']} estrelas")
        st.write(f"**Analise de sentimento:** {feedback_dict['descricao']}")
        st.write(f"**Status:** {feedback_dict['status']}")
        st.write("---")

st.title("Input de Comentários - Análise de Sentimentos")

tab1, tab2 = st.tabs(["Enviar Comentário", "Ver Feedbacks"])

with tab1:
    comment = st.text_input("Escreva seu comentário aqui:")
    rating = st.slider("Avaliação (1 a 5 estrelas):", 1, 5, 3)
    if st.button("Enviar"):
        submit_comment(comment, rating)

with tab2:
    display_feedback()