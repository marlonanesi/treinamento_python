# 📝 Aula 14: Concorrência e Paralelismo em Python

## 📌 Introdução

A **concorrência** e o **paralelismo** são conceitos essenciais para melhorar a eficiência de programas que realizam múltiplas tarefas simultaneamente. Python oferece diferentes abordagens para lidar com essas tarefas, como **threads, multiprocessamento e programação assíncrona**.

Nesta aula, aprenderemos:

1. **Concorrência vs. Paralelismo: Qual a diferença?**
2. **Trabalhando com `threading` (multithreading)**
3. **Usando `multiprocessing` para tarefas paralelas**
4. **Programação assíncrona com `asyncio`**
5. **Comparação entre abordagens e melhores práticas**

---

## 📌 1. Concorrência vs. Paralelismo: Qual a diferença?

- **Concorrência**: Múltiplas tarefas são executadas de maneira intercalada, compartilhando um mesmo processador.
- **Paralelismo**: Múltiplas tarefas são executadas ao mesmo tempo, utilizando múltiplos processadores ou núcleos.

### 🔹 Exemplo:
- **Concorrência**: Um caixa de supermercado atendendo vários clientes ao mesmo tempo, alternando entre cada um.
- **Paralelismo**: Vários caixas atendendo clientes simultaneamente.

> **Python suporta concorrência via `threading` e paralelismo via `multiprocessing`.**

---

## 📌 2. Trabalhando com `threading` (Multithreading)

O módulo `threading` permite criar **múltiplas threads**, permitindo que tarefas sejam executadas de forma concorrente.

### 🔹 Exemplo: Criando múltiplas threads
```python
import threading
import time

def tarefa(nome):
    print(f"Iniciando {nome}...")
    time.sleep(2)
    print(f"Finalizando {nome}...")

# Criando threads
thread1 = threading.Thread(target=tarefa, args=("Thread 1",))
thread2 = threading.Thread(target=tarefa, args=("Thread 2",))

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando todas as threads finalizarem
thread1.join()
thread2.join()
print("Todas as threads finalizaram!")
```
> **Multithreading é útil para tarefas que dependem de I/O, como requisições de rede e leitura/escrita de arquivos.**

---

## 📌 3. Usando `multiprocessing` para tarefas paralelas

O módulo `multiprocessing` permite executar tarefas em **processos separados**, aproveitando múltiplos núcleos da CPU para obter paralelismo real.

### 🔹 Exemplo: Criando múltiplos processos
```python
import multiprocessing
import time

def tarefa(nome):
    print(f"Iniciando {nome}...")
    time.sleep(2)
    print(f"Finalizando {nome}...")

# Criando processos
processo1 = multiprocessing.Process(target=tarefa, args=("Processo 1",))
processo2 = multiprocessing.Process(target=tarefa, args=("Processo 2",))

# Iniciando os processos
processo1.start()
processo2.start()

# Aguardando todos os processos finalizarem
processo1.join()
processo2.join()
print("Todos os processos finalizaram!")
```
> **Multiprocessing é ideal para tarefas que exigem processamento intensivo da CPU, como cálculos matemáticos complexos.**

---

## 📌 4. Programação Assíncrona com `asyncio`

O módulo `asyncio` permite criar programas assíncronos, onde múltiplas tarefas podem ser executadas sem bloqueio.

### 🔹 Exemplo: Criando uma função assíncrona com `asyncio`
```python
import asyncio

async def tarefa(nome):
    print(f"Iniciando {nome}...")
    await asyncio.sleep(2)  # Simula uma operação assíncrona
    print(f"Finalizando {nome}...")

async def main():
    await asyncio.gather(tarefa("Tarefa 1"), tarefa("Tarefa 2"))

print("\n🔹 Exemplo de Asyncio")
asyncio.run(main())
```
> **Asyncio é útil para tarefas que envolvem operações de I/O, como chamadas a APIs e interações com bancos de dados assíncronos.**

---

## 📌 5. Comparação entre Abordagens e Melhores Práticas

| Método            | Concorrência/Paralelismo | Melhor Uso  |
|------------------|----------------------|------------|
| `threading`      | Concorrência         | Operações de I/O (como rede, arquivos) |
| `multiprocessing`| Paralelismo          | Tarefas de CPU intensivas |
| `asyncio`        | Concorrência         | Operações assíncronas (chamadas a APIs, banco de dados) |

✔️ **Use `threading` para I/O-bound (operações de entrada e saída, como redes e arquivos).**
✔️ **Use `multiprocessing` para CPU-bound (tarefas intensivas de processamento).**
✔️ **Use `asyncio` para operações assíncronas que não bloqueiam a execução.**

---

## 🏆 Conclusão

- **Concorrência** permite que múltiplas tarefas sejam executadas intercaladas no mesmo processador.
- **Paralelismo** permite que múltiplas tarefas sejam executadas simultaneamente em múltiplos processadores.
- O Python suporta concorrência via **`threading`**, paralelismo via **`multiprocessing`**, e programação assíncrona via **`asyncio`**.
- Escolha a abordagem certa para cada tipo de problema!