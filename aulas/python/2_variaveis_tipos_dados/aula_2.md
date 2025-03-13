# 📌 Aula 2: Variáveis e Tipos de Dados em Python

## 📝 Introdução

Nesta aula, aprenderemos sobre **variáveis** e **tipos de dados** em Python.
As variáveis são usadas para armazenar informações e os tipos de dados determinam o tipo de valor que pode ser armazenado e manipulado.

---

## 🔹 O que são Variáveis?

Uma **variável** é um espaço reservado na memória para armazenar um valor.
Em Python, não é necessário declarar o tipo da variável explicitamente.

### ✅ Exemplo de atribuição de variáveis:

```python
nome = "Alice"  # String (Texto)
idade = 25       # Inteiro (int)
altura = 1.75    # Float (Número decimal)
ativo = True     # Booleano (Verdadeiro/Falso)
```

### 🔹 Regras para nomear variáveis:
- Pode conter letras, números e **_** (underline), mas **não pode começar com número**.
- Sensível a maiúsculas e minúsculas (`idade` e `Idade` são variáveis diferentes).
- Não pode ser uma palavra reservada do Python (ex: `class`, `def`, `if`).

---

## 🔹 Tipos de Dados em Python

### 1️⃣ **Tipo Numérico**
Representa números inteiros e decimais.

| Tipo     | Descrição          | Exemplo  |
|----------|------------------|---------|
| `int`    | Números inteiros  | `10, -5, 200` |
| `float`  | Números decimais  | `3.14, -0.5, 10.0` |

### ✅ Exemplo:
```python
numero_inteiro = 10
numero_decimal = 3.14
print(type(numero_inteiro))  # <class 'int'>
print(type(numero_decimal))  # <class 'float'>
```

---

### 2️⃣ **Tipo Texto (String)**
Armazena sequências de caracteres.

### ✅ Exemplo:
```python
frase = "Aprendendo Python!"
print(frase)
print(type(frase))  # <class 'str'>
```

**Concatenando Strings:**
```python
nome = "Carlos"
mensagem = "Olá, " + nome + "!"
print(mensagem)
```

**Interpolação usando f-strings:**
```python
idade = 30
mensagem = f"Eu tenho {idade} anos."
print(mensagem)
```

---

### 3️⃣ **Tipo Booleano (bool)**
Valores **True** (Verdadeiro) ou **False** (Falso).

### ✅ Exemplo:
```python
ativo = True
print(type(ativo))  # <class 'bool'>
```

**Usando booleanos em comparações:**
```python
idade = 18
maior_de_idade = idade >= 18
print(maior_de_idade)  # True
```

---

### 4️⃣ **Tipo Lista (list)**
Estrutura para armazenar vários valores.

### ✅ Exemplo:
```python
nomes = ["Alice", "Bob", "Carlos"]
print(nomes[0])  # Alice
print(len(nomes))  # Número de elementos na lista
```

**Modificando listas:**
```python
nomes.append("Daniel")  # Adiciona um novo nome
print(nomes)
```

---

### 5️⃣ **Tipo Tupla (tuple)**
Semelhante à lista, mas **imutável** (não pode ser alterada).

### ✅ Exemplo:
```python
cores = ("vermelho", "azul", "verde")
print(cores[1])  # azul
```

---

### 6️⃣ **Tipo Dicionário (dict)**
Armazena pares **chave: valor**.

### ✅ Exemplo:
```python
pessoa = {"nome": "Alice", "idade": 25, "altura": 1.65}
print(pessoa["nome"])  # Alice
```

---

### 7️⃣ **Tipo Conjunto (set)**
Armazena elementos únicos e sem ordem específica.

### ✅ Exemplo:
```python
numeros = {1, 2, 3, 4, 4, 5}
print(numeros)  # {1, 2, 3, 4, 5} (não repete o 4)
```

---

## 🚀 Exercícios Rápidos

Tente prever o que será impresso antes de rodar os códigos:

**1️⃣ O que será impresso?**
```python
x = "Python"
y = " é incrível!"
print(x + y)
```

**2️⃣ Qual o tipo de dado de `resultado`?**
```python
resultado = 10 > 5
print(type(resultado))
```

**3️⃣ Como acessar o valor "Carlos" dentro da lista abaixo?**
```python
nomes = ["Alice", "Bob", "Carlos"]
```

---

## 🏆 Conclusão

- **Variáveis armazenam valores e podem mudar ao longo do programa.**
- **Python define o tipo de dado automaticamente (tipagem dinâmica).**
- **Principais tipos de dados: int, float, str, bool, list, tuple, dict, set.**
- **Entender os tipos de dados é essencial para escrever código eficiente.**

