# 🔹 Comparação Didática: Gerenciadores de Contexto (Context Managers) em Python

# 📌 Exemplo 1: Gerenciador de Contexto com `with` para Manipular Arquivos
print("\n🔹 Exemplo de Gerenciador de Contexto com Arquivos")
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Usando um gerenciador de contexto para abrir arquivos!")
print("Arquivo criado e fechado automaticamente!")

# 📌 Exemplo 2: Criando um Gerenciador de Contexto com Classe
class MeuGerenciador:
    def __init__(self, nome_arquivo, modo):
        self.nome_arquivo = nome_arquivo
        self.modo = modo
    
    def __enter__(self):
        print("Abrindo o arquivo...")
        self.arquivo = open(self.nome_arquivo, self.modo)
        return self.arquivo
    
    def __exit__(self, tipo, valor, traceback):
        self.arquivo.close()
        print("Arquivo fechado corretamente!")

print("\n🔹 Exemplo de Gerenciador de Contexto com Classe")
with MeuGerenciador("teste.txt", "w") as f:
    f.write("Usando um gerenciador de contexto personalizado!")

# 📌 Exemplo 3: Criando um Gerenciador de Contexto com `contextlib`
from contextlib import contextmanager

@contextmanager
def gerenciar_arquivo(nome_arquivo, modo):
    print("Abrindo o arquivo...")
    arquivo = open(nome_arquivo, modo)
    try:
        yield arquivo
    finally:
        arquivo.close()
        print("Arquivo fechado com sucesso!")

print("\n🔹 Exemplo de Gerenciador de Contexto com `contextlib`")
with gerenciar_arquivo("exemplo2.txt", "w") as f:
    f.write("Gerenciando arquivos com contextlib!")

# 📌 Exemplo 4: Gerenciando Conexões com Banco de Dados
import sqlite3

@contextmanager
def conexao_banco(nome_bd):
    print("Conectando ao banco de dados...")
    conexao = sqlite3.connect(nome_bd)
    cursor = conexao.cursor()
    try:
        yield cursor
    finally:
        conexao.commit()
        conexao.close()
        print("Conexão com o banco de dados encerrada!")

print("\n🔹 Exemplo de Gerenciador de Contexto para Banco de Dados")
with conexao_banco("meubanco.db") as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
    cursor.execute("INSERT INTO usuarios (nome) VALUES ('Alice')")

print("\n✅ Conclusão: Gerenciadores de contexto ajudam a lidar com arquivos, bancos de dados e outros recursos de maneira eficiente e segura!")
