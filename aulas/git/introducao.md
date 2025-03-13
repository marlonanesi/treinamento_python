# 🚀 Introdução ao Git

## 📌 O que é o Git?

Git é um **sistema de controle de versão distribuído** que permite acompanhar mudanças no código, colaborar com outros desenvolvedores e manter um histórico seguro das alterações. Ele foi criado por **Linus Torvalds** (o mesmo criador do Linux) e se tornou o padrão da indústria para controle de versão.

Com o Git, podemos:
- **Salvar e recuperar versões do código** 📂
- **Trabalhar em equipe sem conflitos** 🤝
- **Manter um histórico completo das alterações** 📜
- **Experimentar novas funcionalidades sem comprometer o código principal** 🛠️

---

## 🎯 Benefícios do Versionamento com Git

✅ **Histórico de alterações** → Você pode voltar para qualquer versão anterior do código.  
✅ **Colaboração eficiente** → Vários desenvolvedores podem trabalhar no mesmo projeto sem sobrescrever mudanças.  
✅ **Segurança e rastreabilidade** → Todas as modificações são registradas, permitindo rastrear quem fez o quê.  
✅ **Desenvolvimento em paralelo** → Permite criar branches (ramificações) para testar novas funcionalidades sem afetar o código principal.  
✅ **Facilidade de recuperação** → Se algo der errado, é possível reverter para uma versão anterior.

---

## 🏗️ Principais Comandos do Git

### 🔹 Configuração Inicial
Antes de começar a usar o Git, configure seu nome e e-mail:
```sh
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

### 🔹 Criando ou Clonando um Repositório
Criar um novo repositório Git:
```sh
git init
```

Clonar um repositório existente:
```sh
git clone https://github.com/usuario/repositorio.git
```

### 🔹 Fluxo Básico de Versionamento
Adicionar arquivos ao controle de versão:
```sh
git add .
```
Criar um commit com as mudanças:
```sh
git commit -m "Mensagem descritiva da alteração"
```
Enviar as mudanças para o repositório remoto:
```sh
git push origin main
```
Baixar as alterações do repositório remoto:
```sh
git pull origin main
```

---

## 🔄 Estratégias de Versionamento

### 🔹 **Git Flow**
Uma das estratégias mais populares, onde há um fluxo definido com branches específicas:
- **main** → Contém a versão estável do projeto.
- **develop** → Contém o código em desenvolvimento.
- **feature branches** → Criadas a partir do develop para novas funcionalidades.
- **release branches** → Criadas quando uma versão está prestes a ser lançada.
- **hotfix branches** → Criadas para corrigir bugs críticos diretamente na main.

### 🔹 **GitHub Flow**
Um fluxo mais simplificado usado por equipes ágeis:
- Tudo acontece na **main**.
- Cada nova funcionalidade ou correção é feita em um **branch separado**.
- Quando pronto, um **Pull Request** (PR) é aberto para revisão.
- Após a aprovação, o código é mesclado na **main**.

### 🔹 **Trunk-Based Development**
- Todos os desenvolvedores fazem commits diretamente em um único branch principal.
- Pequenas mudanças são integradas continuamente.
- Ideal para equipes que utilizam **CI/CD (Continuous Integration / Continuous Deployment)**.

---

## ✅ Conclusão

O Git é uma ferramenta essencial para o desenvolvimento de software moderno. Ele permite versionar código de forma segura, colaborar em equipe e testar novas funcionalidades sem comprometer a base do projeto.

Escolher a estratégia de versionamento correta depende do tamanho do time e do fluxo de desenvolvimento, mas todas compartilham o mesmo objetivo: manter o código organizado e confiável.

🚀 **Bons estudos!**
