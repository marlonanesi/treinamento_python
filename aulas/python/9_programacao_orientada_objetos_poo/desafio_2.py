# 🔹 DESAFIO: Criando um Sistema de Gestão de Veículos com SQLite 🚗

# 📌 Enunciado:
# A concessionária "Super Carros" deseja um sistema para gerenciar seu estoque de veículos
# utilizando Programação Orientada a Objetos (POO) e armazenando os dados em um banco de dados SQLite.
# O sistema deve permitir o cadastro, listagem, edição e remoção de veículos diretamente no banco.
#
# ✅ A classe `Database` já está pronta e implementa os métodos necessários para interagir com o SQLite.
# Seu desafio é utilizar essa classe para criar um menu interativo onde o usuário poderá gerenciar os veículos.
#
# O sistema deve funcionar da seguinte forma:
# 1. O usuário pode cadastrar um novo veículo informando:
#    - Marca
#    - Modelo
#    - Ano
#    - Tipo (Carro, Moto, Caminhão) *(se nenhum tipo for informado corretamente, o padrão será Carro)*.
# 2. O usuário pode visualizar a lista de veículos cadastrados.
# 3. O usuário pode editar os dados de um veículo existente.
# 4. O usuário pode remover um veículo pelo ID da tabela do banco de dados.
# 5. O sistema deve rodar em um loop até que o usuário escolha sair.
#
# ✅ Tarefa:
# - Utilizar a classe `Database` para armazenar e manipular os veículos no banco de dados.
# - Instalar o pacote externo do sqlite utilizando o pip "pip install sqlite".
# - Criar um menu interativo para o usuário.
#
# 🔥 Dica:
# - Utilize o módulo `sqlite` criado previamente para interagir com o banco de dados.
# - Use `input()` para interagir com o usuário.
# - Certifique-se de tratar entradas inválidas.

from sqlite import Database

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

# Classe Concessionaria para gerenciar a lista de veículos usando SQLite
class Concessionaria:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def cadastrar_veiculo(self, veiculo):
        self.db.inserir_veiculo(veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.tipo)

    def listar_veiculos(self):
        veiculos = self.db.listar_veiculos()
        if not veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            for veiculo in veiculos:
                print(f"{veiculo[0]}: {veiculo[1]} {veiculo[2]} ({veiculo[3]}) - Tipo: {veiculo[4]}")

    def atualizar_veiculo(self, veiculo_id, marca, modelo, ano, tipo):
        self.db.atualizar_veiculo(veiculo_id, marca, modelo, ano, tipo)

    def remover_veiculo(self, veiculo_id):
        self.db.remover_veiculo(veiculo_id)

# Função para exibir o menu interativo
def menu():
    concessionaria = Concessionaria('concessionaria.db')
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
            print("Veículo cadastrado com sucesso!")
            
        elif opcao == "2":
            concessionaria.listar_veiculos()

        elif opcao == "3":
            veiculo_id = int(input("ID do veículo a editar: "))
            marca = input("Nova Marca: ")
            modelo = input("Novo Modelo: ")
            ano = input("Novo Ano: ")
            tipo = input("Novo Tipo (Carro, Moto, Caminhão): ").capitalize()
            if tipo not in ["Carro", "Moto", "Caminhão"]:
                tipo = "Carro"
            concessionaria.atualizar_veiculo(veiculo_id, marca, modelo, ano, tipo)
            print("Veículo atualizado com sucesso!")

        elif opcao == "4":
            veiculo_id = int(input("ID do veículo a remover: "))
            concessionaria.remover_veiculo(veiculo_id)
            print("Veículo removido com sucesso!")

        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()