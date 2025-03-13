# 🚀 Tuning no MongoDB: Otimizando Performance

## 📌 Introdução

MongoDB é altamente eficiente para grandes volumes de dados, mas sem a configuração correta pode sofrer com consultas lentas e alto consumo de recursos. **O tuning é essencial** para garantir alto desempenho e escalabilidade.

Nesta aula, abordaremos **boas práticas e técnicas de otimização** como:
- Uso correto de **índices simples e compostos**
- **Hinting** para melhorar a escolha de índices
- Monitoramento e análise de consultas
- Estratégias de **sharding e replicação**

---

## 🔍 1. Monitoramento de Consultas Lentas

Antes de otimizar, precisamos identificar gargalos. MongoDB possui ferramentas para isso:

### 📊 **Visualizando consultas lentas**
Habilitar logs para consultas que demoram mais de 100ms:
```sh
db.setProfilingLevel(1, 100)
```
Ver logs de queries lentas:
```sh
db.system.profile.find().sort({ ts: -1 }).limit(5).pretty()
```

### 📊 **Analisando um plano de execução**
Podemos verificar como MongoDB processa uma query e se está usando um índice:
```sh
db.usuarios.find({ "email": "maria@email.com" }).explain("executionStats")
```
Se `COLLSCAN` aparecer, significa que a busca está escaneando toda a coleção, o que é ruim. Precisamos de **índices** para evitar isso.

---

## 📌 2. Índices: Simples vs Compostos

Os **índices** aceleram consultas ao permitir busca eficiente nos dados.

### 🔹 **Índice Simples**
Criado em apenas um campo:
```sh
db.usuarios.createIndex({ "email": 1 })
```
Útil quando buscamos frequentemente pelo campo `email`.

### 🔹 **Índice Composto**
Criado em múltiplos campos:
```sh
db.usuarios.createIndex({ "email": 1, "status": 1 })
```
🔹 **Quando usar índices compostos?**
- Quando consultas filtram ou ordenam por **múltiplos campos**.
- Se `email` e `status` forem usados juntos em muitas consultas.

Ver índices existentes:
```sh
db.usuarios.getIndexes()
```

Remover um índice se não for mais útil:
```sh
db.usuarios.dropIndex("email_1_status_1")
```

---

## 📌 3. Forçando o Uso de Índices com `hint()`

Em alguns casos, o **otimizador de índices do MongoDB pode não escolher o melhor índice**. Se soubermos que um índice específico é melhor para uma consulta, podemos usar `hint()` para forçar seu uso.

### 🔹 Exemplo de Hinting
```sh
db.usuarios.find({ "email": "maria@email.com" }).hint("email_1").explain("executionStats")
```
Isso força MongoDB a usar o índice `email_1` e mostra estatísticas da execução.

Outro exemplo para um índice composto:
```sh
db.usuarios.find({ "email": "maria@email.com", "status": "ativo" }).hint("email_1_status_1")
```

Use `hint()` **somente se necessário**, pois pode prejudicar o desempenho se usado incorretamente.

---

## 📌 4. Estratégias de Sharding e Replicação

Se o banco crescer muito, otimizar apenas índices pode não ser suficiente. MongoDB permite **sharding e replicação** para escalabilidade.

### 🔹 **Sharding (Distribuição Horizontal)**
- Distribui dados entre vários servidores.
- Ideal para grandes volumes de dados.
- Exemplo de habilitação de sharding:
```sh
sh.enableSharding("meu_banco")
sh.shardCollection("meu_banco.usuarios", { "email": "hashed" })
```

### 🔹 **Replica Sets (Alta Disponibilidade)**
- Cópias dos dados são mantidas em servidores diferentes.
- Permite failover automático em caso de falha.
- Criando um Replica Set:
```sh
rs.initiate()
```

---

## 📌 5. Outras Boas Práticas de Performance

✅ **Evite full collection scans** → Sempre use índices para melhorar buscas.  
✅ **Mantenha o banco enxuto** → Delete registros desnecessários periodicamente.  
✅ **Use `projection` para buscar apenas os campos necessários**:
```sh
db.usuarios.find({}, { "nome": 1, "email": 1 })
```
✅ **Evite $regex em campos não indexados** → Pode causar scans completos:
```sh
db.usuarios.find({ "email": /@gmail.com$/ })
```
✅ **Compacte e reindexe periodicamente**:
```sh
db.collection.reIndex()
```

---

## ✅ Conclusão

MongoDB é poderoso, mas sem otimizações pode sofrer com performance. O uso correto de **índices, hinting e sharding** ajuda a manter **consultas rápidas e eficientes**.

Sempre **monitore suas queries**, crie índices adequados e utilize técnicas de **tuning** para manter o banco rodando de forma otimizada! 🚀

🔹 **Dúvidas? Comente e participe!**

🐳 **Bons estudos!**
