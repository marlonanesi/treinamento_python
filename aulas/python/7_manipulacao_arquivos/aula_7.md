# 📝 Aula 7: Manipulação de Arquivos em Python

## 📌 Introdução

A manipulação de arquivos é uma habilidade essencial em Python, permitindo a leitura, escrita e modificação de arquivos no sistema. Nesta aula, aprenderemos sobre:

1. **Abrindo e fechando arquivos**
2. **Modos de abertura (`r`, `w`, `a`, `x`)**
3. **Lendo arquivos (`read()`, `readline()`, `readlines()`)**
4. **Escrevendo em arquivos (`write()`, `writelines()`)**
5. **Usando `with open()` para manipulação segura**
6. **Trabalhando com arquivos CSV**

---

## 📌 1. Abrindo e Fechando Arquivos

Para abrir um arquivo em Python, usamos a função `open()`. Sempre que abrimos um arquivo, devemos fechá-lo após o uso com `close()`.

### ✅ Exemplo:
```python
arquivo = open("dados.txt", "r")  # Abre o arquivo para leitura
conteudo = arquivo.read()  # Lê o conteúdo do arquivo
print(conteudo)
arquivo.close()  # Fecha o arquivo
```
> **Dica:** Esquecer de fechar um arquivo pode causar problemas no sistema.

---

## 📌 2. Modos de Abertura de Arquivos

O `open()` aceita um segundo argumento que define o modo de abertura:

| Modo  | Descrição |
|--------|------------|
| `r`  | Leitura (padrão) |
| `w`  | Escrita (apaga o conteúdo existente) |
| `a`  | Acrescentar (adiciona ao final do arquivo) |
| `x`  | Criar um novo arquivo (erro se já existir) |
| `b`  | Modo binário (exemplo: imagens, PDFs) |

### ✅ Exemplo:
```python
arquivo = open("novo.txt", "w")  # Cria um novo arquivo para escrita
arquivo.write("Olá, Python!\n")  # Escreve no arquivo
arquivo.close()
```
> **Cuidado!** O modo `w` sobrescreve o arquivo existente.

---

## 📌 3. Lendo Arquivos

Podemos ler arquivos de várias formas:

### 🔹 `read()`: Lê todo o conteúdo de uma vez
```python
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
```

### 🔹 `readline()`: Lê uma linha por vez
```python
arquivo = open("dados.txt", "r")
linha = arquivo.readline()
print(linha)  # Apenas a primeira linha será exibida
arquivo.close()
```

### 🔹 `readlines()`: Retorna uma lista de todas as linhas
```python
arquivo = open("dados.txt", "r")
linhas = arquivo.readlines()
print(linhas)  # Lista de strings, uma por linha
arquivo.close()
```

---

## 📌 4. Escrevendo em Arquivos

Podemos escrever ou adicionar texto em arquivos:

### 🔹 `write()`: Escreve uma string no arquivo
```python
arquivo = open("dados.txt", "w")
arquivo.write("Nova linha de texto\n")
arquivo.close()
```

### 🔹 `writelines()`: Escreve uma lista de strings
```python
arquivo = open("dados.txt", "a")  # Modo de adicionar
arquivo.writelines(["Linha 1\n", "Linha 2\n"])
arquivo.close()
```

---

## 📌 5. Usando `with open()` (Forma Segura)

A melhor prática para manipulação de arquivos é usar `with open()`, pois ele fecha o arquivo automaticamente.

### ✅ Exemplo:
```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```
> **Vantagem:** Não precisamos chamar `close()`, pois o arquivo é fechado automaticamente ao sair do bloco `with`.

---

## 📌 6. Trabalhando com Arquivos CSV

Os arquivos CSV (Comma-Separated Values) são amplamente usados para armazenar dados estruturados.

### 🔹 Lendo um arquivo CSV
```python
import csv

with open("dados.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
```

### 🔹 Escrevendo em um arquivo CSV
```python
import csv

dados = [["Nome", "Idade"], ["Alice", 25], ["Bob", 30]]

with open("dados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)
```

---

## 🏆 Conclusão

- A função `open()` permite abrir arquivos em diferentes modos.
- Sempre feche arquivos ou use `with open()` para segurança.
- `read()`, `readline()`, e `readlines()` permitem ler arquivos de maneiras diferentes.
- `write()` e `writelines()` são usados para escrever arquivos.
- O módulo `csv` facilita a leitura e escrita de arquivos CSV.

Agora que você domina a manipulação de arquivos, vamos praticar com um **desafio!** 🚀
