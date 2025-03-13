# 🚀 Introdução ao Docker Compose

## 📌 O que é o Docker Compose?

Docker Compose é uma ferramenta que permite a **orquestração de múltiplos containers** de forma simples, utilizando um único arquivo YAML (`docker-compose.yml`). Com ele, podemos definir e gerenciar ambientes completos sem precisar rodar manualmente vários comandos `docker run`.

O Compose é muito útil para **aplicações locais**, desenvolvimento e testes, pois permite criar um ambiente padronizado e facilmente replicável.

---

## 🎯 Por que usar Docker Compose?

✅ **Facilidade na configuração** → Em vez de rodar vários comandos, basta um único `docker-compose up` para subir toda a aplicação.  
✅ **Definição centralizada** → Toda a configuração dos containers está em um único arquivo YAML.  
✅ **Portabilidade** → Compartilhe seu ambiente com outras pessoas sem complicação.  
✅ **Automação** → Pode definir volumes, redes e variáveis de ambiente com facilidade.  

---

## 🏗️ Exemplo de Arquivo `docker-compose.yml`

Vamos criar um ambiente com um **banco de dados MySQL** e uma **aplicação Python** que se conecta a ele.

```yaml
version: '3.8'

services:
  db:
    image: mysql:latest
    container_name: meu-mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: minha_app
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

  app:
    build: .
    container_name: minha-aplicacao
    restart: always
    depends_on:
      - db
    ports:
      - "8000:8000"
    environment:
      DB_HOST: db
      DB_USER: root
      DB_PASSWORD: root

volumes:
  db_data:
```

### 🛠️ Explicação:
- **`services`** → Define os containers que serão criados.
- **`db`** → Serviço do banco de dados MySQL.
- **`app`** → Aplicação Python que se conecta ao banco.
- **`depends_on`** → Define que o container `app` só inicia depois do `db`.
- **`volumes`** → Mantém os dados do MySQL mesmo após parar os containers.

---

## ▶️ Executando o Docker Compose

1️⃣ **Subir os serviços:**
```sh
docker-compose up -d
```

2️⃣ **Ver logs dos serviços:**
```sh
docker-compose logs -f
```

3️⃣ **Parar os serviços:**
```sh
docker-compose down
```

4️⃣ **Reiniciar apenas um serviço:**
```sh
docker-compose restart app
```

---

## 🔄 Docker Compose vs Kubernetes

Docker Compose e Kubernetes são **orquestradores**, mas servem para propósitos diferentes:

| Característica       | Docker Compose | Kubernetes |
|----------------------|---------------|------------|
| **Escopo**          | Local / Dev    | Produção / Cloud |
| **Complexidade**    | Simples        | Avançado |
| **Gerenciamento**   | Manual         | Automático |
| **Escalabilidade**  | Limitada       | Alta |
| **Infraestrutura**  | Containers locais | Multi-cluster |

Embora o **Docker Compose seja excelente para desenvolvimento e testes locais**, aplicações que precisam ser escaladas na nuvem geralmente são migradas para **Kubernetes**.

### 🏗️ Como converter Docker Compose para Kubernetes?
- **Containers → Pods** → No Kubernetes, os containers rodam dentro de **Pods**.
- **Volumes → Persistent Volumes** → No Kubernetes, os volumes são gerenciados por meio de recursos como PersistentVolumes.
- **Networking** → No Kubernetes, o tráfego é gerenciado por **Services e Ingress**.
- **Orquestração** → O Compose gerencia containers localmente, enquanto o Kubernetes faz isso em **clusters distribuídos**.

O que realmente leva uma aplicação para a **Cloud** são configurações adicionais de **segurança, rede e balanceamento de carga**, mas a transição de Docker Compose para Kubernetes é relativamente simples!

---

## ✅ Conclusão

Docker Compose é uma ferramenta poderosa para **orquestração local** e desenvolvimento de aplicações com múltiplos containers. Com um único arquivo YAML, você pode definir e rodar **ambientes completos** de forma prática e replicável.

Se sua aplicação precisar escalar para um ambiente **Cloud/Produção**, a transição para **Kubernetes** será natural, pois os conceitos são semelhantes!

🐳 **Bons estudos!** 🚀
