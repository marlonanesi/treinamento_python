# 📘 PDB - Guia de Comandos Interativos

Este documento serve como **referência rápida** dos principais comandos do `pdb`, o depurador nativo do Python. Ideal para consultas durante o uso da ferramenta.

---

## 🧭 Comandos Fundamentais

| Comando       | Descrição                                                                 |
|---------------|---------------------------------------------------------------------------|
| `n`           | Executa a **próxima linha** do código                                     |
| `s`           | Entra na função chamada na linha atual                                     |
| `c`           | Continua a execução até o próximo breakpoint                               |
| `r`           | Continua a execução até sair da função atual                              |
| `q`           | Sai do modo de debug                                                      |
| `l`           | Lista as próximas linhas do código                                        |
| `b [linha]`   | Cria um breakpoint na linha especificada                                  |
| `cl [linha]`  | Remove breakpoint da linha                                                |
| `disable [n]` | Desabilita o breakpoint de número `n`                                     |
| `enable [n]`  | Reabilita o breakpoint de número `n`                                      |
| `p <expr>`    | Avalia e imprime a expressão Python `<expr>`                              |
| `!<comando>`  | Executa comandos arbitrários do Python (ex: `!x = 42`)                    |
| `a`           | Mostra os argumentos da função atual                                      |
| `retval`      | Mostra o valor de retorno da última função                                |

---

## 🔍 Exploração de Objetos e Testes

Esses comandos ajudam a **investigar e testar objetos** em tempo real:

### ▶️ `dir(obj)`
Lista os **atributos e métodos** disponíveis de um objeto.

```bash
(Pdb) dir(nome)
```

### 🧾 `help(obj)`
Mostra a documentação de um método ou objeto.

```bash
(Pdb) help(nome.upper)
```

### 🧪 `!comando`
Permite executar **qualquer comando Python** diretamente no contexto atual:

```bash
(Pdb) !nome = nome.upper()
(Pdb) !print(nome)
```

Você pode:
- Criar novas variáveis
- Alterar valores existentes
- Executar funções manualmente

---

## 🧠 Dicas Avançadas

- Você pode usar `condition` em breakpoints:
  ```bash
  (Pdb) b 12, x > 10
  ```
- Para ver os breakpoints atuais:
  ```bash
  (Pdb) b
  ```
- Para exibir o stack trace:
  ```bash
  (Pdb) where
  ```

---

## 📌 Recomendação

Sempre que estiver **em dúvida sobre um objeto**, use:

```bash
(Pdb) dir(obj)
(Pdb) help(obj.algum_metodo)
```

Esses dois comandos ajudam a entender **o que é possível fazer** com o objeto em questão.

---

## ✅ Exemplo Rápido:

```python
def saudacao(nome):
    import pdb; pdb.set_trace()
    mensagem = f"Olá, {nome.upper()}!"
    return mensagem

print(saudacao("Marlon"))
```

Durante o debug, você pode digitar:

```bash
(Pdb) dir(nome)
(Pdb) help(nome.upper)
(Pdb) !nome = nome.lower()
(Pdb) !print(nome)
(Pdb) c
```

---
