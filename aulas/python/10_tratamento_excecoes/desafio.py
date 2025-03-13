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


def calculadora(num1, num2, operacao):
    """Função que executa a operação matemática e trata exceções."""
    try:
        if operacao == "+":
            return num1 + num2
        elif operacao == "-":
            return num1 - num2
        elif operacao == "*":
            return num1 * num2
        elif operacao == "/":
            return num1 / num2  # Pode gerar ZeroDivisionError
        else: # Nesse caso estamos forçando uma exceção, pois sabemos que nenhum dos operadores validos foi informado
            raise ValueError("Operação inválida. Use +, -, * ou /.") 
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero."
    except ValueError as e: # Captura a exceção gerada acima e exibe a mensagem de erro
        return f"Erro: {e}"


# Loop principal da calculadora
while True:
    try:
        num1 = input("Digite o primeiro número (ou 'sair' para encerrar): ")
        if num1.lower() == "sair":
            break
        num1 = float(num1)
        
        num2 = input("Digite o segundo número: ")
        num2 = float(num2)
        
        operacao = input("Digite a operação (+, -, *, /): ")
        resultado = calculadora(num1, num2, operacao)
        
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: Entrada inválida! Digite um número válido.")
    
print("Calculadora encerrada.")
