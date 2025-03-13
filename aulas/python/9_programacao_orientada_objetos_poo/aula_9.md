# 📝 Aula 9: Programação Orientada a Objetos (POO) em Python

## 📌 Introdução

A **Programação Orientada a Objetos (POO)** é um paradigma de programação que permite estruturar o código de forma modular e reutilizável, modelando entidades do mundo real como **objetos**. Nesta aula, aprenderemos sobre:

1. **Conceitos principais da POO**
2. **Criando classes e objetos**
3. **Atributos e métodos**
4. **Encapsulamento**
5. **Herança**
6. **Polimorfismo**
7. **Abstração**

---

## 📌 1. Conceitos Principais da POO

A POO se baseia em quatro pilares:

- **Encapsulamento**: Protege os dados dentro dos objetos.
- **Herança**: Permite que uma classe derive de outra.
- **Polimorfismo**: Permite que métodos tenham diferentes comportamentos.
- **Abstração**: Oculta detalhes complexos e expõe apenas o necessário.

> **Vantagem**: Facilita a organização, manutenção e reutilização do código.

---

## 📌 2. Criando Classes e Objetos

Uma **classe** é um modelo para criar **objetos**. Um objeto é uma instância de uma classe.

### ✅ Exemplo: Criando uma classe `Carro`
```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Criando um objeto (instância da classe)
meu_carro = Carro("Toyota", "Corolla", 2023)
print(meu_carro.marca)  # Saída: Toyota
```

---

## 📌 3. Atributos e Métodos

- **Atributos**: Características do objeto (variáveis).
- **Métodos**: Ações que um objeto pode realizar (funções dentro da classe).

### 🔹 Exemplo: Criando métodos em uma classe
```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
        print("O carro está ligado.")
    
    def desligar(self):
        self.ligado = False
        print("O carro está desligado.")

# Criando um carro e ligando-o
meu_carro = Carro("Honda", "Civic", 2022)
meu_carro.ligar()
```

---

## 📌 4. Encapsulamento

O **encapsulamento** protege os dados de serem acessados ou modificados diretamente.

- `_atributo` → Indica que o atributo é protegido.
- `__atributo` → Indica que o atributo é privado.

### 🔹 Exemplo: Protegendo um atributo
```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito realizado. Novo saldo: R$ {self.__saldo}")
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor} realizado.")
        else:
            print("Saldo insuficiente!")

# Criando conta e interagindo com saldo protegido
conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(200)
```

---

## 📌 5. Herança

A **herança** permite criar uma nova classe baseada em uma classe existente.

### 🔹 Exemplo: Criando uma classe `CarroEletrico` que herda de `Carro`
```python
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, bateria):
        super().__init__(marca, modelo, ano)
        self.bateria = bateria
    
    def carregar_bateria(self):
        print("Bateria carregada!")

# Criando um carro elétrico
meu_tesla = CarroEletrico("Tesla", "Model S", 2024, "100 kWh")
meu_tesla.carregar_bateria()
```

---

## 📌 6. Polimorfismo

O **polimorfismo** permite sobrescrever métodos de uma classe pai na classe filha.

### 🔹 Exemplo: Sobrescrevendo um método
```python
class Animal:
    def fazer_som(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late")

class Gato(Animal):
    def fazer_som(self):
        print("O gato mia")

# Testando polimorfismo
animais = [Cachorro(), Gato()]
for animal in animais:
    animal.fazer_som()
```

---

## 📌 7. Abstração

A **abstração** define classes base (abstratas) que não podem ser instanciadas diretamente.

### 🔹 Exemplo: Criando uma classe abstrata
```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

# Criando um quadrado e calculando a área
quadrado = Quadrado(4)
print(quadrado.calcular_area())  # Saída: 16
```

---

## 🏆 Conclusão

- **Classes e objetos** são a base da POO.
- **Atributos e métodos** definem as características e comportamentos de um objeto.
- **Encapsulamento** protege dados sensíveis.
- **Herança** permite reuso de código entre classes.
- **Polimorfismo** permite diferentes implementações de métodos.
- **Abstração** define interfaces para serem implementadas por outras classes.
