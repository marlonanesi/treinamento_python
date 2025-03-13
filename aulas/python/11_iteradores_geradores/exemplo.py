# 🔹 Comparação Didática: Iteradores vs. Geradores

# 📌 Exemplo 1: Criando um Iterador Manualmente
class Contador:
    def __init__(self, limite):
        self.limite = limite  # Define o número máximo
        self.contador = 0  # Inicia a contagem
    
    def __iter__(self):
        return self  # Retorna o próprio objeto iterador
    
    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration  # Sinaliza que o iterador terminou

# Criando um objeto iterador e iterando sobre ele
print("\n🔹 Exemplo de Iterador Manual")
meu_contador = Contador(5)
for numero in meu_contador:
    print(numero)

# 📌 Exemplo 2: Criando um Gerador usando yield

def gerador_numeros(n):
    for i in range(1, n + 1):
        yield i  # Pausa a função e retorna um valor, mantendo o estado

print("\n🔹 Exemplo de Gerador")
meu_gerador = gerador_numeros(5)
for numero in meu_gerador:
    print(numero)

# 📌 Comparação de Uso de Memória
import sys

# Criando uma lista e um gerador com 1 milhão de números
lista = [x for x in range(1_000_000)]  # Lista tradicional
gerador = (x for x in range(1_000_000))  # Gerador

print("\n🔹 Comparação de Uso de Memória")
print(f"Tamanho da lista: {sys.getsizeof(lista)} bytes")  # Lista ocupa muita memória
print(f"Tamanho do gerador: {sys.getsizeof(gerador)} bytes")  # Gerador ocupa bem menos

# 📌 Exemplo de Uso Real com Arquivo Grande

def ler_arquivo_em_blocos(arquivo, tamanho=1024):
    with open(arquivo, 'r', encoding='utf-8') as f:
        while bloco := f.read(tamanho):
            yield bloco  # Retorna um bloco de texto sem carregar todo o arquivo

print("\n🔹 Exemplo de Leitura de Arquivo com Gerador")
# Este trecho está comentado para evitar erro caso não haja um arquivo disponível
# for bloco in ler_arquivo_em_blocos("grande_arquivo.txt"):
#     print(bloco)

print("\n✅ Conclusão: Geradores economizam memória e são ideais para grandes volumes de dados!")
