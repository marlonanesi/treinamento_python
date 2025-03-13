# 📝 Aula 6: Manipulação de Strings em Python

## 📌 Introdução

As **strings** são um dos tipos de dados mais usados em Python. Elas representam sequências de caracteres e podem ser manipuladas de diversas formas. Nesta aula, aprenderemos sobre:

1. **Declaração de strings**
2. **Acessando caracteres**
3. **Fatiamento (Slicing)**
4. **Principais métodos de string**
5. **Interpolação e formatação de strings**
6. **Strings e listas**

---

## 📌 1. Declaração de Strings

Em Python, strings podem ser declaradas com aspas simples (`'`), aspas duplas (`"`), ou triplas (`'''` ou `"""`) para textos multilinhas.

### ✅ Exemplo:
```python
s1 = 'Olá, mundo!'
s2 = "Python é incrível!"
s3 = '''Esta é uma string
com múltiplas linhas.'''
print(s1)
print(s2)
print(s3)
```

---

## 📌 2. Acessando Caracteres

Podemos acessar caracteres individuais de uma string usando **índices**.

### ✅ Exemplo:
```python
texto = "Python"
print(texto[0])  # P
print(texto[3])  # h
print(texto[-1])  # Último caractere: n
```

> **Observação:** Os índices começam em `0` e números negativos percorrem a string de trás para frente.

---

## 📌 3. Fatiamento (Slicing)

Podemos extrair partes de uma string usando a sintaxe `[inicio:fim:passo]`.

### ✅ Exemplo:
```python
frase = "Manipulação de Strings"
print(frase[0:10])   # 'Manipulaç'
print(frase[:10])    # Do início até o 10º caractere
print(frase[5:])     # A partir do 5º caractere até o final
print(frase[::2])    # Pulando de 2 em 2
print(frase[::-1])   # String invertida
```

> **Dica:** `[::-1]` inverte a string completamente.

---

## 📌 4. Principais Métodos de String

Python oferece diversos métodos para manipular strings:

### 🔹 **Alteração de Case**
```python
s = "python"
print(s.upper())  # 'PYTHON'
print(s.lower())  # 'python'
print(s.title())  # 'Python'
print(s.capitalize())  # 'Python'
```

### 🔹 **Removendo Espaços**
```python
s = "  exemplo  "
print(s.strip())  # 'exemplo' (remove espaços no início e fim)
print(s.lstrip())  # 'exemplo  ' (remove apenas da esquerda)
print(s.rstrip())  # '  exemplo' (remove apenas da direita)
```

### 🔹 **Substituição e Busca**
```python
s = "Python é incrível!"
print(s.replace("incrível", "poderoso"))  # 'Python é poderoso!'
print(s.find("é"))  # Retorna o índice de 'é'
print("Python" in s)  # True (verifica se existe na string)
```

### 🔹 **Quebrando e Juntando Strings**
```python
s = "Python é fácil e poderoso"
lista_palavras = s.split()  # Divide por espaços
print(lista_palavras)  # ['Python', 'é', 'fácil', 'e', 'poderoso']

nova_string = "-".join(lista_palavras)  # Junta usando '-'
print(nova_string)  # 'Python-é-fácil-e-poderoso'
```

---

## 📌 5. Interpolação e Formatação de Strings

Podemos formatar strings de diferentes formas:

### 🔹 **Usando `f-strings` (Python 3.6+)**
```python
nome = "Alice"
idade = 25
print(f"Meu nome é {nome} e tenho {idade} anos.")
```

### 🔹 **Usando `.format()`**
```python
print("Meu nome é {} e tenho {} anos.".format(nome, idade))
```

### 🔹 **Usando `%` (antiga, mas ainda usada)**
```python
print("Meu nome é %s e tenho %d anos." % (nome, idade))
```

---

## 📌 6. Strings e Listas

Strings podem ser transformadas em listas e vice-versa.

### ✅ Exemplo:
```python
s = "Python"
lista = list(s)  # Transforma string em lista de caracteres
print(lista)  # ['P', 'y', 't', 'h', 'o', 'n']

string_nova = "".join(lista)  # Junta de volta em string
print(string_nova)  # 'Python'
```

---

## 🏆 Conclusão

- Strings são **imutáveis**, ou seja, não podem ser modificadas diretamente.
- Podemos acessar caracteres individuais ou **fatiar** strings.
- Python oferece diversos **métodos úteis** para manipulação de strings.
- A formatação pode ser feita com **f-strings**, `.format()` ou `%`.
- Strings podem ser convertidas em listas e vice-versa para manipulação avançada.