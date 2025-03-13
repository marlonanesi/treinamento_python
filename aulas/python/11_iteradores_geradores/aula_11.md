# 📝 Aula 11: Iteradores e Geradores em Python

## 📌 Introdução

Os **iteradores** e **geradores** são conceitos fundamentais para manipulação eficiente de grandes volumes de dados em Python. Eles permitem que iteremos sobre coleções sem precisar carregar todos os elementos na memória ao mesmo tempo.

Nesta aula, aprenderemos:

1. **O que são iteradores?**
2. **Criando iteradores personalizados**
3. **O que são geradores?**
4. **Usando `yield` para criar geradores**
5. **Comparação entre iteradores e geradores**
6. **Casos práticos de uso**

---

## 📌 1. O que são Iteradores?

Um **iterador** é um objeto que implementa os métodos `__iter__()` e `__next__()`, permitindo percorrer uma sequência de valores um por um.

### 🔹 Exemplo: Utilizando um iterador padrão
```python
lista = [1, 2, 3]
iterador = iter(lista)

print(next(iterador))  # Saída: 1
print(next(iterador))  # Saída: 2
print(next(iterador))  # Saída: 3
print(next(iterador))  # Erro: StopIteration
```
> **Quando um iterador atinge o final da sequência, ele levanta uma exceção `StopIteration`.**

---

## 📌 2. Criando Iteradores Personalizados

Podemos criar nossos próprios iteradores implementando as funções `__iter__()` e `__next__()`.

### 🔹 Exemplo: Criando um iterador que gera números de 1 a N
```python
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0
    
    def __iter__(self):
        return self  # Retorna o próprio objeto iterador
    
    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration

meu_contador = Contador(5)
for numero in meu_contador:
    print(numero)
```
> **Iteradores são úteis para processar grandes quantidades de dados sem precisar armazená-los em memória.**

---

## 📌 3. O que são Geradores?

Os **geradores** são uma forma simplificada de criar iteradores em Python. Eles são definidos como funções e utilizam a palavra-chave `yield` para produzir valores sob demanda.

### 🔹 Exemplo: Criando um gerador
```python
def gerador_numeros(n):
    for i in range(1, n + 1):
        yield i

meu_gerador = gerador_numeros(5)
print(next(meu_gerador))  # Saída: 1
print(next(meu_gerador))  # Saída: 2
```
> **Os geradores pausam a execução e retomam de onde pararam ao chamar `next()`, economizando memória.**

---

## 📌 4. Usando `yield` para Criar Geradores

O `yield` funciona como um `return`, mas mantém o estado da função, permitindo que continue do ponto onde parou.

### 🔹 Exemplo: Gerando uma sequência infinita
```python
def gerador_infinito():
    num = 1
    while True:
        yield num
        num += 1

contador = gerador_infinito()
print(next(contador))  # Saída: 1
print(next(contador))  # Saída: 2
```
> **Diferente de listas, os geradores não ocupam espaço na memória para armazenar todos os valores de uma vez.**

---

## 📌 5. Comparação entre Iteradores e Geradores

| Característica | Iteradores | Geradores |
|--------------|------------|------------|
| Implementação | Classe com `__iter__()` e `__next__()` | Função com `yield` |
| Estado | Mantido manualmente | Mantido automaticamente |
| Uso de memória | Pode consumir muita memória | Usa memória sob demanda |
| Performance | Pode ser mais lento | Mais rápido para grandes volumes de dados |

> **Quando usar cada um?**
> - Use **iteradores** quando precisar de mais controle sobre o estado interno.
> - Use **geradores** quando quiser criar iteradores de forma mais eficiente.

---

## 📌 6. Casos Práticos de Uso

### 🔹 Lendo um arquivo linha por linha sem carregar tudo na memória
```python
def ler_arquivo_em_blocos(arquivo, tamanho=1024):
    with open(arquivo, 'r') as f:
        while bloco := f.read(tamanho):
            yield bloco

for bloco in ler_arquivo_em_blocos("grande_arquivo.txt"):
    print(bloco)
```
> **Ideal para lidar com arquivos grandes sem consumir muita memória.**

### 🔹 Criando um gerador para números primos
```python
def gerador_primos():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1

primos = gerador_primos()
print(next(primos))  # Saída: 2
print(next(primos))  # Saída: 3
print(next(primos))  # Saída: 5
```
> **Ótimo para gerar valores conforme necessário sem armazenar todos em memória.**

---

## 🏆 Conclusão

- **Iteradores** são objetos que permitem iterar sobre elementos um por um.
- **Geradores** são uma forma simplificada e eficiente de criar iteradores.
- **`yield`** permite pausar e retomar a execução da função, economizando memória.
- **Iteradores são úteis quando precisamos controlar manualmente a iteração.**
- **Geradores são ideais para processar grandes volumes de dados sob demanda.**