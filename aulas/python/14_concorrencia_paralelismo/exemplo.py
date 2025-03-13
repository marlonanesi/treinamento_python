# 🔹 Comparação Didática: Concorrência e Paralelismo em Python

import threading
import multiprocessing
import asyncio
import time

# 📌 Exemplo 1: Concorrência com Threading
print("\n🔹 Exemplo de Concorrência com Threading")

def tarefa(nome, contador):
    """
    Função executada pelas threads/processos.
    :param nome: Nome identificador da thread/processo
    :param contador: Número de iterações da tarefa
    """
    print(f"Iniciando {nome}...")
    for i in range(contador):
        time.sleep(0.5)
        print(f"{nome}: {i+1}")
    print(f"Finalizando {nome}...")

def escrever_frase(nome, frase):
    """
    Função que escreve uma frase palavra por palavra para demonstrar concorrência.
    :param nome: Nome identificador da thread
    :param frase: Frase a ser escrita
    """
    palavras = frase.split()
    for palavra in palavras:
        time.sleep(0.5)
        print(f"{nome}: {palavra}")

if __name__ == "__main__":
    inicio = time.time()

    # Criando múltiplas threads
    # target=tarefa -> Define a função que será executada pela thread
    # args=("Thread 1", 4) -> Passa os argumentos para a função tarefa
    thread1 = threading.Thread(target=escrever_frase, args=("Frase 1", "Python é incrível para concorrência"))
    thread2 = threading.Thread(target=escrever_frase, args=("Frase 2", "Threads ajudam a rodar tarefas simultâneas"))

    # Iniciando as threads
    thread1.start()
    thread2.start()

    # join() -> Aguarda a finalização da thread antes de continuar
    thread1.join()
    thread2.join()

    fim = time.time()
    print(f"Todas as threads finalizaram em {fim - inicio:.2f} segundos!\n")

    # 📌 Exemplo 2: Paralelismo com Multiprocessing
    print("\n🔹 Exemplo de Paralelismo com Multiprocessing")

    inicio = time.time()

    # Criando processos (semelhante às threads, mas rodando em núcleos separados)
    processo1 = multiprocessing.Process(target=tarefa, args=("Processo 1", 4))
    processo2 = multiprocessing.Process(target=tarefa, args=("Processo 2", 4))

    # Iniciando os processos
    processo1.start()
    processo2.start()

    # join() -> Aguarda a finalização do processo antes de continuar
    processo1.join()
    processo2.join()

    fim = time.time()
    print(f"Todos os processos finalizaram em {fim - inicio:.2f} segundos!\n")

    # 📌 Exemplo 3: Programação Assíncrona com asyncio
    print("\n🔹 Exemplo de Programação Assíncrona com asyncio")

    async def tarefa_async(nome, contador):
        """
        Função assíncrona que simula uma tarefa concorrente.
        :param nome: Nome identificador da tarefa assíncrona
        :param contador: Número de iterações da tarefa
        """
        print(f"Iniciando {nome}...")
        for i in range(contador):
            await asyncio.sleep(0.5)  # await permite execução assíncrona sem bloquear
            print(f"{nome}: {i+1}")
        print(f"Finalizando {nome}...")

    async def main():
        inicio = time.time()
        # asyncio.gather() -> Executa múltiplas tarefas assíncronas ao mesmo tempo
        await asyncio.gather(
            tarefa_async("Tarefa Assíncrona 1", 4),
            tarefa_async("Tarefa Assíncrona 2", 4)
        )
        fim = time.time()
        print(f"Todas as tarefas assíncronas finalizaram em {fim - inicio:.2f} segundos!\n")

    asyncio.run(main())

    print("\n✅ Conclusão: Threading é útil para tarefas de I/O, Multiprocessing é ideal para processamento pesado, e Asyncio melhora eficiência em operações assíncronas!")
