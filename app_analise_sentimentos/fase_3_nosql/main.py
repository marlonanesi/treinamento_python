import subprocess
import uvicorn
import os
import sys

def start_streamlit():
    """
    Ponto de entrada principal do script
    Adiciona diretórios ao PYTHONPATH, inicia o Streamlit e executa o servidor Uvicorn.
    Orquestrador para facilitar a subida da aplicação localmente/via terminal, para desenvolvimento e debug.
    python main.py // da raiz dessa pasta
    """
    # Definir a variável de ambiente para o host do FastAPI
    os.environ['FASTAPI_HOST'] = 'localhost'
    
    # Usar o comando streamlit diretamente
    subprocess.Popen(["streamlit", "run", "frontend/streamlit.py"])

if __name__ == "__main__":
    # Adicionar o diretório raiz do projeto ao PYTHONPATH
    sys.path.append(os.getcwd())
    sys.path.append(os.path.join(os.getcwd(), 'backend'))
    start_streamlit()
    uvicorn.run("backend.fast_api:app", host="0.0.0.0", port=8000, reload=True)