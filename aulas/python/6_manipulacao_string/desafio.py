# 🔹 DESAFIO: Analisador de Texto 📄

# 📌 Enunciado:
# Você foi contratado para desenvolver um programa que analise um texto fornecido pelo usuário.
# O sistema deve funcionar da seguinte forma:
# 1. O usuário deve inserir um texto qualquer.
# 2. O programa deve exibir:
#    - Quantidade de palavras no texto.
#    - Quantidade de caracteres (sem contar espaços).
#    - A palavra mais longa do texto.
# 3. Pergunte ao usuário se deseja analisar outro texto. Se sim, repita o processo. Caso contrário, finalize o programa.

# ✅ Tarefa:
# - Criar uma função chamada `analisar_texto(texto)` que exibe as informações pedidas.
# - Utilizar um loop para permitir que o usuário analise vários textos.
# - O programa só deve parar quando o usuário digitar "sair".

# 🔥 Dica:
# - Use a função `input()` para capturar a entrada do usuário.
# - Utilize `split()` para dividir o texto em palavras.
# - Utilize `max()` com a função `key=len` para encontrar a palavra mais longa.
# - Use `while` para repetir até que o usuário deseje sair.

# ✏️ Comece seu código abaixo:

def analisar_texto(texto):
    palavras = texto.split()
    qtd_palavras = len(palavras)
    qtd_caracteres = len(texto.replace(" ", ""))
    palavra_mais_longa = max(palavras, key=len)

    print(f"Quantidade de palavras: {qtd_palavras}")
    print(f"Quantidade de caracteres: {qtd_caracteres}")
    print(f"Palavra mais longa: {palavra_mais_longa}")

while True:
    texto = input("Digite um texto ou 'sair' para encerrar: ")
    if texto.lower() == "sair":
        break

    analisar_texto(texto)
    print()

print("Programa encerrado.")

# Agora, vamos analisar o código acima:
# - A função `analisar_texto(texto)` recebe um texto como parâmetro.
# - O texto é dividido em palavras usando o método `split()`.
# - A quantidade de palavras é obtida com a função `len()`.
# - A quantidade de caracteres é obtida removendo os espaços do texto e calculando o comprimento.
# - A palavra mais longa é obtida com a função `max()` e a função `key=len`.
# - O resultado é exibido na tela.
# - O programa principal solicita um texto ao usuário.
# - Se o texto for "sair", o programa é encerrado.
# - Caso contrário, a função `analisar_texto(texto)` é chamada.
# - O processo se repete até o usuário digitar "sair".
# - O programa exibe "Programa encerrado" ao final.