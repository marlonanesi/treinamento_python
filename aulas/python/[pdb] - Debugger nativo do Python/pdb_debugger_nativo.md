# 📌 Aula: Debugando com PDB - O Depurador Nativo do Python

## 📝 Introdução

Nesta aula, vamos aprender a utilizar o **PDB**, o **debugger nativo do Python**, uma ferramenta poderosa que permite **inspecionar variáveis**, **controlar a execução do código passo a passo** e encontrar **erros com mais eficiência**.

---

## 🔹 O que é o PDB?

O **PDB (Python Debugger)** é uma ferramenta integrada ao Python que permite:

- Pausar a execução do programa em pontos específicos.
- Ver o valor de variáveis em tempo real.
- Executar o código linha a linha.
- Corrigir e entender erros com mais facilidade.

---

## 🔧 Como iniciar o PDB?

### ✅ Usando diretamente no código:

```python
import pdb

def saudacao(nome):
    pdb.set_trace()  # Pausa a execução aqui
    print(f"Olá, {nome}!")

saudacao("Alice")
```

---

## 🛠️ Comandos principais do PDB

| Comando | Significado                                  |
|--------|----------------------------------------------|
| `n`    | Executa a **próxima linha**                  |
| `s`    | Entra na função chamada                      |
| `c`    | Continua a execução até o próximo breakpoint |
| `q`    | Sai do modo de debug                         |
| `l`    | Lista as próximas linhas de código           |
| `p`    | Imprime o valor de uma variável              |
| `b`    | Define um breakpoint (parada)                |
| `h`    | Exibe ajuda dos comandos                     |
| `dir()`| Lista os atributos e métodos de um objeto     |

---

### ✅ Exemplo prático:

```python
def soma(a, b):
    resultado = a + b
    return resultado

def main():
    import pdb; pdb.set_trace()
    x = 10
    y = 5
    total = soma(x, y)
    print(f"Total: {total}")

main()
```

Durante a execução, você verá algo assim no terminal:

```
> arquivo.py(9)main()
-> x = 10
(Pdb)
```

Você pode digitar os comandos diretamente, como:

```bash
(Pdb) n
(Pdb) p x
(Pdb) s
```

---

## 🦝 Explorando Objetos com `dir()` no PDB

O comando `dir()` é muito útil no PDB para descobrir quais atributos e métodos estão disponíveis em um objeto.

### ✅ Exemplo:

```bash
(Pdb) nome = "Python"
(Pdb) dir(nome)
```

Isso retornará algo como:

```
['__add__', '__class__', '__contains__', ..., 'upper', 'zfill']
```

Com isso, você pode testar os métodos diretamente no debug:

```bash
(Pdb) nome.upper()
'PYTHON'
(Pdb) nome.startswith("Py")
True
```

Esse recurso é excelente para **explorar comportamentos dinamicamente**, principalmente em objetos que você não conhece bem.

---

## 🌟 Benefícios de usar o PDB

- Ajuda a entender **exatamente o que está acontecendo** no código.
- Facilita a **identificação de bugs complexos**.
- Não precisa instalar nada — **já vem com o Python!**
- Ideal para **quem está aprendendo** e deseja enxergar o passo a passo.
- Permite **testar códigos e comandos diretamente** na instância ativa do debug.
- Com `dir()`, é possível **inspecionar qualquer objeto**.

---

## 🚀 Exercício Rápido

**1️⃣ O que será impresso e em que linha o código irá parar?**

```python
def teste_debug():
    nome = "Marlon"
    idade = 30
    import pdb; pdb.set_trace()
    print(nome, idade)

teste_debug()
```

**2️⃣ Use o comando `dir(nome)` no debug para descobrir métodos da string e teste algum.**

---

## 🏆 Conclusão

- O **PDB é um recurso nativo** muito últil para depuração.
- Você pode pausar, inspecionar e controlar a execução do seu programa.
- **Conhecer e praticar com o PDB é um grande diferencial** para quem desenvolve em Python.
- Use o comando `pdb.set_trace()` para começar a explorar o comportamento do seu código de forma interativa.
- Utilize `dir()` para explorar as **propriedades e comportamentos dos objetos** em tempo real.