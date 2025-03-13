from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
MOCK_OPENAPI_SERVICE = False