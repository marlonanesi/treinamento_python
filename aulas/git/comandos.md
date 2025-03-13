# 🐙 Principais Comandos do Git

## 🔹 Configuração Inicial
Antes de começar a usar o Git, configure seu nome e e-mail:
```sh
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```
Verificar configurações do Git:
```sh
git config --list
```

---

## 📂 Criando e Clonando Repositórios

### Criar um novo repositório Git:
```sh
git init
```

### Clonar um repositório existente:
```sh
git clone https://github.com/usuario/repositorio.git
```

---

## 🚀 Fluxo Básico de Versionamento

### Verificar o status do repositório:
```sh
git status
```

### Adicionar arquivos ao controle de versão:
```sh
git add nome_do_arquivo
```
Adicionar todos os arquivos alterados:
```sh
git add .
```

### Criar um commit com as mudanças:
```sh
git commit -m "Mensagem descritiva da alteração"
```

### Enviar as mudanças para o repositório remoto:
```sh
git push origin main
```

### Baixar alterações do repositório remoto:
```sh
git pull origin main
```

---

## 🔀 Trabalhando com Branches

### Criar uma nova branch:
```sh
git branch nome-da-branch
```

### Listar todas as branches:
```sh
git branch
```

### Alternar para outra branch:
```sh
git checkout nome-da-branch
```

### Criar e mudar para uma nova branch ao mesmo tempo:
```sh
git checkout -b nome-da-branch
```

### Mesclar uma branch na main:
```sh
git checkout main
git merge nome-da-branch
```

### Remover uma branch local:
```sh
git branch -d nome-da-branch
```

### Remover uma branch remota:
```sh
git push origin --delete nome-da-branch
```

---

## 📌 Visualização e Histórico

### Ver histórico de commits:
```sh
git log
```

### Ver histórico compacto em uma linha:
```sh
git log --oneline --graph --decorate --all
```

### Ver diferenças entre commits:
```sh
git diff
```

### Ver diferenças entre um arquivo modificado e a versão commitada:
```sh
git diff nome_do_arquivo
```

---

## 🛠️ Comandos Avançados

### Alterar a mensagem do último commit:
```sh
git commit --amend -m "Nova mensagem do commit"
```

### Desfazer um commit sem perder as alterações:
```sh
git reset --soft HEAD~1
```

### Desfazer um commit e descartar as alterações:
```sh
git reset --hard HEAD~1
```

### Reverter um commit específico:
```sh
git revert ID_DO_COMMIT
```

### Criar um stash (guardar temporariamente mudanças não commitadas):
```sh
git stash
```

### Aplicar um stash salvo:
```sh
git stash pop
```

### Excluir um stash salvo:
```sh
git stash drop
```

---

## 🚀 Trabalhando com Tags

### Criar uma nova tag:
```sh
git tag -a v1.0 -m "Versão 1.0"
```

### Listar todas as tags:
```sh
git tag
```

### Enviar tags para o repositório remoto:
```sh
git push origin --tags
```

---

## 📌 Conclusão

Agora você tem um guia com os principais comandos do Git, desde os mais básicos até os mais avançados. Com esse conhecimento, você poderá gerenciar repositórios, versionar código e colaborar em projetos de forma eficiente!

🐙 **Bons estudos!** 🚀
