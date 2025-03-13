# ✅ Boas Práticas no Uso do Git

## 📌 1. Use Commits Pequenos e Frequentes

- Evite commits gigantes com várias mudanças.
- Pequenos commits facilitam o rastreamento de mudanças e debugging.
- Sempre teste antes de commitar para garantir que o código está funcionando.

## 📌 2. Escreva Mensagens de Commit Claras

- Use mensagens descritivas e curtas.
- O padrão recomendado é:

```sh
git commit -m "feat: adiciona funcionalidade de login com autenticação JWT"
```

## 📌 3. Utilize Padrões de Commit (Conventional Commits)

Formato sugerido:

```
<tipo>: <descrição curta>

[opcional] Descrição mais detalhada se necessário.
```

**Principais tipos de commit:**

| Tipo   | Descrição |
|--------|--------------------------------------------------|
| `feat` | Adiciona uma nova funcionalidade |
| `fix`  | Corrige um bug |
| `docs` | Alterações na documentação |
| `style` | Alterações de formatação, espaços, vírgulas, etc. |
| `refactor` | Refatoração de código sem alteração de funcionalidade |
| `test` | Adição ou modificação de testes |
| `chore` | Alterações de build, dependências, etc. |

**Exemplos:**
```sh
git commit -m "feat: adiciona validação de CPF no cadastro"
git commit -m "fix: corrige erro de login ao inserir senha inválida"
git commit -m "docs: adiciona seção sobre autenticação na documentação"
```

## 📌 4. Sempre Trabalhe com Branches

- Nunca trabalhe diretamente na branch `main` ou `master`.
- Use branches para cada nova funcionalidade ou correção.
- Nomeie as branches de forma descritiva, como:

```sh
git checkout -b feat/autenticacao-jwt
```

## 📌 5. Mantenha o Repositório Atualizado

- Antes de começar a trabalhar, sempre atualize sua branch:

```sh
git pull origin main
```

- Para evitar conflitos, mantenha suas branches sincronizadas.

## 📌 6. Revise Código Antes de Mesclar (Pull Requests)

- Use **Pull Requests (PRs)** para revisões de código antes de mesclar na `main`.
- Sempre peça revisão de outro desenvolvedor antes de fazer merge.

## 📌 7. Evite Commits de Arquivos Sensíveis

- Adicione um `.gitignore` no projeto para evitar commits acidentais de arquivos sensíveis, como:

```
node_modules/
.env
secrets.json
.idea/
.DS_Store
```

## 📌 8. Faça Squash de Commits Sempre que Possível

- Se um PR tiver vários commits pequenos e irrelevantes, use **squash** para mesclá-los em um único commit significativo.

```sh
git rebase -i HEAD~3
```

- Isso melhora a clareza do histórico de commits.

## 📌 9. Escreva Pull Requests Claros

- Explique a mudança feita.
- Adicione prints ou logs se necessário.
- Exemplo de descrição de PR:

```
### O que foi feito?
- Implementado sistema de login com JWT.

### Como testar?
- Rodar `npm start` e tentar logar com usuário válido.

### Checklist
- [x] Código revisado
- [x] Testes rodaram sem erro
- [x] PR aprovado por pelo menos um revisor
```

## 📌 10. Mantenha um Histórico de Commits Limpo

- Evite commits como "correção de erro", "teste", "funcionando agora".
- Se necessário, reescreva a história do Git para limpar commits desnecessários:

```sh
git rebase -i HEAD~5
```

---

## ✅ Conclusão

Seguir boas práticas no Git melhora a colaboração, torna o código mais organizado e reduz problemas em equipes. Use commits claros, siga um fluxo de branches bem definido e mantenha um histórico de alterações limpo! 🚀

🔹 **Dúvidas? Comente e participe!**

🐙 **Bons estudos!**
