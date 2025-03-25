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