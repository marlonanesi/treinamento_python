import csv

def ler_e_imprimir_nomes():
    with open('nomes.csv', 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        
        print("=" * 50)
        print("LISTA DE PESSOAS")
        print("=" * 50)
        
        for linha in leitor:
            nome_completo = f"{linha['nome']} {linha['sobrenome']}"
            print(f"Nome: {nome_completo:<20} | Idade: {linha['idade']:<3} | Cidade: {linha['cidade']}")
        
        print("=" * 50)

if __name__ == "__main__":
    ler_e_imprimir_nomes()