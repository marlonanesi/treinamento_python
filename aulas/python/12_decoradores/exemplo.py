# 🔹 Comparação Didática: Decoradores em Python

# 📌 Exemplo 1: Criando um Decorador Simples
def meu_decorador(func):
    def wrapper():
        print("Executando algo antes da função...")
        func()
        print("Executando algo depois da função...")
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
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tempo
def tarefa_pesada():
    time.sleep(2)
    print("Tarefa concluída!")

print("\n🔹 Exemplo de Decorador para Medir Tempo")
tarefa_pesada()

# 📌 Exemplo 3: Decorador com Argumentos
def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
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
        print("Bem-vindo ao sistema!")
    
    @classmethod
    def criar_padrao(cls, nome):
        return cls(nome, 18)
    
    @property
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

print("\n🔹 Exemplo de Decoradores Embutidos")
Pessoa.mensagem()
pessoa1 = Pessoa.criar_padrao("Carlos")
print(pessoa1.saudacao)

print("\n✅ Conclusão: Decoradores são úteis para modificar funções e métodos de forma reutilizável e eficiente!")
