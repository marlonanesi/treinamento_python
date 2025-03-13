# 📈 Aula 4: Estruturas de Controle e Loops em Python

## 📝 Introdução

Nesta aula, aprenderemos sobre **estruturas de controle e loops** em Python.

As estruturas de controle permitem **repetir blocos de código** de forma eficiente e tomar **decisões lógicas** para controlar o fluxo do programa. Vamos explorar os principais comandos de repetição e controle de fluxo:

1. **Loop `for`**
2. **Loop `while`**
3. **Comandos de controle (`break`, `continue`, `pass`)**
4. **Compreensão de listas (`list comprehensions`)**

---

## 📉 1. Estruturas de Repetição (`for` e `while`)

Os **loops** são utilizados para **repetir instruções** sem precisar reescrever o mesmo código várias vezes.

---

## 📅 Loop `for`

O `for` é utilizado quando sabemos **quantas vezes** queremos repetir um bloco de código.

### ✅ Exemplo básico:
```python
for i in range(5):
    print(f"Repetição {i}")
```

o `range(5)` gera os valores `0, 1, 2, 3, 4`, executando o bloco 5 vezes.

### ✅ Iterando sobre listas:
```python
nomes = ["Alice", "Bob", "Carlos"]
for nome in nomes:
    print(f"Olá, {nome}!")
```

### ✅ Iterando sobre caracteres de uma string:
```python
palavra = "Python"
for letra in palavra:
    print(letra)
```

---

## 📆 Loop `while`

O `while` é usado quando **não sabemos exatamente** quantas repetições serão necessárias, mas queremos continuar até que uma condição seja falsa.

### ✅ Exemplo básico:
```python
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa o contador
```

a execução para quando `contador >= 5`.

### ✅ Solicitando entrada do usuário até um valor válido:
```python
senha = "python123"
digito = ""

while digito != senha:
    digito = input("Digite a senha: ")
print("Acesso concedido!")
```

---

## 🔄 Comandos de Controle (`break`, `continue`, `pass`)

### 💭 `break`
O `break` interrompe a repetição antes que a condição natural do loop seja atingida.

#### ✅ Exemplo:
```python
for numero in range(10):
    if numero == 5:
        break  # Sai do loop quando numero == 5
    print(numero)
```

### 💬 `continue`
O `continue` pula a iteração atual e passa para a próxima.

#### ✅ Exemplo:
```python
for numero in range(5):
    if numero == 2:
        continue  # Pula o número 2
    print(numero)
```

### 💭 `pass`
O `pass` é usado para **código ainda não implementado**, evitando erros de sintaxe.

#### ✅ Exemplo:
```python
for i in range(3):
    pass  # Lugar reservado para futuro código
```

---

## 🎯 List Comprehension - Criando Listas de Forma Inteligente  

A **List Comprehension** permite criar listas de maneira mais rápida e legível, reduzindo a necessidade de escrever múltiplas linhas de código com loops tradicionais.

### ✅ Exemplo: Criando uma lista de números dobrados  

**Sem List Comprehension:**
```python
numeros = [1, 2, 3, 4, 5]
dobrados = []
for num in numeros:
    dobrados.append(num * 2)
print(dobrados)  # [2, 4, 6, 8, 10]
```

**Com List Comprehension:**
```python
dobrados = [num * 2 for num in [1, 2, 3, 4, 5]]
print(dobrados)  # [2, 4, 6, 8, 10]
```

🚀 **Benefício**: Código mais curto e mais fácil de entender!

---

### ✅ Exemplo: Criando uma lista de palavras em maiúsculas  

**Sem List Comprehension:**
```python
nomes = ["ana", "carlos", "bia"]
maiusculas = []
for nome in nomes:
    maiusculas.append(nome.upper())
print(maiusculas)  # ['ANA', 'CARLOS', 'BIA']
```

**Com List Comprehension:**
```python
maiusculas = [nome.upper() for nome in ["ana", "carlos", "bia"]]
print(maiusculas)  # ['ANA', 'CARLOS', 'BIA']
```

---

### ✅ Exemplo com filtro condicional: Pegando apenas os números pares  

**Sem List Comprehension:**
```python
pares = []
for x in range(10):
    if x % 2 == 0:
        pares.append(x)
print(pares)  # [0, 2, 4, 6, 8]
```

**Com List Comprehension:**
```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

---

### ✅ Exemplo com condição `if-else`: Classificando números como "par" ou "ímpar"  

```python
classificacao = ["par" if x % 2 == 0 else "ímpar" for x in range(5)]
print(classificacao)  # ['par', 'ímpar', 'par', 'ímpar', 'par']
```

---

## 🏆 Conclusão

- O loop **`for`** é ideal para repetições com um número definido de iterações.
- O loop **`while`** é útil quando a repetição depende de uma condição.
- Os comandos **`break`**, **`continue`** e **`pass`** permitem controlar melhor a execução dos loops.
- A **list comprehension** oferece uma forma elegante e eficiente de criar listas baseadas em regras.

