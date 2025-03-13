# 📈 Aula 5: Funções em Python

## 📝 Introdução

Nesta aula, aprenderemos sobre **funções** em Python.

As funções são blocos de código reutilizáveis que ajudam a organizar e estruturar programas de maneira mais eficiente. Elas permitem evitar repetição de código, tornam o código mais legível e facilitam a manutenção.

Vamos explorar os principais conceitos:

1. **Definição de funções**
2. **Parâmetros e argumentos**
3. **Retorno de valores**
4. **Funções com valores padrão**
5. **Funções anônimas (`lambda`)**
6. **Escopo de variáveis**

---

## 📌 1. Criando uma Função

Em Python, uma função é definida usando a palavra-chave `def`, seguida pelo nome da função e parênteses.

### ✅ Exemplo básico de uma função:
```python
# Definição de uma função simples
def saudacao():
    print("Olá, seja bem-vindo!")

# Chamando a função
saudacao()
```

---

## 📌 2. Parâmetros e Argumentos

Funções podem receber **parâmetros**, permitindo que sejam mais flexíveis.

### ✅ Exemplo com parâmetro:
```python
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

# Chamando a função com argumentos diferentes
saudacao("Alice")
saudacao("Carlos")
```

### ✅ Função com múltiplos parâmetros:
```python
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)  # 8
```

---

## 📌 3. Retornando Valores com `return`

A palavra-chave `return` permite que uma função envie um valor de volta ao código que a chamou.

### ✅ Exemplo:
```python
def dobro(numero):
    return numero * 2

valor = dobro(4)
print(valor)  # 8
```

> Sem `return`, a função apenas executa o código, mas não devolve nenhum valor.

---

## 📌 4. Parâmetros com Valores Padrão

Se um argumento não for passado ao chamar a função, o valor padrão é utilizado.

### ✅ Exemplo:
```python
def apresentar(nome, idade=18):
    print(f"Nome: {nome}, Idade: {idade}")

apresentar("Ana")  # Nome: Ana, Idade: 18
apresentar("Pedro", 25)  # Nome: Pedro, Idade: 25
```

---

## 📌 5. Funções `lambda` (Funções Anônimas)

As funções **lambda** são funções anônimas em Python, ideais para operações rápidas e curtas. Elas são úteis quando precisamos de pequenas funções que serão usadas apenas uma vez ou como argumento para funções como `map()` e `filter()`.

A estrutura básica de uma função `lambda` é:

```python
lambda argumentos: expressão
```

---

### ✅ Exemplo 1: Multiplicando um número por 2

**Usando `lambda`:**
```python
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10
```

**Usando uma função normal:**
```python
def dobro(x):
    return x * 2

print(dobro(5))  # Saída: 10
```
---

### ✅ Exemplo 2: Filtrando números pares de uma lista com `filter()`

**Criando dados de teste:**
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Usando `lambda` com `filter()`:**
```python
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6, 8, 10]
```

**Usando uma função normal com `filter()`:**
```python
def eh_par(x):
    return x % 2 == 0

pares = list(filter(eh_par, numeros))
print(pares)  # Saída: [2, 4, 6, 8, 10]
```
---

### ✅ Exemplo 3: Transformando uma lista de números com `map()`

**Criando dados de teste:**
```python
numeros = [1, 2, 3, 4, 5]
```

**Usando `lambda` com `map()`:**
```python
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
```

**Usando uma função normal com `map()`:**
```python
def ao_quadrado(x):
    return x ** 2

quadrados = list(map(ao_quadrado, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
```

---

## 📌 6. Escopo de Variáveis

O escopo define onde uma variável pode ser acessada. 

### ✅ Exemplo:
```python
x = 10  # Variável global

def minha_funcao():
    x = 5  # Variável local
    print(x)  # 5

minha_funcao()
print(x)  # 10 (a variável global permanece inalterada)
```

---

## 🏆 Conclusão

- **Funções** permitem organizar o código e evitar repetição.
- **Parâmetros** tornam as funções mais flexíveis.
- **`return`** é usado para devolver valores de uma função.
- **Valores padrão** evitam erros ao chamar funções sem todos os argumentos.
- **Funções lambda** são úteis para expressões curtas.
- **Escopo de variáveis** define onde elas podem ser usadas.