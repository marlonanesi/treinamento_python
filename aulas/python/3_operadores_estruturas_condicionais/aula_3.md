# 📈 Aula 3: Operadores e Estruturas Condicionais em Python

## 📝 Introdução

Nesta aula, aprenderemos sobre **operadores e estruturas condicionais** em Python.

Os operadores permitem manipular valores, realizar cálculos, comparar valores e construir expressões lógicas. Já as **estruturas condicionais** permitem que nosso código tome decisões com base em condições específicas.

---

## 🔹 Tipos de Operadores em Python

1. **Aritméticos**
2. **Comparativos**
3. **Lógicos**
4. **Atribuição**
5. **Identidade**
6. **Pertinência**

---

## 📌 1. Operadores Aritméticos

Usados para realizar operações matemáticas.

| Operador | Descrição       | Exemplo  |
|----------|-----------------|----------|
| `+`      | Adição          | `10 + 5` → `15` |
| `-`      | Subtração       | `10 - 5` → `5`  |
| `*`      | Multiplicação   | `10 * 5` → `50` |
| `/`      | Divisão         | `10 / 3` → `3.333` |
| `//`     | Divisão Inteira | `10 // 3` → `3` |
| `%`      | Módulo (Resto)  | `10 % 3` → `1` |
| `**`     | Expoente        | `2 ** 3` → `8` |

### ✅ Exemplo prático:
```python
x = 10
y = 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.333
print(x // y)  # 3
print(x % y)  # 1
print(x ** y)  # 1000
```

---

## 📌 2. Operadores Comparativos

Comparam valores e retornam **True** ou **False**.

| Operador | Descrição       | Exemplo  |
|----------|----------------|---------|
| `==`     | Igual          | `10 == 5` → `False` |
| `!=`     | Diferente      | `10 != 5` → `True` |
| `>`      | Maior que      | `10 > 5` → `True` |
| `<`      | Menor que      | `10 < 5` → `False` |
| `>=`     | Maior ou igual | `10 >= 10` → `True` |
| `<=`     | Menor ou igual | `10 <= 5` → `False` |

### ✅ Exemplo prático:
```python
idade = 18
print(idade >= 18)  # True
print(idade < 21)  # True
print(idade == 18)  # True
print(idade != 17)  # True
```

---

## 📌 3. Operadores Lógicos

Combinam expressões lógicas.

| Operador | Descrição                | Exemplo  |
|----------|----------------------|---------|
| `and`    | Retorna **True** se ambas as condições forem verdadeiras | `(10 > 5) and (5 > 2)` → `True` |
| `or`     | Retorna **True** se pelo menos uma condição for verdadeira | `(10 > 5) or (5 < 2)` → `True` |
| `not`    | Inverte o valor lógico | `not (10 > 5)` → `False` |

---

## 📌 4. Operadores de Atribuição

Atribuem valores a variáveis.

| Operador | Exemplo  | Equivalente a |
|----------|---------|--------------|
| `=`      | `x = 5` | `x = 5` |
| `+=`     | `x += 3` | `x = x + 3` |
| `-=`     | `x -= 2` | `x = x - 2` |
| `*=`     | `x *= 4` | `x = x * 4` |
| `/=`     | `x /= 3` | `x = x / 3` |
| `%=`     | `x %= 3` | `x = x % 3` |

---

## 📌 5. Operadores de Identidade

Comparam objetos na memória.

| Operador | Descrição     | Exemplo  |
|----------|--------------|---------|
| `is`     | Retorna **True** se as variáveis apontarem para o mesmo objeto | `x is y` |
| `is not` | Retorna **True** se as variáveis apontarem para objetos diferentes | `x is not y` |

---

## 📌 6. Operadores de Pertinência

Verificam se um valor está presente em uma estrutura de dados.

| Operador | Descrição     | Exemplo  |
|----------|--------------|---------|
| `in`     | Retorna **True** se o valor estiver presente | `'a' in 'banana'` |
| `not in` | Retorna **True** se o valor não estiver presente | `'x' not in 'python'` |

---

## 📌 Estruturas Condicionais

As **estruturas condicionais** permitem que o código tome decisões com base em condições específicas. Elas funcionam como um **fluxo de decisão**, onde o programa executa um bloco de código dependendo da condição avaliada.

### ✅ Como funciona `if`, `elif`, `else`?

- **`if`**: Executa um bloco de código se a condição for verdadeira.
- **`elif`** (else if): Permite adicionar verificações extras, caso a primeira condição não seja atendida.
- **`else`**: Executa um bloco de código caso nenhuma das condições anteriores seja verdadeira.

### ✅ Exemplo de `if`, `elif`, `else`:
```python
idade = 18
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem exatamente 18 anos")
else:
    print("Maior de idade")
```

### ✅ Operador Ternário (Expressão Condicional)
O **operador ternário** é uma forma mais compacta de escrever um `if` simples.

#### 🔄 Forma convencional:
```python
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
```

#### 🔄 Forma alternativa usando `and` e `or`:
```python
idade = 20
status = idade >= 18 and "Maior de idade" or "Menor de idade"
print(status)
```

---

## 🏆 Conclusão

- **Python permite realizar operações matemáticas, lógicas e estruturais facilmente.**
- **Expressões condicionais permitem que programas tomem decisões baseadas em condições lógicas.**
- **Operadores bitwise permitem manipular bits diretamente.**
- **Expressões ternárias permitem escrita concisa de condições simples.**