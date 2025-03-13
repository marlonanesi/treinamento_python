# 🔹 Manipulação de Dados com Pandas - Exemplo Didático

import pandas as pd

# 📌 1. Criando um DataFrame
print("\n🔹 Criando um DataFrame")

dados = {
    "Nome": ["Ana", "Carlos", "Bianca", "Daniel"],
    "Idade": [25, 30, 22, 28],
    "Cidade": ["SP", "RJ", "MG", "SP"],
    "Salário": [3000, 4500, 2500, 4000]
}

df = pd.DataFrame(dados)
print(df)

# 📌 2. Acessando e Filtrando Dados
print("\n🔹 Acessando e Filtrando Dados")

print("\n📍 Coluna Nome:")
print(df["Nome"])  # Exibe apenas os nomes

print("\n📍 Filtrando pessoas com idade maior que 25 anos:")
print(df[df["Idade"] > 25])

# 📌 3. Adicionando e Modificando Dados
print("\n🔹 Adicionando e Modificando Dados")

# Adicionando uma nova coluna "Bônus"
df["Bônus"] = df["Salário"] * 0.10
print("\n📍 Adicionando coluna 'Bônus' (10% do salário):")
print(df)

# Modificando valores específicos
df.loc[df["Nome"] == "Carlos", "Salário"] = 5000
print("\n📍 Modificando o salário de Carlos para 5000:")
print(df)

# 📌 4. Estatísticas Básicas
print("\n🔹 Estatísticas Básicas")

print("\n📍 Média de Idade:", df["Idade"].mean())
print("\n📍 Maior Salário:", df["Salário"].max())
print("\n📍 Estatísticas Gerais:")
print(df.describe())

# 📌 5. Agrupando e Agregando Dados
print("\n🔹 Agrupando e Agregando Dados")

print("\n📍 Média Salarial por Cidade:")
print(df.groupby("Cidade")["Salário"].mean())

# 📌 6. Exportando e Importando Dados
print("\n🔹 Exportando e Importando Dados")

# Salvando como CSV
df.to_csv("dados_exemplo.csv", index=False)
print("\n✅ Dados salvos em 'dados_exemplo.csv'!")

# Lendo novamente o arquivo salvo
df_novo = pd.read_csv("dados_exemplo.csv")
print("\n📍 Lendo os dados salvos:")
print(df_novo)
