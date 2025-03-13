# 📝 Aula 12: Decoradores em Python

## 📌 Introdução

Os **decoradores** são uma ferramenta poderosa no Python que permite modificar o comportamento de funções ou métodos sem alterar seu código-fonte. Eles são amplamente utilizados para funcionalidades como logging, autenticação e controle de acesso.

Nesta aula, aprenderemos:

1. **O que são decoradores?**
2. **Criando um decorador simples**
3. **Usando decoradores embutidos (`@staticmethod`, `@classmethod`, `@property`)**
4. **Decoradores com argumentos**
5. **Empilhamento de decoradores**
6. **Casos práticos de uso**

---

## 📌 1. O que são Decoradores?

Um **decorador** é uma função que recebe outra função como argumento e retorna uma nova função com comportamento modificado.

### 🔹 Exemplo: Criando uma função decoradora
```python
def meu_decorador(func):
    def wrapper():
        print("Executando algo antes da função...")
        func()
        print("Executando algo depois da função...")
    return wrapper

@meu_decorador  # Aplicando o decorador à função
def saudacao():
    print("Olá, mundo!")

saudacao()
```
> **Aqui, `@meu_decorador` modifica o comportamento da função `saudacao()`, executando código antes e depois dela.**

---

## 📌 2. Criando um Decorador Simples

Um decorador pode ser usado para adicionar funcionalidades comuns a várias funções sem duplicar código.

### 🔹 Exemplo: Criando um decorador para logging
```python
def log_decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando a função {func.__name__} com argumentos {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorador
def soma(a, b):
    return a + b

print(soma(3, 5))
```
> **O decorador `log_decorador` exibe informações sobre a execução da função `soma()`.**

---

## 📌 3. Decoradores Embutidos (`@staticmethod`, `@classmethod`, `@property`)

O Python fornece decoradores nativos para uso com classes:

- **`@staticmethod`**: Define um método estático, que não acessa atributos da classe.
- **`@classmethod`**: Define um método que recebe a classe (`cls`) como primeiro argumento.
- **`@property`**: Define um método que pode ser acessado como um atributo.

### 🔹 Exemplo de decoradores embutidos
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def mensagem():
        print("Bem-vindo ao sistema!")
    
    @classmethod
    def criar_com_idade(cls, nome):
        return cls(nome, 18)  # Criando uma pessoa com idade padrão
    
    @property
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

Pessoa.mensagem()
pessoa1 = Pessoa.criar_com_idade("Carlos")
print(pessoa1.saudacao)
```
> **Esses decoradores são úteis para definir diferentes tipos de métodos em classes.**

---

## 📌 4. Decoradores com Argumentos

Podemos criar decoradores que aceitam parâmetros para tornar seu comportamento mais flexível.

### 🔹 Exemplo: Decorador com argumentos para autenticação
```python
def autenticar(usuario_autorizado):
    def decorador(func):
        def wrapper(usuario, *args, **kwargs):
            if usuario != usuario_autorizado:
                print("Acesso negado!")
                return
            return func(usuario, *args, **kwargs)
        return wrapper
    return decorador

@autenticar("admin")
def painel(usuario):
    print(f"Bem-vindo ao painel, {usuario}!")

painel("user")  # Acesso negado!
painel("admin")  # Bem-vindo ao painel!
```
> **Aqui, o decorador `autenticar` aceita um argumento e valida o usuário antes de executar a função.**

---

## 📌 5. Empilhamento de Decoradores

Podemos aplicar múltiplos decoradores a uma única função.

### 🔹 Exemplo: Aplicando dois decoradores a uma função
```python
def decorador1(func):
    def wrapper():
        print("Executando decorador 1...")
        func()
    return wrapper

def decorador2(func):
    def wrapper():
        print("Executando decorador 2...")
        func()
    return wrapper

@decorador1
@decorador2
def minha_funcao():
    print("Função principal executada.")

minha_funcao()
```
> **Os decoradores são aplicados na ordem de baixo para cima (`decorador2` → `decorador1` → `minha_funcao`).**

---

## 📌 6. Casos Práticos de Uso

Os decoradores são amplamente usados em bibliotecas e frameworks, como Django e Flask. Algumas aplicações comuns incluem:

✔️ **Autenticação e controle de acesso**
✔️ **Registro de logs**
✔️ **Medição de tempo de execução**
✔️ **Cache de resultados para otimização**

### 🔹 Exemplo: Medindo o tempo de execução de uma função
```python
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

tarefa_pesada()
```
> **Esse decorador é útil para analisar a performance de funções demoradas.**

---

## 🏆 Conclusão

- **Decoradores** permitem modificar funções sem alterar seu código-fonte.
- Podem ser usados para **log**, **autenticação**, **tempo de execução**, entre outros.
- Python oferece decoradores embutidos (`@staticmethod`, `@classmethod`, `@property`).
- **Decoradores podem aceitar argumentos e serem empilhados para funcionalidades complexas.**