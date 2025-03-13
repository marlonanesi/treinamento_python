# TOKEN excluido por motivos de segurança, caso utilize o servico deve fazer uma recarga no portal do desenvolvedor da openai ou caso utilize outro FM deve seguir a documentação do mesmo
# Caso não tenha um token, pode utilizar o mock para simular o comportamento do serviço, setando o MOCK_OPENAPI_SERVICE para True
# caso não possua o dotenv, instale com o comando: pip install python-dotenv ou utilize o venv para instalar as dependências do requirements vide README.md
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def str_to_bool(value):
    return value.lower() in ('true', '1', 't', 'y', 'yes')

API_KEY = os.getenv('API_KEY')
MOCK_OPENAPI_SERVICE = str_to_bool(os.getenv('MOCK_OPENAPI_SERVICE', 'True'))