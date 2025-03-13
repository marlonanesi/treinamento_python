# 🔹 DESAFIO: Criando um Sistema de Gestão de Veículos 🚗

# 📌 Enunciado:
# A concessionária "Super Carros" deseja um sistema para gerenciar seu estoque de veículos
# utilizando Programação Orientada a Objetos (POO). O sistema deve permitir o cadastro,
# listagem, edição e remoção de veículos.
#
# O sistema deve funcionar da seguinte forma:
# 1. O usuário pode cadastrar um novo veículo informando:
#    - Marca
#    - Modelo
#    - Ano
#    - Tipo (Carro, Moto, Caminhão) *(se nenhum tipo for informado corretamente, o padrão será Carro)*.
# 2. O usuário pode visualizar a lista de veículos cadastrados.
# 3. O usuário pode editar os dados de um veículo existente.
# 4. O usuário pode remover um veículo pelo índice da lista.
# 5. O sistema deve rodar em um loop até que o usuário escolha sair.

# ✅ Tarefa:
# - Criar uma classe `Veiculo` com atributos `marca`, `modelo` e `ano`.
# - Criar classes `Carro`, `Moto` e `Caminhao`, que herdam de `Veiculo` e adicionam um atributo `tipo`.
# - Criar uma classe `Concessionaria` que gerencia a lista de veículos.
# - Implementar métodos para cadastrar, listar, editar e remover veículos.
# - Criar um menu interativo para o usuário.
#
# 🔥 Dica:
# - Utilize listas para armazenar os veículos.
# - Use `input()` para interagir com o usuário.
# - Utilize herança para diferenciar os tipos de veículos.
# - Certifique-se de tratar entradas inválidas.

# Classe base Veiculo
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

# Classes derivadas Carro, Moto e Caminhao
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.tipo = "Carro"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.tipo = "Moto"

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.tipo = "Caminhão"

# Classe Concessionaria para gerenciar a lista de veículos
class Concessionaria:
    def __init__(self):
        self.veiculos = []

    def cadastrar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
        print("Veículo cadastrado com sucesso!")

    def listar_veiculos(self):
        if not self.veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            for idx, veiculo in enumerate(self.veiculos):
                print(f"{idx}: {veiculo} - Tipo: {veiculo.tipo}")

    def editar_veiculo(self, indice, marca, modelo, ano):
        if 0 <= indice < len(self.veiculos):
            self.veiculos[indice].marca = marca
            self.veiculos[indice].modelo = modelo
            self.veiculos[indice].ano = ano
            print("Veículo atualizado com sucesso!")
        else:
            print("Índice inválido.")

    def remover_veiculo(self, indice):
        if 0 <= indice < len(self.veiculos):
            removido = self.veiculos.pop(indice)
            print(f"Veículo removido: {removido}")
        else:
            print("Índice inválido.")

# Função para exibir o menu interativo
def menu():
    concessionaria = Concessionaria()
    while True:
        print("\nMenu:")
        print("1. Cadastrar veículo")
        print("2. Listar veículos")
        print("3. Editar veículo")
        print("4. Remover veículo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            ano = input("Ano: ")
            tipo = input("Tipo (Carro, Moto, Caminhão): ").capitalize()
            if tipo == "Moto":
                veiculo = Moto(marca, modelo, ano)
            elif tipo == "Caminhão":
                veiculo = Caminhao(marca, modelo, ano)
            else:
                veiculo = Carro(marca, modelo, ano)
            concessionaria.cadastrar_veiculo(veiculo)
        elif opcao == "2":
            concessionaria.listar_veiculos()
        elif opcao == "3":
            concessionaria.listar_veiculos()
            try:
                indice = int(input("Índice do veículo a editar: "))
                marca = input("Nova marca: ")
                modelo = input("Novo modelo: ")
                ano = input("Novo ano: ")
                concessionaria.editar_veiculo(indice, marca, modelo, ano)
            except ValueError:
                print("Entrada inválida.")
        elif opcao == "4":
            concessionaria.listar_veiculos()
            try:
                indice = int(input("Índice do veículo a remover: "))
                concessionaria.remover_veiculo(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
