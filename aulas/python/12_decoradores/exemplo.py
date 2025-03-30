# 🔹 Comparação Didática: Decoradores em Python

# 📌 Exemplo 1: Criando um Decorador Simples
def meu_decorador(func):
    def wrapper():
        print("Executando algo antes da função...")  # Ação antes da função decorada
        func()  # Chamada da função original
        print("Executando algo depois da função...")  # Ação depois da função decorada
    return wrapper

@meu_decorador  # Aplicando o decorador à função
def saudacao():
    print("Olá, mundo!")

print("\n🔹 Exemplo de Decorador Simples")
saudacao()

# 📌 Exemplo 2: Decorador para Medir Tempo de Execução
import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Marca o tempo inicial
        resultado = func(*args, **kwargs)  # Executa a função original
        fim = time.time()  # Marca o tempo final
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")  # Calcula e exibe o tempo de execução
        return resultado
    return wrapper

@medir_tempo
def tarefa_pesada():
    time.sleep(2)  # Simula uma tarefa demorada
    print("Tarefa concluída!")

print("\n🔹 Exemplo de Decorador para Medir Tempo")
tarefa_pesada()

# 📌 Exemplo 3: Decorador com Argumentos
def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):  # Repete a execução da função `n` vezes
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)  # O decorador recebe um argumento (número de repetições)
def mensagem():
    print("Executando a função repetida!")

print("\n🔹 Exemplo de Decorador com Argumentos")
mensagem()

# 📌 Exemplo 4: Decoradores Embutidos (`@staticmethod`, `@classmethod`, `@property`)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @staticmethod
    def mensagem():
        # `@staticmethod`: Método que não depende da instância ou da classe.
        # Pode ser chamado diretamente sem acessar atributos ou métodos da classe.
        print("Bem-vindo ao sistema!")
    
    @classmethod
    def criar_padrao(cls, nome):
        # `@classmethod`: Método que recebe a classe como primeiro argumento (cls).
        # Útil para criar instâncias ou acessar atributos/métodos da classe.
        return cls(nome, 18)
    
    @property
    def saudacao(self):
        # `@property`: Permite acessar um método como se fosse um atributo.
        # Útil para encapsular lógica de acesso a atributos.
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

print("\n🔹 Exemplo de Decoradores Embutidos")
Pessoa.mensagem()  # Chamada de método estático
pessoa1 = Pessoa.criar_padrao("Carlos")  # Criação de instância usando método de classe
print(pessoa1.saudacao)  # Acessando o método como se fosse um atributo

print("\n✅ Conclusão: Decoradores são úteis para modificar funções e métodos de forma reutilizável e eficiente!")