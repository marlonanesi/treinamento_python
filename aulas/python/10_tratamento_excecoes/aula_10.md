# 📝 Aula 10: Tratamento de Exceções em Python

## 📌 Introdução

Erros são inevitáveis em qualquer programa. Para evitar que eles interrompam a execução do código, Python fornece mecanismos para capturar e tratar exceções. Nesta aula, abordaremos:

1. **O que são exceções?**
2. **Try, Except, Finally**
3. **Exceções genéricas vs. Exceções específicas**
4. **Criando exceções personalizadas**
5. **Melhores práticas para tratamento de erros**

---

## 📌 1. O que são Exceções?

Uma **exceção** é um erro que ocorre durante a execução do programa. Se não for tratada, o programa será interrompido.

### 🔹 Exemplo: Exceção não tratada
```python
numero = int(input("Digite um número: "))
print(10 / numero)  # Se o usuário digitar 0, gerará um erro de divisão por zero.
```
> **Erro:** `ZeroDivisionError: division by zero`

---

## 📌 2. Try, Except, Finally

O bloco `try-except` permite capturar exceções e evitar que o programa seja interrompido.

### 🔹 Exemplo: Tratando exceções
```python
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)
except ZeroDivisionError:
    print("Erro: Divisão por zero não permitida!")
except ValueError:
    print("Erro: Entrada inválida! Digite um número válido.")
finally:
    print("Finalizando a execução.")
```
> **O bloco `finally` sempre será executado, independentemente de erro.**

---

## 📌 3. Exceções Genéricas vs. Específicas

- **Exceções específicas** capturam erros específicos e oferecem mensagens mais precisas.
- **Exceções genéricas** capturam qualquer erro, mas podem ocultar detalhes importantes.

### ✅ Exemplo: Capturando exceções específicas
```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
```
> **Vantagem:** O erro específico `FileNotFoundError` fornece uma mensagem clara.

### ⚠️ Exemplo: Capturando exceção genérica
```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except Exception as e:
    print(f"Erro: {e}")
```
> **Desvantagem:** Captura qualquer erro, mas sem indicar qual foi.

**📌 Conclusão:** Prefira capturar exceções específicas sempre que possível.

---

## 📌 4. Criando Exceções Personalizadas

Podemos criar nossas próprias exceções herdando da classe `Exception`.

### 🔹 Exemplo: Criando uma exceção personalizada
```python
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f"Erro: Saldo insuficiente! Saldo atual: R$ {saldo}, Tentativa de saque: R$ {valor}")

# Simulando uma conta bancária
saldo = 100
valor_saque = 200

try:
    if valor_saque > saldo:
        raise SaldoInsuficienteError(saldo, valor_saque)
    saldo -= valor_saque
    print(f"Saque realizado. Novo saldo: R$ {saldo}")
except SaldoInsuficienteError as e:
    print(e)
```
> **Vantagem:** Exceções personalizadas tornam o código mais expressivo e fácil de depurar.

---

## 📌 5. Melhores Práticas para Tratamento de Erros

✔️ **Capture exceções específicas sempre que possível**
✔️ **Evite `except Exception` sem necessidade**
✔️ **Use `finally` para fechar conexões, arquivos ou liberar recursos**
✔️ **Crie exceções personalizadas quando necessário**
✔️ **Forneça mensagens de erro claras para o usuário**

---

## 🏆 Conclusão

- O tratamento de exceções evita que o programa pare inesperadamente.
- `try-except` permite capturar erros e tomar ações adequadas.
- Prefira exceções específicas para maior clareza.
- Exceções personalizadas ajudam a criar um código mais legível e robusto.