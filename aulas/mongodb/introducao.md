# 🚀 Introdução ao MongoDB

## 📌 O que é o MongoDB?

MongoDB é um **banco de dados NoSQL orientado a documentos**, projetado para armazenar e processar grandes volumes de dados de forma escalável e flexível. Diferente dos bancos de dados relacionais (SQL), o MongoDB usa **documentos JSON-like (BSON)** em vez de tabelas, permitindo um armazenamento mais dinâmico e rápido.

### 🔹 Características do MongoDB:
✅ **Modelo de dados flexível** → Não exige esquema fixo como no SQL.  
✅ **Alta escalabilidade** → Pode ser distribuído horizontalmente em múltiplos servidores.  
✅ **Alto desempenho** → Processamento rápido de grandes volumes de dados.  
✅ **Facilidade de integração** → Compatível com diversas linguagens de programação.  
✅ **Alta disponibilidade** → Suporte a replicação e failover automático.  

---

## 🎯 SQL vs NoSQL: Qual a Diferença?

| Característica | SQL (Relacional) | NoSQL (MongoDB) |
|--------------|----------------|----------------|
| **Estrutura** | Tabelas com linhas e colunas | Documentos JSON-like (BSON) |
| **Esquema** | Estrito (precisa definir colunas e tipos) | Flexível (pode ter diferentes campos em cada documento) |
| **Escalabilidade** | Vertical (aumenta hardware do servidor) | Horizontal (distribui dados em vários servidores) |
| **Transações** | Suporte robusto a transações | Transações limitadas (mas com suporte desde versões recentes) |
| **Consultas** | SQL (SELECT, JOIN, etc.) | MongoDB Query Language (MQL) |

🔹 **MongoDB é ideal para aplicações modernas que precisam de escalabilidade e flexibilidade, como big data, IoT, aplicativos web e mobile.**

---

## ⚙️ Estrutura do MongoDB

### 🔸 **Database** (Banco de Dados)
Conjunto de **coleções** que armazenam os documentos.

### 🔸 **Collection** (Coleção)
Equivalente a uma tabela no SQL, mas sem esquema fixo.

### 🔸 **Document** (Documento)
Formato JSON-like (BSON) que contém os dados armazenados.
```json
{
  "nome": "Maria Silva",
  "idade": 30,
  "email": "maria@email.com"
}
```

---

## 📌 Principais Comandos do MongoDB

### 🔹 Criar um Banco de Dados:
```sh
use minha_base_de_dados
```

### 🔹 Criar uma Collection:
```sh
db.createCollection("usuarios")
```

### 🔹 Inserir um Documento:
```sh
db.usuarios.insertOne({ "nome": "João", "idade": 25, "email": "joao@email.com" })
```

### 🔹 Buscar Documentos:
```sh
db.usuarios.find()
```

### 🔹 Atualizar um Documento:
```sh
db.usuarios.updateOne({ "nome": "João" }, { $set: { "idade": 26 } })
```

### 🔹 Remover um Documento:
```sh
db.usuarios.deleteOne({ "nome": "João" })
```

---

## ▶️ Exemplo Prático: Rodando MongoDB com Docker

Criar um `docker-compose.yml` para rodar o MongoDB:

```yaml
version: '3.8'

services:
  mongodb:
    image: mongo:latest
    container_name: meu-mongo
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```

### 🔹 Subir o MongoDB com Docker:
```sh
docker-compose up -d
```

### 🔹 Conectar ao MongoDB via CLI:
```sh
docker exec -it meu-mongo mongosh
```

---

## ✅ Conclusão

MongoDB é uma poderosa alternativa aos bancos de dados relacionais, oferecendo **flexibilidade, desempenho e escalabilidade** para aplicações modernas. Sua estrutura baseada em documentos JSON-like facilita a integração com APIs e sistemas web.

Se você precisa de um banco de dados que lide bem com grandes volumes de dados e mudanças dinâmicas no esquema, **MongoDB é uma excelente escolha!** 🚀

🐳 **Bons estudos!**

## 📖 Documentação Oficial
[Acesse a documentação oficial do MongoDB](https://www.mongodb.com/docs/)
