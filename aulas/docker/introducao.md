# 🚀 Introdução ao Docker

## 📌 O que é o Docker?

Docker é uma plataforma de **virtualização leve baseada em containers**, permitindo empacotar, distribuir e rodar aplicações de forma **isolada** e **reprodutível**. Ele resolve um problema clássico do desenvolvimento de software:  

> *"Na minha máquina funciona, mas no servidor não!"* 😱

Com Docker, garantimos que a aplicação rode da mesma forma em qualquer ambiente, seja no seu computador, no servidor de produção ou na nuvem.

### 🏗️ Como o Docker funciona?

Docker utiliza **containers**, que são unidades isoladas contendo tudo que uma aplicação precisa para rodar: código, dependências, bibliotecas e variáveis de ambiente. Diferente de máquinas virtuais (VMs), que rodam sistemas operacionais completos, containers compartilham o **kernel do host**, tornando-os mais leves e rápidos.

### 🛠️ Principais Componentes do Docker

- **Docker Engine** → Motor que executa e gerencia os containers.
- **Docker Image** → Imagem imutável que contém a aplicação e suas dependências.
- **Docker Container** → Instância em execução de uma imagem Docker.
- **Dockerfile** → Arquivo que define como uma imagem Docker deve ser construída.
- **Docker Hub** → Repositório de imagens públicas e privadas para compartilhar containers.

---

## 🎯 Por que usar Docker?

- **Portabilidade** → Um container roda em qualquer lugar com Docker instalado.
- **Reprodutibilidade** → Ambiente sempre igual, sem surpresas.
- **Facilidade na configuração** → Tudo configurado em um único arquivo.
- **Rápido para subir e testar aplicações** → Em poucos minutos você tem um banco de dados ou uma aplicação rodando.

---

## 🏗️ Criando um Banco de Dados MySQL no Docker

Para rodar um banco **MySQL** em um container, basta rodar o seguinte comando:

```sh
docker run -d --name meu-mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 mysql:latest
```

Explicação:
- `-d` → Roda o container em background.
- `--name meu-mysql` → Nome do container.
- `-e MYSQL_ROOT_PASSWORD=root` → Define a senha do usuário root.
- `-p 3306:3306` → Mapeia a porta do host para o container.
- `mysql:latest` → Imagem do MySQL mais recente.

Agora, para acessar o banco MySQL dentro do container:
```sh
docker exec -it meu-mysql mysql -u root -p
```
Digite a senha `root` e pronto! Você está dentro do MySQL! 🎉

---

## 🏗️ Criando um Banco NoSQL (MongoDB) no Docker

Agora, vamos rodar um **MongoDB**:

```sh
docker run -d --name meu-mongo -p 27017:27017 mongo:latest
```

Para conectar ao MongoDB dentro do container:
```sh
docker exec -it meu-mongo mongosh
```

Se aparecer o prompt do MongoDB (`>`), significa que está tudo funcionando! 🚀

---

## 📦 Criando um Dockerfile para uma Aplicação Backend Python

Vamos criar um `Dockerfile` para empacotar uma aplicação backend Python:

1️⃣ **Criar um arquivo chamado `Dockerfile` no diretório do projeto:**

```Dockerfile
# Utilizando a imagem oficial do Python como base
FROM python:3.9

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para dentro do container
COPY . .

# Instalar as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Definir a variável de ambiente para desativar buffer de saída do Python
ENV PYTHONUNBUFFERED=1

# Expor a porta 8000 para comunicação
EXPOSE 8000

# Comando de inicialização da aplicação
CMD ["python", "app.py"]
```

2️⃣ **Explicação de cada linha do Dockerfile:**

- `FROM python:3.9` → Utiliza a imagem oficial do Python como base.
- `WORKDIR /app` → Define o diretório de trabalho dentro do container.
- `COPY . .` → Copia todos os arquivos do projeto para dentro do container.
- `RUN pip install --no-cache-dir -r requirements.txt` → Instala as dependências do projeto.
- `ENV PYTHONUNBUFFERED=1` → Evita problemas de buffer no log.
- `EXPOSE 8000` → Expõe a porta 8000 do container para comunicação.
- `CMD ["python", "app.py"]` → Define o comando que será executado ao iniciar o container.

3️⃣ **Construindo a imagem Docker:**

```sh
docker build -t minha-aplicacao-python .
```

4️⃣ **Rodando o container da aplicação:**

```sh
docker run -d -p 8000:8000 minha-aplicacao-python
```

Agora sua aplicação Python está rodando dentro de um container! 🎉

---

## 🗑️ Removendo Containers

Se quiser excluir os containers criados:
```sh
docker rm -f meu-mysql meu-mongo minha-aplicacao-python
```
Isso apagará os containers de forma permanente.

---

## 📋 Introdução ao Docker Compose

Docker Compose permite definir e gerenciar múltiplos containers através de um único arquivo YAML! 

Vamos falar mais sobre **Docker Compose** na próxima aula! 😉

---

## ✅ Conclusão

Agora você já sabe como rodar bancos de dados e aplicações no Docker! Com isso, você pode testar aplicações sem precisar instalar nada no seu sistema. O famoso problema *"Na minha máquina funciona"* não existe mais! 🛠️🔥

🚀 **Bons estudos!**

## 📖 Documentação Oficial
[Acesse a documentação oficial do Docker](https://docs.docker.com/)
