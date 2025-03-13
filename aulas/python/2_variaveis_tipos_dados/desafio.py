# 🏆 DESAFIO: Manipulação de Variáveis e Tipos de Dados

# Objetivo: O aluno deve corrigir e completar o código abaixo para que ele funcione corretamente.
# O programa deve armazenar informações de um usuário, processá-las e exibir uma mensagem personalizada.

# 📝 Instruções:
# 1. Defina corretamente as variáveis abaixo preenchendo os valores adequados.
# 2. Converta os tipos de dados conforme necessário para realizar os cálculos e concatenar as strings corretamente.
# 3. Substitua os '???' pelas expressões corretas.
# 4. Execute o código e veja se a saída está correta (abra o terminal, execute o comando python > arquivo).

# Definição de variáveis
nome = '???'  # Nome do usuário (string)
idade = '???'  # Idade do usuário (int)
altura = '???'  # Altura do usuário (float)
peso = '???'  # Peso do usuário (float)

# Cálculo do IMC (Índice de Massa Corporal)
imc = peso / (altura ** 2)

# Mensagem formatada usando f-string
mensagem = f"Olá, {'???'}! Você tem {'???'} anos, mede {'???'}m e pesa {'???'}kg."
mensagem_imc = f"Seu IMC é {'???':.2f}."

# Exibir resultados
print(mensagem)
print(mensagem_imc)

# Desafio extra:
# 1. Modifique o programa para classificar o IMC como "Abaixo do peso", "Peso normal" ou "Sobrepeso".
# 2. Pergunte ao usuário qual é a sua comida favorita e exiba uma mensagem incluindo essa informação.
