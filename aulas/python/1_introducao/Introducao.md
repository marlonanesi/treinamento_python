# 📝 Introdução ao Python  

---

## 📌 O que é Python? 
Python é uma linguagem de programação **de alto nível**, **interpretada** e **de propósito geral**. Foi criada por **Guido van Rossum** e lançada em **1991**.  

O nome "Python" foi inspirado no grupo de comédia britânico **Monty Python**, refletindo a simplicidade e leveza da linguagem.  

✔️ **Fácil de aprender** – Código limpo e intuitivo  
✔️ **Alta legibilidade** – Usa indentação obrigatória para estruturação  
✔️ **Executado em tempo real** – Interpretado, sem necessidade de compilação  
✔️ **Extremamente popular** – Usado em diversas áreas, como ciência de dados e IA 
---

## 📌 Características Técnicas do Python

### 🔹  Linguagem Interpretada
Python é uma linguagem interpretada, o que significa que o código é executado linha por linha por um interpretador, em vez de ser compilado em um arquivo binário antes da execução. Isso traz algumas vantagens:

- **Depuração facilitada**: Como o código é executado linha a linha, é mais fácil identificar e corrigir erros. Se houver um erro em uma linha, o interpretador para a execução e aponta exatamente onde está o problema. **[DIFERENCIAL]** do curso - Aprenderemos a usar o debug nativo do Python!
- **Portabilidade**: Código Python pode ser executado em qualquer sistema que tenha um interpretador Python instalado, sem necessidade de recompilação.
- **Desenvolvimento rápido**: A ausência de um passo de compilação permite testar e iterar rapidamente.

### 🔹Indentação e Blocos de Código  

Diferente de linguagens como C e Java, que usam `{}` para delimitar blocos, **Python utiliza a indentação obrigatória para definir a estrutura do código**.  

🚨 **Erro comum:** Se a indentação estiver incorreta, o código **não executará**!  

**✅ Exemplo correto:**  

```python
if 5 > 3:
    print("5 é maior que 3")  # Código indentado corretamente
```

📌 **Saída:**  
```
5 é maior que 3
```

**❌ Exemplo incorreto:**  

```python
if 5 > 3:
print("Erro!")  # Falta de indentação gera erro
```

📌 **Erro gerado:**  
```
IndentationError: expected an indented block
```

📌 **Importante:**  
- O **padrão de indentação** recomendado para Python é **4 espaços por nível**.  
- **Não misture TAB e espaços** para evitar erros.  

---

### 🔹Tipagem Dinâmica
Python é uma linguagem de tipagem dinâmica, o que significa que você não precisa declarar o tipo de uma variável ao criá-la. O interpretador infere o tipo com base no valor atribuído. Por exemplo:
- x = 10        # x é um inteiro
- x = "Python"  # Agora x é uma string

### 🔹Gerenciamento Automático de Memória

Python utiliza um sistema de coleta de lixo (garbage collection) para gerenciar automaticamente a alocação e liberação de memória. Isso reduz a complexidade do código e evita vazamentos de memória.

---

## 📌 Multiplataforma

Python é compatível com diversos sistemas operacionais, como Windows, Linux e macOS. Isso permite que programas escritos em Python sejam executados em diferentes ambientes sem modificações.

---

## 📌 Como surgiu o Python?

A história do Python começou no final dos anos 1980, quando Guido van Rossum estava trabalhando no Centro de Matemática e Informática (CWI) na Holanda. Ele queria criar uma linguagem que fosse fácil de ler, escrever e manter, combinando a capacidade de scripting com a robustez de uma linguagem de programação estruturada.

A primeira versão do Python, 0.9.0, foi lançada em 1991. Desde então, a linguagem evoluiu significativamente, com a versão 2.0 sendo lançada em 2000 e a versão 3.0 em 2008. A versão 3.x trouxe mudanças importantes para melhorar a consistência e remover redundâncias, mas também criou uma divisão entre o Python 2 e o Python 3, já que eles não são totalmente compatíveis.

---

## 📌 Para onde o Python foi?

Python se tornou uma das linguagens de programação mais populares do mundo, sendo amplamente utilizada em diversas áreas:

- **Desenvolvimento Web**: Frameworks como Django e Flask permitem criar aplicações web robustas e escaláveis.
- **Ciência de Dados**: Bibliotecas como Pandas, NumPy e Matplotlib são essenciais para análise e visualização de dados.
- **Machine Learning e IA**: TensorFlow, PyTorch e Scikit-learn são ferramentas poderosas para inteligência artificial.
- **Automatização e Scripting**: Python é frequentemente usado para automatizar tarefas repetitivas, como manipulação de arquivos e scraping de dados.
- **Jogos e Gráficos**: Com bibliotecas como Pygame, é possível criar jogos simples e aplicações gráficas.

A comunidade Python é uma das mais ativas do mundo, contribuindo com milhares de bibliotecas e frameworks que tornam a linguagem ainda mais poderosa e versátil.

---

## 📌 Instalação e primeiros passos

### 🔹1. Instalação do Python

Para começar a usar Python, você precisa instalá-lo no seu sistema. Siga os passos abaixo:

- **Linux/Mac**: Python geralmente já vem pré-instalado. Para verificar, abra o terminal e digite: `python3 --version`
- **Windows**:
  1. Acesse o site oficial [python.org](https://www.python.org/downloads/), baixe o instalador e execute-o.
  2. **Muito importante**: Durante a instalação, **marque a opção "Add Python to PATH"** antes de clicar em "Install Now".
  3. Após a instalação, abra o prompt de comando (`cmd`) e digite:
     ```sh
     python --version
     ```
     Se a versão do Python for exibida, a instalação foi concluída com sucesso.

  **Caso o comando não funcione**, siga os passos abaixo para adicionar o Python manualmente às variáveis do sistema:
  1. Pressione `Win + R`, digite `sysdm.cpl` e pressione Enter.
  2. Vá até a aba **"Avançado"** e clique em **"Variáveis de ambiente"**.
  3. Em **"Variáveis do sistema"**, encontre a variável `Path` e clique em **"Editar"**.
  4. Clique em **"Novo"** e adicione o caminho onde o Python foi instalado, normalmente:
     ```
     C:\Users\SeuUsuario\AppData\Local\Programs\Python\PythonXX\
     C:\Users\SeuUsuario\AppData\Local\Programs\Python\PythonXX\Scripts\
     ```
     (Substitua `PythonXX` pela versão instalada)
  5. Clique em **"OK"** em todas as janelas e reinicie o terminal.

  Agora, você pode executar Python diretamente no terminal com:
  python arquivo.py


### 🔹2. Instalação do VSCode

Visual Studio Code (VSCode) é um editor de código leve mas poderoso, que suporta uma variedade de linguagens de programação e ferramentas. Siga as instruções abaixo para instalar o VSCode em diferentes sistemas operacionais:

#### 🔹Windows:
- Acesse [code.visualstudio.com](https://code.visualstudio.com/).
- Clique no botão de download para Windows e salve o arquivo de instalação.
- Execute o instalador e siga as instruções na tela para completar a instalação.

#### 🔹Linux:
- Acesse [code.visualstudio.com](https://code.visualstudio.com/).
- Escolha a opção de download para Linux (deb, rpm, tar.gz, dependendo da sua distribuição).
- Para distribuições baseadas em Debian/Ubuntu:
  - Baixe o arquivo .deb.
  - Abra o terminal e navegue até o diretório onde o arquivo foi salvo.
  - Instale com o comando `sudo dpkg -i <nome_do_arquivo>.deb` e depois `sudo apt-get install -f`.
- Para distribuições baseadas em Red Hat/Fedora:
  - Baixe o arquivo .rpm.
  - Use o comando `sudo rpm -i <nome_do_arquivo>.rpm` no terminal para instalar.

#### 🔹macOS:
- Acesse [code.visualstudio.com](https://code.visualstudio.com/).
- Clique no botão de download para macOS.
- Abra o arquivo .zip baixado e arraste o Visual Studio Code para a pasta Aplicações.
- Abra o VSCode da pasta Aplicações.

---

### 🔹Mudando o Idioma do VSCode para Português

Se desejar alterar o idioma padrão do VSCode para português, siga estes passos:

1. Abra o VSCode.
2. Vá em `View` > `Command Palette...` ou pressione `Ctrl+Shift+P` no Windows/Linux ou `Cmd+Shift+P` no macOS.
3. Digite `Configure Display Language` e selecione a opção.
4. Procure por `Portuguese` (Português) e selecione o idioma desejado, como `Portuguese (Brazil)` ou `Portuguese (Portugal)`.
5. O VSCode solicitará que você reinicie o editor para aplicar a mudança.
---

### 🔹3. Instalação do Docker (não necessário na fase inicial do curso, mas posteriormente sim)

Docker é uma plataforma que permite desenvolver, testar e executar aplicações em contêineres, facilitando a gestão de dependências e ambientes. Para instalar o Docker nos diferentes sistemas operacionais, siga estas instruções:

#### 🔹Windows:
- Acesse docker.com e baixe o Docker Desktop para Windows.
- Execute o instalador baixado e siga as instruções na tela. Pode ser necessário habilitar a virtualização no BIOS do seu computador, se ainda não estiver ativada.
- Após a instalação, reinicie seu computador para concluir a configuração do Docker.

#### 🔹Linux:
- Acesse docker.com e escolha a versão adequada para a sua distribuição Linux.
- Use o gerenciador de pacotes da sua distribuição para instalar o Docker. Por exemplo, no Ubuntu, você poderia usar os comandos:
  - sudo apt update
  - sudo apt install docker-ce docker-ce-cli containerd.io
- Habilite e inicie o serviço Docker com:
  - sudo systemctl enable docker
  - sudo systemctl start docker

#### 🔹macOS:
- Acesse docker.com e baixe o Docker Desktop para macOS.
- Abra o arquivo .dmg baixado e arraste o Docker para a pasta Aplicações.
- Abra o Docker a partir da pasta Aplicações. Você precisará autorizar o Docker e possivelmente inserir sua senha de administrador.
- Siga as instruções na tela para completar a instalação.

---
### 🔹4. Instalação do Git (não necessário na fase inicial do curso, mas posteriormente sim)

Git é uma ferramenta fundamental para o controle de versão e colaboração em projetos de desenvolvimento de software, permitindo que você trabalhe eficazmente com repositórios no GitHub. Para instalar o Git nos diferentes sistemas operacionais, siga estas instruções:

#### 🔹Windows:
- Acesse [git-scm.com](https://git-scm.com/) e baixe o instalador do Git para Windows.
- Execute o instalador baixado e siga as instruções na tela, escolhendo as configurações que melhor atendem às suas necessidades (padrões geralmente são adequados).
- Após a instalação, você pode verificar se foi bem-sucedida abrindo o prompt de comando ou o Git Bash e digitando: `git --version`

#### 🔹Linux:
- Git geralmente está disponível nos repositórios padrão da maioria das distribuições Linux. Você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu, você pode usar os seguintes comandos:
  - `sudo apt update`
  - `sudo apt install git`
- Verifique a instalação com o comando: `git --version`

#### 🔹macOS:
- O Git pode ser instalado no macOS usando o Homebrew, um gerenciador de pacotes para macOS. Se o Homebrew ainda não estiver instalado, você pode instalá-lo primeiro com o comando: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Com o Homebrew instalado, instale o Git com o comando: `brew install git`
- Verifique a instalação com: `git --version`

---

### 🔹4.1 Começando com o GitHub e Git

O GitHub é uma plataforma de hospedagem de código para controle de versão e colaboração. Permite que você e outros trabalhem juntos em projetos de qualquer lugar. Seguem os passos para começar a usar o GitHub e o Git:

#### 🔹Criar uma conta no GitHub
- Acesse [github.com](https://github.com/).
- Clique em "Sign up" e siga as instruções para criar uma nova conta.
- Escolha o plano gratuito, a menos que você precise de recursos adicionais oferecidos nos planos pagos.

#### 🔹Configurar Git
Após instalar o Git, você precisa configurá-lo para uso:
- Abra o terminal ou o Git Bash no Windows.
- Configure seu nome de usuário do GitHub:
  - `git config --global user.name "seu_nome_de_usuario"`
- Configure seu email do GitHub:
  - `git config --global user.email "seu_email@exemplo.com"`
- (Opcional) Para facilitar o uso do Git sem precisar digitar sua senha do GitHub a cada push, você pode configurar o armazenamento de credenciais:
  - `git config --global credential.helper store`

#### 🔹Clonar um repositório
Para começar a trabalhar em um projeto existente:
- Encontre o repositório no GitHub e copie o URL do repositório.
- Abra o terminal e digite:
  - `git clone url_do_repositório`
- Isso criará uma cópia local do repositório em sua máquina.

#### 🔹Principais comandos do Git

- `git add`
  - Adiciona um ou mais arquivos modificados ao stage (área de preparação) para serem incluídos no próximo commit.
  - Uso: `git add <nome_do_arquivo>` ou `git add .` para adicionar todos os arquivos modificados.

- `git commit`
  - Salva as alterações feitas nos arquivos no repositório local. Cada commit deve ser acompanhado de uma mensagem explicativa.
  - Uso: `git commit -m "mensagem explicativa sobre o commit"`

- `git push`
  - Envia as alterações feitas e commitadas no seu repositório local para o repositório remoto no GitHub.
  - Uso: `git push origin main` (assumindo que 'main' é o nome da sua branch principal).

- `git pull`
  - Atualiza seu repositório local com a versão mais recente do repositório remoto.
  - Uso: `git pull origin main`

- `git checkout`
  - Permite trocar de branch ou criar uma nova branch e trocar para ela.
  - Para trocar para uma branch existente: `git checkout nome_da_branch`
  - Para criar uma nova branch e trocar para ela: `git checkout -b nova_branch`
  - Esse comando é crucial para trabalhar em diferentes funcionalidades ou correções sem interferir com a linha principal de desenvolvimento (main).

---

## 📌 Extensões Recomendadas no VSCode

Para maximizar a produtividade e facilitar o desenvolvimento no VSCode, recomendamos instalar as seguintes extensões. Elas são particularmente úteis para trabalhar com Python, Docker e para obter assistência de codificação avançada com o GitHub Copilot, além de facilitar o versionamento e análise com o Git.

### 🔹1. Extensão Python

A extensão Python da Microsoft oferece suporte poderoso para desenvolvimento em Python, incluindo:

- Intellisense (autocompletar, incluindo sugestões de código e parâmetros).
- Linting (análise de código para potenciais erros).
- Formatação de código (ajusta o estilo do código automaticamente).

Para instalar:
- Abra o VSCode, vá até a aba de "Extensões" e procure por `Python`.
- Clique em "Instalar" na extensão da Microsoft.

### 🔹2. Extensão Docker

A extensão Docker facilita o gerenciamento de contêineres Docker diretamente do VSCode, permitindo:

- Construir, gerenciar e implantar contêineres Docker.
- Visualizar logs de contêineres.
- Compor arquivos Docker e executar serviços Docker Compose.

Para instalar:
- Abra o VSCode, vá até a aba de "Extensões" e procure por `Docker`.
- Clique em "Instalar" na extensão oficial da Microsoft.

### 🔹3. GitHub Copilot (caso possua acesso free ou a um plano pago)

O GitHub Copilot é uma ferramenta de codificação assistida por IA, que sugere linhas inteiras ou blocos de código conforme você digita. É especialmente útil para aprender novos padrões e solucionar problemas complexos mais rapidamente.

Para instalar:
- Abra o VSCode, vá até a aba de "Extensões" e procure por `GitHub Copilot`.
- Clique em "Instalar".
- Nota: O GitHub Copilot requer uma assinatura, mas você pode testá-lo durante um período de avaliação gratuito ou acessar através de planos educacionais, se disponíveis.

### 🔹4. Git History

Git History permite visualizar o histórico de commits de um repositório Git de maneira detalhada e gráfica.

Para instalar:
- Abra o VSCode, vá até a aba de "Extensões" e procure por `Git History`.
- Clique em "Instalar".

### 🔹5. GitLens

GitLens supera os recursos padrão de Git do VSCode, ampliando a funcionalidade com visualizações sofisticadas de histórico de arquivos, insights de linha por linha, e muito mais.

Para instalar:
- Abra o VSCode, vá até a aba de "Extensões" e procure por `GitLens`.
- Clique em "Instalar".

Essas extensões são escolhidas para complementar suas atividades de desenvolvimento e aprendizado no curso, tornando a experiência mais interativa e produtiva.

---
---
# [REFLEXÃO] Escolha da melhor linguagem de programação (comparação com C++, Java e Python)

## 📌 Performance vs. Simplicidade

- **C++** oferece a maior performance entre as três linguagens, sendo amplamente utilizada em aplicações que exigem alto desempenho e controle de hardware, como sistemas embarcados, jogos e computação científica. No entanto, exige mais gerenciamento manual de memória e um nível maior de complexidade no desenvolvimento.

- **Java** equilibra performance e facilidade de uso, sendo muito utilizado em sistemas empresariais, aplicações web escaláveis e serviços financeiros. Oferece um modelo de gerenciamento de memória automático (Garbage Collector) e uma ampla compatibilidade com diferentes ambientes, tornando-se uma escolha robusta para aplicações de médio a grande porte.

- **Python**, embora tenha menor performance bruta em comparação a C++ e Java, se destaca pela simplicidade e velocidade de desenvolvimento. É ideal para prototipagem rápida, ciência de dados, automação e aplicações onde a facilidade de manutenção e desenvolvimento são mais importantes que a execução ultra-rápida.

## 📌 Comparação de Performance em Requests por Segundo (RPS)

Os benchmarks abaixo comparam a quantidade de requests processadas por segundo em APIs desenvolvidas em cada linguagem com suas principais bibliotecas:

[Os valores podem variar dependendo do ambiente e configuração, baseando-se em benchmarks como o da TechEmpower e outras medições independentes.]

- **C++ (Crow/Restinio)** → ~10.000 a 15.000 RPS  
- **Java (Spring Boot/Vert.x)** → ~3.772 a 12.782 RPS  
- **Python (FastAPI)** → ~1.103 RPS  
- **Python (Flask)** → ~639 RPS  

> 📝 **Observação**: Os benchmarks podem variar de acordo com o hardware, otimizações aplicadas e perfil da aplicação. Embora C++ e Java apresentem maior throughput, isso nem sempre é determinante. Em muitas aplicações, a escolha de Python pode acelerar o desenvolvimento e reduzir custos operacionais sem que a diferença de performance seja significativa para o uso real.

🔗 **Fontes**: [TechEmpower Benchmarks](https://www.techempower.com/benchmarks/) e comparações independentes disponíveis em comunidades de desenvolvimento.

## 📌 O Papel da Infraestrutura na Performance

A performance da linguagem de programação, por si só, não é o único fator determinante para a escalabilidade e eficiência de um sistema. Fatores como **orquestração da infraestrutura, auto scaling e boas práticas de DevOps** têm um impacto significativo na capacidade de resposta e na eficiência operacional.

- **Infraestrutura bem projetada** (como uso de Kubernetes e arquiteturas serverless) pode compensar diferenças de desempenho entre linguagens.
- **Boas práticas de DevOps**, como otimização de CI/CD, monitoramento e provisionamento eficiente de recursos, garantem que aplicações escalem conforme a demanda.
- **Auto scaling e load balancing** permitem que aplicações desenvolvidas em linguagens com menor throughput individual consigam lidar com grandes volumes de tráfego sem perda perceptível de desempenho.

Por isso, a escolha da linguagem deve ser acompanhada de um planejamento robusto da infraestrutura, garantindo que a aplicação possa crescer de forma eficiente e sustentável.

## 📌 Conclusão

Enquanto C++ oferece a melhor performance, seu uso é mais indicado para aplicações que exigem controle total de hardware e otimização extrema. Java se posiciona como um meio-termo, equilibrando desempenho e produtividade, sendo ideal para aplicações corporativas escaláveis. Python, por sua vez, se destaca quando o foco está na velocidade de desenvolvimento e facilidade de manutenção.

Além disso, **a infraestrutura e boas práticas de DevOps são fatores críticos para garantir escalabilidade e eficiência**, muitas vezes sendo mais determinantes do que a própria linguagem na capacidade de lidar com altas cargas de requisições.

A melhor linguagem não é aquela com a maior taxa de requisições/processamento por segundo, mas sim a que se alinha melhor com os objetivos do projeto, a experiência da equipe e os requisitos operacionais.  

*(As linguagens citadas foram utilizadas apenas para ilustrar a reflexão, não como uma comparação definitiva.)*  

No fim das contas, não existe uma linguagem "melhor" — existe a linguagem mais adequada para o desafio que você precisa resolver. O segredo está em escolher a ferramenta certa para o trabalho certo! 🚀

## 📖 Documentação Oficial
[Acesse a documentação oficial do Python](https://docs.python.org/3/)
