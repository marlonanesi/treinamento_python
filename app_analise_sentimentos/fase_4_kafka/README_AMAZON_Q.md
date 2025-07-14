# 🤖 App de Análise de Sentimentos - Fase 4 (Kafka)
*Documentação gerada com Amazon Q Developer*

## 📋 Visão Geral

Esta é a **fase mais avançada** do projeto de análise de sentimentos, implementando uma arquitetura **event-driven** com **Apache Kafka** para processamento assíncrono. O sistema utiliza **microserviços containerizados** com Docker, integrando:

- **Frontend**: Streamlit para interface do usuário
- **Backend**: FastAPI como API REST
- **Message Broker**: Apache Kafka para processamento assíncrono
- **Database**: MongoDB para persistência
- **IA**: OpenAI GPT para análise de sentimentos
- **Monitoring**: Kowl para visualização do Kafka

## 🏗️ Arquitetura do Sistema

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Streamlit  │───▶│   FastAPI   │───▶│    Kafka    │
│ (Frontend)  │    │ (Producer)  │    │   Topic     │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
┌─────────────┐    ┌─────────────┐          │
│   MongoDB   │◀───│   Consumer  │◀─────────┘
│ (Database)  │    │ (Processor) │
└─────────────┘    └─────────────┘
```

### Fluxo de Dados:
1. **Usuário** envia comentário via Streamlit
2. **FastAPI** recebe e envia para tópico Kafka
3. **Kafka Consumer** processa mensagem assincronamente
4. **OpenAI API** analisa sentimento do comentário
5. **MongoDB** armazena resultado processado
6. **Frontend** exibe feedbacks salvos

## 🐳 Serviços Docker

| Serviço | Porta | Descrição |
|---------|-------|-----------|
| **streamlit** | 8501 | Interface web do usuário |
| **fastapi** | 8000 | API REST e producer Kafka |
| **kafka** | 9092/29092 | Message broker |
| **zookeeper** | 2181 | Coordenação do Kafka |
| **mongodb** | 27017 | Banco de dados NoSQL |
| **kowl** | 8080 | Interface web do Kafka |
| **kafka_consumer** | - | Processador assíncrono |

## 🚀 Execução Rápida

### Opção 1: Docker Compose (Recomendado)
```bash
# Subir toda a infraestrutura
docker-compose up --build

# Acessar aplicação
http://localhost:8501  # Frontend
http://localhost:8000/docs  # API Docs
http://localhost:8080  # Kafka UI
```

### Opção 2: Desenvolvimento Local
```bash
# 1. Ativar ambiente virtual
.venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar .env (opcional)
echo "API_KEY=sua_chave_openai" > backend/.env

# 4. Executar orquestrador
python main.py
```

## 📁 Estrutura de Arquivos

```
fase_4_kafka/
├── backend/
│   ├── fast_api.py          # API REST + Kafka Producer
│   ├── kafka_consumer.py    # Consumidor assíncrono
│   ├── kafka_producer.py    # Produtor Kafka
│   ├── api_client.py        # Cliente OpenAI
│   ├── mongodb.py           # Conexão MongoDB
│   ├── config.py            # Configurações
│   └── requirements.txt     # Dependências backend
├── frontend/
│   ├── streamlit.py         # Interface Streamlit
│   └── requirements.txt     # Dependências frontend
├── docker-compose.yml       # Orquestração completa
├── main.py                  # Orquestrador local
└── README.md               # Documentação original
```

## 🔧 Componentes Principais

### 1. FastAPI Producer (`fast_api.py`)
- **Endpoint POST** `/feedback/`: Recebe comentários e envia para Kafka
- **Endpoint GET** `/get-feedback/`: Lista últimos 10 feedbacks processados
- **Kafka Integration**: Produz mensagens no tópico `feedback`

### 2. Kafka Consumer (`kafka_consumer.py`)
- **Processamento assíncrono** de mensagens do tópico `feedback`
- **Integração OpenAI** para análise de sentimentos
- **Persistência MongoDB** dos resultados processados
- **Error handling** e commit manual

### 3. Streamlit Frontend (`streamlit.py`)
- **Interface intuitiva** para envio de comentários
- **Visualização** de feedbacks processados
- **Tabs separadas** para envio e consulta

### 4. Kafka Producer (`kafka_producer.py`)
- **Auto-criação** de tópicos
- **Delivery reports** para monitoramento
- **Error handling** robusto

## ⚙️ Configurações Importantes

### Variáveis de Ambiente:
```bash
# OpenAI (opcional - usa mock se não definido)
API_KEY=sua_chave_openai
MOCK_OPENAPI_SERVICE=False

# Kafka
KAFKA_BROKER=kafka:29092

# MongoDB
MONGO_URI=mongodb://mongodb:27017/

# FastAPI Host
FASTAPI_HOST=fastapi
```

### Configuração OpenAI:
- **Modelo**: `gpt-4.1-mini` (custo-benefício)
- **Prompt**: Análise de sentimento em até 40 palavras
- **Status**: `aprovado` ou `reprovado`
- **Mock disponível** para desenvolvimento sem API key

## 🔍 Monitoramento

### Kowl (Kafka UI):
- **URL**: http://localhost:8080
- **Funcionalidades**:
  - Visualizar tópicos e mensagens
  - Monitorar consumers e lag
  - Debug de mensagens em tempo real

### Logs dos Containers:
```bash
# Ver logs específicos
docker-compose logs fastapi
docker-compose logs kafka_consumer
docker-compose logs kafka

# Logs em tempo real
docker-compose logs -f
```

## 🧪 Testando o Sistema

### 1. Enviar Comentário:
1. Acesse http://localhost:8501
2. Digite um comentário na aba "Enviar Comentário"
3. Selecione avaliação (1-5 estrelas)
4. Clique "Enviar"

### 2. Verificar Processamento:
1. Acesse aba "Ver Feedbacks"
2. Verifique se comentário foi processado
3. Observe análise de sentimento gerada

### 3. Monitorar Kafka:
1. Acesse http://localhost:8080
2. Visualize tópico `feedback`
3. Monitore mensagens sendo processadas

## 🚨 Troubleshooting

### Problemas Comuns:

**Kafka não conecta:**
```bash
# Verificar ordem de inicialização
docker-compose up zookeeper
docker-compose up kafka
docker-compose up kowl
```

**Consumer não processa:**
```bash
# Verificar logs do consumer
docker-compose logs kafka_consumer

# Reiniciar consumer
docker-compose restart kafka_consumer
```

**OpenAI API falha:**
```bash
# Ativar modo mock
echo "MOCK_OPENAPI_SERVICE=True" >> backend/.env
docker-compose restart fastapi kafka_consumer
```

## 💡 Vantagens da Arquitetura Kafka

### ✅ Benefícios:
- **Resiliência**: Falhas não perdem mensagens
- **Escalabilidade**: Múltiplos consumers podem processar
- **Desacoplamento**: Producer e consumer independentes
- **Auditoria**: Histórico completo de mensagens
- **Performance**: Processamento assíncrono

### 🎯 Casos de Uso:
- **Alto volume** de comentários
- **Processamento pesado** (IA/ML)
- **Múltiplos consumidores** (analytics, notifications)
- **Sistemas distribuídos**

## 🔄 Evolução do Projeto

| Fase | Tecnologias | Foco |
|------|-------------|------|
| **Fase 1** | Python + Streamlit | App básico |
| **Fase 2** | + Docker | Containerização |
| **Fase 3** | + MongoDB | Persistência |
| **Fase 4** | + Kafka | Event-driven |

## 📚 Próximos Passos

### Possíveis Melhorias:
- **Kubernetes** para orquestração
- **Redis** para cache
- **Elasticsearch** para busca
- **Prometheus** para métricas
- **Multiple consumers** para escalabilidade
- **Dead letter queue** para mensagens com erro

---

**🤖 Esta documentação foi gerada com Amazon Q Developer para facilitar o entendimento e uso do sistema de análise de sentimentos com arquitetura event-driven usando Kafka.**