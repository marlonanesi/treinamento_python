# 📝 Aula 8: Módulos e Pacotes em Python

## 📌 Introdução

Os **módulos** e **pacotes** são fundamentais para a organização do código e a reutilização de funcionalidades. Com eles, podemos dividir nosso código em arquivos menores e reutilizar código de terceiros. Nesta aula, aprenderemos sobre:

1. **O que são módulos e pacotes?**
2. **Criando e importando módulos**
3. **Utilizando pacotes padrão do Python**
4. **Instalando e utilizando pacotes externos (`pip`)**
5. **Estruturando pacotes personalizados**

---

## 📌 1. O que são Módulos e Pacotes?

- **Módulo**: Um arquivo `.py` contendo funções, classes ou variáveis reutilizáveis.
- **Pacote**: Um diretório contendo múltiplos módulos organizados, com um arquivo `__init__.py`.

> **Vantagem**: Permite a organização do código em arquivos menores e facilita a reutilização.

---

## 📌 2. Criando e Importando Módulos

Para criar um módulo, basta criar um arquivo `.py` e definir funções nele.

### ✅ Exemplo: Criando um módulo `meu_modulo.py`
```python
# Arquivo: meu_modulo.py

def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo ao curso de Python."
```

Agora podemos importar esse módulo em outro arquivo e utilizá-lo:

```python
import meu_modulo

print(meu_modulo.saudacao("Alice"))
```

Podemos também importar apenas funções específicas:
```python
from meu_modulo import saudacao
print(saudacao("Bob"))
```

> **Dica:** Usar `import meu_modulo as mod` permite encurtar nomes de módulos.

---

## 📌 3. Utilizando Pacotes Padrão do Python

O Python possui diversos módulos nativos/embutidos que podem ser usados sem necessidade de instalação.

### 🔹 Exemplo: Usando o módulo `math`
```python
import math

print(math.sqrt(16))  # Raiz quadrada
print(math.pi)        # Valor de pi
```

### 🔹 Exemplo: Usando o módulo `random`
```python
import random

print(random.randint(1, 10))  # Número aleatório entre 1 e 10
```

> **Dica:** Você pode consultar todos os módulos embutidos na [documentação oficial](https://docs.python.org/3/library/).

---

## 📌 4. Instalando e Utilizando Pacotes Externos (`pip`)

Além dos módulos internos, podemos instalar pacotes externos usando o **pip**, o gerenciador de pacotes do Python.

### 🔹 Instalando um pacote:
```sh
pip install requests
```

### 🔹 Exemplo: Usando o pacote `requests` para acessar uma API
```python
import requests

resposta = requests.get("https://api.github.com")
print(resposta.status_code)  # Código HTTP da resposta
```

> **Dica:** Para ver pacotes instalados, use `pip list`.

---

## 📌 5. Estruturando Pacotes Personalizados

Um **pacote** é um diretório contendo múltiplos módulos e um arquivo especial `__init__.py`.

### 🔹 Estrutura de um pacote:
```
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
```

### 🔹 Criando o pacote `meu_pacote`
```python
# Arquivo: meu_pacote/modulo1.py
def mensagem():
    return "Isso veio do módulo 1!"
```

Agora podemos importar o pacote:
```python
from meu_pacote import modulo1
print(modulo1.mensagem())
```

> **Dica:** O arquivo `__init__.py` é usado para inicializar o pacote. Se a pasta não contiver um arquivo `__init__.py`, ela pode não ser reconhecida como um pacote pelo Python, resultando em um erro de módulo não encontrado.

---

## 🏆 Conclusão

- **Módulos** ajudam a organizar o código e permitem reutilização.
- **Pacotes** são conjuntos de módulos organizados em diretórios.
- Podemos importar módulos próprios, embutidos ou externos.
- O **pip** permite instalar pacotes da comunidade.
- Criar pacotes próprios facilita a modularização de projetos maiores.
