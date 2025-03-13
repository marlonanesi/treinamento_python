# Análise de Sentimento de Comentários

Este projeto é uma aplicação em Python que utiliza a API da OpenAI para analisar o sentimento de comentários escritos. A interface do usuário é desenvolvida usando Streamlit, enquanto o backend utiliza FastAPI. O projeto evolui em diferentes fases:

1. **Execução Inicial**: A aplicação roda localmente com Streamlit como frontend e FastAPI como backend.
2. **Conteinerização com Docker**: Implementação de Docker para conteinerizar a aplicação, incluindo orquestração com Docker Compose.
3. **Banco de Dados NoSQL**: Integração com MongoDB para armazenamento dos comentários e suas respostas.
4. **Processamento Assíncrono com Kafka**: Os comentários são gravados em um tópico Kafka, permitindo que um consumidor processador os leia e analise de forma assíncrona, garantindo resiliência a falhas.

## Estrutura do Projeto

- **`main.py`**: Arquivo utilizado apenas para inicialização local em modo de desenvolvimento. Ele é um facilitador para subir frontend e backend simultaneamente, mas ambos podem ser iniciados separadamente.
- **`backend/`**: Contém o serviço FastAPI responsável pelo processamento dos comentários.
- **`frontend/`**: Contém a interface Streamlit para interação com o usuário.

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
    .venv\Scripts\activate  # Windows
    source .venv/bin/activate  # Linux/Mac
    ```

### Instalar Dependências

1. Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

### Desativar o Ambiente Virtual

1. Quando terminar de trabalhar no projeto, desative o ambiente virtual:
    ```sh
    deactivate
    ```

## Configuração do Serviço da OpenAI

Para utilizar a API da OpenAI, crie um arquivo `.env` na pasta /backend e defina a variável `API_KEY` com o token da OpenAI:

```sh
API_KEY=seu_token_aqui
```

Caso não deseje utilizar a API da OpenAI, ative o mock da API definindo a variável `MOCK_OPENAPI_SERVICE` como `True` no arquivo `backend/config.py`:

```python
MOCK_OPENAPI_SERVICE = True
```

Isso permitirá que a aplicação funcione sem a necessidade de uma chave da OpenAI.

## Executar a Aplicação

### Frontend (Streamlit)

1. Com o ambiente virtual ativado, execute a aplicação Streamlit:
    ```sh
    streamlit run frontend/app.py
    ```

2. Acesse a aplicação no navegador através do endereço:
    ```
    http://localhost:8501
    ```

### Backend (FastAPI)

1. Com o ambiente virtual ativado, execute a aplicação FastAPI:
    ```sh
    uvicorn backend.app:app --host 0.0.0.0 --port 8000
    ```

2. Acesse a documentação da API no navegador através do endereço:
    ```
    http://localhost:8000/docs
    ```

## Conteinerização com Docker

Para conteinerizar a aplicação, siga os passos abaixo:

1. Crie as imagens Docker:
    ```sh
    docker build -t app-streamlit frontend/  # Cria a imagem do frontend
    docker build -t app-fastapi backend/  # Cria a imagem do backend
    ```

2. Execute os contêineres:
    ```sh
    docker run -p 8501:8501 app-streamlit  # Frontend
    docker run -p 8000:8000 app-fastapi  # Backend
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

