# 🏆 **Atividade Prática: Validando o Kafka**  

---

## 🎯 **Objetivo**  
Testar a comunicação entre **Producer** e **Consumer** no Kafka usando Docker.

---

## 🚀 **Passo a Passo**  

### 1⃣ **Subir o Docker Compose**  
Execute o comando abaixo para subir os serviços:  
```bash
docker-compose up --build
```

---

### 2⃣ **Produzir Mensagens no Kafka**  
Rode o **producer** para enviar mensagens ao tópico:  
```bash
python kafka_producer.py
```

---

### 3⃣ **Consumir Mensagens do Kafka**  
Rode o **consumer** para ler as mensagens do tópico:  
```bash
python kafka_consumer.py
```

---

## 🔎 **Testando e Observando**  
✔️ **Abra dois terminais lado a lado** para acompanhar o fluxo das mensagens.  
✔️ **Teste hipóteses** e observe o comportamento do Kafka.  

---

## 🌐 **Acessando o Kowl**  
📌 O **Kowl** pode ser acessado via: [localhost:8080](http://localhost:8080)  

💡 Se o Kowl não iniciar, rode novamente:  
```bash
docker-compose up --build
```
✅ Se apenas o Kowl não subiu, ele será iniciado na sequência.  

📣 *Nota*: O Kowl pode falhar ao iniciar junto com o Kafka no `docker-compose`.  

---

🚀 **Agora é sua vez de testar!**

