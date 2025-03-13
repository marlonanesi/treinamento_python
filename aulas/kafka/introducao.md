# 🚀 **Introdução ao Apache Kafka**

---

## 📌 O que é o Kafka?

O **Apache Kafka** é uma plataforma de **mensageria distribuída e orientada a eventos**, projetada para processar e transmitir grandes volumes de dados em **tempo real**. Criado originalmente pelo **LinkedIn**, ele se tornou essencial para sistemas distribuídos modernos, sendo amplamente adotado por empresas como **Netflix, Uber, Airbnb e Twitter**.

### 🔹 Características do Kafka:
✅ **Alta escalabilidade** → Capaz de lidar com **milhões de mensagens por segundo**.  
✅ **Alta disponibilidade** → Distribui mensagens entre múltiplos servidores para garantir resiliência.  
✅ **Baixa latência** → Comunicação rápida entre serviços.  
✅ **Desacoplamento de sistemas** → Facilita a **integração assíncrona** entre módulos e microsserviços.  

---

## 🎯 Grandes Empresas que Usam o Kafka

- **Netflix** → Utiliza Kafka para **monitoramento de eventos**, recomendações e análise de comportamento do usuário.  
- **Uber** → Usa Kafka para processar **milhões de transações** e coordenar localizações de motoristas.  
- **Airbnb** → Garante **coerência de dados em tempo real** e sincroniza informações entre serviços.  
- **Twitter** → Usa Kafka para **coletar e processar tweets em tempo real**.  

---

## 🌟 Principais Casos de Uso do Kafka

🔹 **Processamento de Eventos em Tempo Real** → Monitoramento de logs, sensores IoT e análise de cliques de usuários.  
🔹 **Integração de Sistemas** → Atua como **backbone** de dados para conectar aplicações heterogêneas.  
🔹 **Streaming de Dados** → Processamento contínuo de **métricas, dados financeiros e transações**.  
🔹 **Log Distribuído** → Permite **auditoria** e **rastreamento de eventos** dentro de sistemas distribuídos.  

---

## ⚙️ Componentes Principais do Kafka

### 🔸 **Producer** (Produtor)
Os **producers** enviam mensagens para os tópicos do Kafka.
```python
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('meu_topico', b'Mensagem de exemplo')
```

### 🔸 **Topics** (Tópicos)
Os **tópicos** armazenam mensagens e funcionam como um canal entre producers e consumers.  
- As mensagens dentro de um tópico são **ordenadas e persistentes**.  
- Podem ser **particionados** para distribuição de carga.  

### 🔸 **Consumer** (Consumidor)
Os **consumers** leem mensagens dos tópicos do Kafka.
```python
from kafka import KafkaConsumer

consumer = KafkaConsumer('meu_topico', bootstrap_servers='localhost:9092')
for mensagem in consumer:
    print(f'Recebido: {mensagem.value.decode()}')
```

### 🔸 **Broker** (Corretor)
Os **brokers** armazenam e distribuem mensagens.  
- Um **cluster Kafka** pode ter **múltiplos brokers** para garantir escalabilidade e resiliência.  

### 🔸 **Zookeeper**
Responsável por coordenar os brokers e manter metadados do cluster.  

---

## ▶️ Exemplo Prático: Subindo o Kafka com Docker

Crie um arquivo `docker-compose.yml` para subir um cluster Kafka:

```yaml
version: '3.8'

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
    ports:
      - "2181:2181"

  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_LISTENERS: PLAINTEXT://:9092
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    ports:
      - "9092:9092"
```

### 🔹 Subir o Kafka:
```sh
docker-compose up -d
```

### 🔹 Criar um tópico Kafka:
```sh
docker exec -it <id_do_container_kafka> kafka-topics --create --topic meu_topico --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

### 🔹 Listar tópicos:
```sh
docker exec -it <id_do_container_kafka> kafka-topics --list --bootstrap-server localhost:9092
```

---

## 📌 Kafka vs Outras Tecnologias de Mensageria

| Característica  | Kafka  | RabbitMQ  | ActiveMQ  |
|--------------|--------|---------|---------|
| **Escalabilidade** | Alta  | Média  | Baixa  |
| **Desempenho** | Excelente  | Médio  | Baixo  |
| **Persistência** | Sim  | Opcional  | Sim  |
| **Latência** | Baixa  | Média  | Alta  |

💡 **Kafka** é a melhor opção para grandes volumes de dados e sistemas distribuídos.

---

## ✅ Conclusão

O **Apache Kafka** é uma solução robusta para **streaming de dados, mensageria e processamento de eventos em tempo real**. Seu modelo distribuído garante **alta disponibilidade, escalabilidade e confiabilidade**.

Se você precisa **integrar serviços, processar grandes volumes de dados ou criar sistemas baseados em eventos**, o **Kafka é a escolha ideal!** 🚀

🐳 **Bons estudos!**

---

## 📖 Documentação Oficial
[Acesse a documentação oficial do Apache Kafka](https://kafka.apache.org/documentation/)

