# 📝 Aula 15: Manipulação de Dados com Pandas

## 📌 Introdução  

A **manipulação de dados** é uma das habilidades mais importantes para análise de dados, ciência de dados e desenvolvimento.  
O **Pandas** é a biblioteca mais popular para manipulação eficiente de tabelas de dados em Python.  

Nesta aula, aprenderemos:  

1. **O que é Pandas e por que utilizá-lo?**  
2. **Criando e manipulando DataFrames**  
3. **Leitura e escrita de arquivos CSV e Excel**  
4. **Filtragem e transformação de dados**  
5. **Estatísticas básicas e agregações**  

---

## 📌 1. O que é Pandas e por que utilizá-lo?  

O **Pandas** fornece estruturas para manipulação de dados tabulares de forma simples e eficiente.  

✔️ Fácil leitura e escrita de dados  
✔️ Integração com **NumPy, Matplotlib e SQL**  
✔️ Excelente para **limpeza, transformação e análise** de dados  

> **🔹 Instalação**  
```bash
pip install pandas
```

---

## 📌 2. Criando e Manipulando DataFrames  

O **DataFrame** é a estrutura principal do Pandas, semelhante a uma planilha do Excel.  

### 🔹 Criando um DataFrame  

```python
import pandas as pd  

# Criando um DataFrame com dicionário
dados = {
    "Nome": ["Ana", "Carlos", "Bianca"],
    "Idade": [25, 30, 22],
    "Cidade": ["SP", "RJ", "MG"]
}

df = pd.DataFrame(dados)

print(df)
```

📝 **Saída:**  
```
    Nome  Idade Cidade
0   Ana     25     SP
1  Carlos   30     RJ
2  Bianca   22     MG
```

---

### 🔹 Acessando colunas e linhas  

```python
print(df["Nome"])  # Acessa uma coluna  
print(df.iloc[0])  # Acessa a primeira linha  
print(df.loc[df["Idade"] > 23])  # Filtra dados  
```

📝 **Saída:**  
```
0      Ana
1   Carlos
2   Bianca
Name: Nome, dtype: object
```

---

## 📌 3. Leitura e Escrita de Arquivos CSV e Excel  

Pandas permite ler e escrever arquivos **CSV** e **Excel** facilmente.  

### 🔹 Lendo um arquivo CSV  

```python
df = pd.read_csv("dados.csv")
print(df.head())  # Exibe as 5 primeiras linhas  
```

### 🔹 Salvando um DataFrame como CSV  

```python
df.to_csv("novo_arquivo.csv", index=False)
```

📌 **Parâmetro `index=False`**: evita salvar o índice do DataFrame como uma coluna.  

### 🔹 Lendo um arquivo Excel  

```python
df = pd.read_excel("dados.xlsx")
```

📌 Para ler arquivos **Excel**, instale a dependência **openpyxl**:  

```bash
pip install openpyxl
```

---

## 📌 4. Filtragem e Transformação de Dados  

Pandas facilita **filtragem, agregação e modificação** de dados.  

### 🔹 Filtrando dados  

```python
df_filtrado = df[df["Idade"] > 25]
print(df_filtrado)
```

### 🔹 Adicionando uma nova coluna  

```python
df["Salário"] = [3000, 4000, 2500]
print(df)
```

### 🔹 Modificando valores  

```python
df.loc[df["Nome"] == "Carlos", "Salário"] = 4500
print(df)
```

---

## 📌 5. Estatísticas Básicas e Agregações  

O Pandas permite cálculos estatísticos rápidos.  

### 🔹 Estatísticas básicas  

```python
print(df["Idade"].mean())   # Média  
print(df["Idade"].min())    # Mínimo  
print(df["Idade"].max())    # Máximo  
print(df.describe())        # Estatísticas gerais  
```

### 🔹 Agrupamento de dados  

```python
df_grouped = df.groupby("Cidade")["Salário"].mean()
print(df_grouped)
```

📝 **Saída:**  
```
Cidade
MG    2500
RJ    4500
SP    3000
Name: Salário, dtype: int64
```

---

## 🏆 Conclusão  

- **Pandas** é essencial para manipulação eficiente de dados.  
- **DataFrames** organizam os dados em tabelas manipuláveis.  
- Podemos **ler e salvar arquivos CSV e Excel** facilmente.  
- Filtragem, transformação e agregação de dados são simples.  
- Estatísticas básicas ajudam a analisar grandes conjuntos de dados. 
