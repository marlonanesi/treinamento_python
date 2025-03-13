# ✅ Boas Práticas no Uso do MongoDB

## 📌 1. Modelagem de Dados Adequada

- **Evite estrutura relacional** → MongoDB não é SQL, então evite modelagens com muitas referências e JOINs.
- **Use documentos aninhados quando necessário** → Armazene dados relacionados juntos para melhorar performance.
- **Evite documentos muito grandes** → Isso pode impactar a performance e consumo de memória.

**Exemplo (correto)**:
```json
{
  "usuario": "Maria",
  "email": "maria@email.com",
  "enderecos": [
    { "rua": "Av. Paulista", "cidade": "São Paulo" },
    { "rua": "Rua das Flores", "cidade": "Rio de Janeiro" }
  ]
}
```

**Exemplo (ruim - normalização excessiva)**:
```json
{
  "usuario": "Maria",
  "email": "maria@email.com",
  "enderecos": ["id_end_1", "id_end_2"]
}
```

---

## 📌 2. Indexação Inteligente

- **Sempre crie índices para consultas frequentes**.
- **Evite índices desnecessários** → Índices ocupam espaço e podem impactar a escrita.
- **Use índices compostos** para consultas que filtram por múltiplos campos.

**Criando um índice no campo `email`**:
```sh
db.usuarios.createIndex({ "email": 1 })
```

**Criando um índice composto para `email` e `status`**:
```sh
db.usuarios.createIndex({ "email": 1, "status": 1 })
```

Para visualizar índices:
```sh
db.usuarios.getIndexes()
```

---

## 📌 3. Evite Full Collection Scans

- **Nunca deixe consultas sem índices** → Elas podem resultar em varreduras na coleção inteira.
- **Sempre monitore consultas lentas**.

Verificar se uma query está usando índice:
```sh
db.usuarios.find({ "email": "maria@email.com" }).explain("executionStats")
```

---

## 📌 4. Sharding para Grandes Volumes de Dados

- **Use sharding para distribuir a carga** quando o banco crescer muito.
- **Escolha um shard key eficiente** para evitar hotspots (escolher um campo com boa distribuição de valores).

Habilitar sharding:
```sh
sh.enableSharding("meu_banco")
sh.shardCollection("meu_banco.usuarios", { "email": "hashed" })
```

---

## 📌 5. Use Aggregation Pipeline para Processamento Eficiente

- **Evite processar dados na aplicação** → Use a **Aggregation Pipeline** para manipular dados dentro do MongoDB.

Exemplo para contar usuários ativos por cidade:
```sh
db.usuarios.aggregate([
  { $match: { "status": "ativo" } },
  { $group: { "_id": "$cidade", "total": { $sum: 1 } } }
])
```

---

## 📌 6. Monitoramento e Backup

- **Use ferramentas como MongoDB Compass ou mongostat para monitorar o desempenho**.
- **Faça backups regulares**:

Criar backup de um banco:
```sh
mongodump --db meu_banco --out /backup/
```

Restaurar backup:
```sh
mongorestore /backup/meu_banco/
```

---

## ✅ Conclusão

MongoDB é poderoso, mas exige boas práticas para garantir performance e escalabilidade. Modelagem eficiente, indexação adequada e monitoramento contínuo são essenciais para um banco de dados bem otimizado! 🚀

🐳 **Bons estudos!**
