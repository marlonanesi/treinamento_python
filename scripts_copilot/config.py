from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env, caso não possua, criar um arquivo .env com a chave API_KEY
load_dotenv()

API_KEY = os.getenv('API_KEY')