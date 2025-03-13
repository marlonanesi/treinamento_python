# Use a imagem base oficial do Python
FROM python:3.11

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o contêiner
COPY . .

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "streamlit.py"]