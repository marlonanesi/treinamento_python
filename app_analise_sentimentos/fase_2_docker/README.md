# Análise de Sentimento de Comentários

Este projeto é uma aplicação em Python que utiliza a API da OpenAI configurada para analisar o sentimento de comentários escritos. A interface do usuário é construída usando Streamlit. O projeto é dividido em várias fases onde respectivamente:
1 - inicia com o app python com a funcionalidade principal rodando via console (streamlit como front e back com FastAPI)
2 - uso de conteinerização em Docker na aplicação (introducao devops) também orquestração com Docker Compose
3 - uso de banco de dados NoSQL (MongoDB) para armazenamento dos comentários e respostas
4 - uso de Kafka como fila, nessa fase o app irá gravar o comentário num tópico/fila Kafka, e um consumidor de forma asyncrona irá ler e processar (resiliencia a falhas)

## Requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes do Python)
- Docker instalado

## Configuração do Ambiente Virtual

Para garantir que todas as dependências do projeto sejam instaladas corretamente, recomenda-se o uso de um ambiente virtual (`.venv`). Siga os passos abaixo para configurar e ativar o ambiente virtual:

### Criar o Ambiente Virtual

1. Navegue até o diretório do projeto:
    ```sh
    cd c:/projetos/app
    ```

2. Crie o ambiente virtual:
    ```sh
    python -m venv .venv
    ```

### Ativar o Ambiente Virtual

1. No terminal, ative o ambiente virtual:
    ```sh
    .venv\Scripts\activate
    ```

### Instalar Dependências

1. Com o ambiente virtual ativado, instale as dependências listadas no arquivo [requirements.txt](http://_vscodecontentref_/1):
    ```sh
    pip install -r requirements.txt
    ```

### Desativar o Ambiente Virtual

1. Quando terminar de trabalhar no projeto, desative o ambiente virtual com o comando:
    ```sh
    deactivate
    ```

## Executar a Aplicação

### Frontend (Streamlit)

1. Com o ambiente virtual ativado, execute a aplicação Streamlit:
    ```sh
    streamlit run app.py
    ```

2. Acesse a aplicação no navegador através do endereço:
    ```
    http://localhost:8501
    ```

### Backend (FastAPI)

1. Com o ambiente virtual ativado, execute a aplicação FastAPI:
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

2. Acesse a documentação da API no navegador através do endereço:
    ```
    http://localhost:8000/docs
    ```

## Conteinerização com Docker

Para conteinerizar a aplicação, siga os passos abaixo:

1. Crie a imagem Docker:
    ```sh
    docker build -t app-streamlit .   // (dentro da pasta frontend)
    docker build -t app-fastapi .     // (dentro da pasta backend)
    ```

2. Execute o contêiner:
    ```sh
    docker run -p 8501:8501 app-streamlit // frontend
    docker run -p 8000:8000 app-fastapi // backend
    ```

## Orquestração com Docker Compose

Para orquestrar a aplicação usando Docker Compose, siga os passos abaixo:

1. Crie e inicie os serviços definidos no `docker-compose.yml`:
    ```sh
    docker-compose up --build
    ```

2. Acesse a aplicação no navegador através do endereço:
    ```
    http://localhost:8501
    ```

3. Acesse a documentação da API no navegador através do endereço:
    ```
    http://localhost:8000/docs
    ```
.