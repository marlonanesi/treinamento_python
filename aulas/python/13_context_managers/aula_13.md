# 📝 Aula 13: Gerenciadores de Contexto (`context managers`) em Python

## 📌 Introdução

Os **Gerenciadores de Contexto** (`context managers`) são recursos do Python que permitem o controle de recursos de forma eficiente e segura. Eles garantem que ações como **abrir arquivos, conexões com banco de dados e manipulação de recursos externos** sejam corretamente finalizadas, evitando vazamentos de memória e outros problemas.

Nesta aula, aprenderemos:

1. **O que são gerenciadores de contexto?**
2. **Usando `with` para gerenciar arquivos**
3. **Criando um gerenciador de contexto com classes**
4. **Criando um gerenciador de contexto com `contextlib`**
5. **Casos práticos de uso**

---

## 📌 1. O que são Gerenciadores de Contexto?

Os **gerenciadores de contexto** permitem que recursos sejam automaticamente liberados após seu uso. Isso evita a necessidade de fechamento manual e reduz a chance de erros.

> **Sintaxe:**
> ```python
> with expressão as variável:
>     bloco_de_codigo
> ```

### 🔹 Exemplo: Abertura e fechamento manual de arquivos **(Sem gerenciador de contexto)**
```python
arquivo = open("exemplo.txt", "w")
try:
    arquivo.write("Olá, mundo!")
finally:
    arquivo.close()  # Fechando manualmente
```
> **Problema:** Se houver um erro antes da linha `arquivo.close()`, o arquivo pode permanecer aberto.

---

## 📌 2. Usando `with` para Gerenciar Arquivos

A palavra-chave **`with`** simplifica o gerenciamento de arquivos e outros recursos.

### 🔹 Exemplo: Utilizando `with` para abrir arquivos corretamente
```python
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!")
# O arquivo é fechado automaticamente ao sair do bloco `with`
```
> **Vantagem:** Mesmo que ocorra um erro dentro do bloco, o arquivo será fechado corretamente.

---

## 📌 3. Criando um Gerenciador de Contexto com Classes

Podemos criar nossos próprios **gerenciadores de contexto** implementando os métodos `__enter__()` e `__exit__()`.

### 🔹 Exemplo: Criando um gerenciador de contexto para manipular arquivos
```python
class MeuGerenciador:
    def __init__(self, arquivo, modo):
        self.arquivo = arquivo
        self.modo = modo

    def __enter__(self):
        self.file = open(self.arquivo, self.modo)
        return self.file

    def __exit__(self, tipo, valor, traceback):
        self.file.close()
        print("Arquivo fechado corretamente!")

# Usando o gerenciador de contexto personalizado
with MeuGerenciador("teste.txt", "w") as f:
    f.write("Escrevendo no arquivo usando um gerenciador de contexto personalizado!")
```
> **Aqui, o método `__enter__()` abre o arquivo e `__exit__()` garante que ele seja fechado corretamente.**

---

## 📌 4. Criando um Gerenciador de Contexto com `contextlib`

A biblioteca `contextlib` permite criar gerenciadores de contexto de forma ainda mais simples, utilizando **funções geradoras**.

### 🔹 Exemplo: Criando um gerenciador de contexto com `contextlib`
```python
from contextlib import contextmanager

@contextmanager
def gerenciar_arquivo(nome_arquivo, modo):
    arquivo = open(nome_arquivo, modo)
    try:
        yield arquivo
    finally:
        arquivo.close()
        print("Arquivo fechado com sucesso!")

# Usando o gerenciador de contexto
with gerenciar_arquivo("exemplo2.txt", "w") as f:
    f.write("Usando contextlib para gerenciar arquivos!")
```
> **`contextmanager` simplifica a criação de gerenciadores de contexto sem precisar definir classes.**

---

## 📌 5. Casos Práticos de Uso

Os **gerenciadores de contexto** são úteis para diversas operações que exigem **inicialização e finalização controladas**.

✔️ **Abertura e fechamento de arquivos**
✔️ **Gerenciamento de conexões com banco de dados**
✔️ **Controle de locks (bloqueios de recursos)**
✔️ **Liberação de recursos em sistemas distribuídos**

### 🔹 Exemplo: Gerenciando conexões com um banco de dados
```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def conexao_banco(nome_bd):
    conexao = sqlite3.connect(nome_bd)
    cursor = conexao.cursor()
    try:
        yield cursor
    finally:
        conexao.commit()
        conexao.close()
        print("Conexão com o banco de dados encerrada!")

# Usando o gerenciador de contexto para banco de dados
with conexao_banco("meubanco.db") as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
    cursor.execute("INSERT INTO usuarios (nome) VALUES ('Alice')")
```
> **Garante que a conexão seja fechada corretamente após a execução dos comandos.**

---

## 🏆 Conclusão

- **Gerenciadores de contexto** evitam vazamento de recursos e tornam o código mais limpo.
- O uso de `with` facilita operações como **abrir e fechar arquivos automaticamente**.
- Podemos criar nossos próprios gerenciadores de contexto usando **classes (`__enter__()` e `__exit__()`)** ou **`contextlib` (`@contextmanager`)**.
- São úteis para **arquivos, banco de dados, conexões de rede e outros recursos externos**.

