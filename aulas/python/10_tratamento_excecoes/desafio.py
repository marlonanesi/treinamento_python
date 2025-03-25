# 🔹 DESAFIO: Calculadora com Tratamento de Exceções 🧮

# 📌 Enunciado:
# Você deve criar um programa que funcione como uma calculadora simples, permitindo
# ao usuário inserir dois números e uma operação matemática (+, -, *, /).
# O programa deve tratar os seguintes tipos de exceção:
# 1. Entrada inválida (se o usuário inserir algo que não seja um número). Exceção: ValueError
# 2. Divisão por zero. Exceção: ZeroDivisionError
# 3. Operação inválida (caso o usuário insira um operador desconhecido). Exceção: ValueError
#
# ✅ Tarefa:
# - Criar uma função `calculadora(num1, num2, operacao)` que realiza a operação desejada.
# - Utilizar `try-except` para capturar exceções.
# - Exibir mensagens de erro apropriadas para cada caso.
# - O programa deve continuar rodando até que o usuário escolha sair.
#
# 🔥 Dica:
# - Utilize `input()` para capturar os valores digitados.
# - Use um loop `while` para manter a calculadora funcionando até que o usuário digite 'sair'.
# - Lembre-se de converter os números para `float` dentro de um bloco `try`.