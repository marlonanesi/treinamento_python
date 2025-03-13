# 🐳 Comandos Essenciais do Docker

## 🔍 Visualizando Containers

### Listar containers ativos:
```sh
docker ps
```
Este comando exibe todos os containers em execução, mostrando informações como ID, nome, status e portas expostas.

### Listar todos os containers (ativos e parados):
```sh
docker ps -a
```
Diferente do `docker ps`, este comando também mostra containers que já foram encerrados.

---

## ▶️ Iniciando e Parando Containers

### Iniciar um container parado:
```sh
docker start nome_do_container
```
Se um container foi interrompido, este comando o reativa.

### Parar um container em execução:
```sh
docker stop nome_do_container
```
Isso encerra um container de maneira segura.

### Reiniciar um container:
```sh
docker restart nome_do_container
```
Isso para e inicia novamente um container em uma única operação.

---

## 🗑️ Removendo Containers

### Remover um container específico:
```sh
docker rm nome_do_container
```
Este comando exclui um container parado. Para remover um container em execução, primeiro é necessário pará-lo (`docker stop`).

### Remover todos os containers parados:
```sh
docker container prune
```
Isso limpa todos os containers que não estão em execução.

---

## 🔨 Construindo e Atualizando Imagens

### Criar uma nova imagem a partir de um `Dockerfile`:
```sh
docker build -t nome_da_imagem .
```
Explicação:
- `-t nome_da_imagem` → Nomeia a imagem gerada.
- `.` → Define que o Dockerfile está no diretório atual.

### Atualizar um container após mudanças no código:
1. **Reconstruir a imagem:**
   ```sh
   docker build -t nome_da_imagem .
   ```
2. **Remover o container antigo:**
   ```sh
   docker rm -f nome_do_container
   ```
3. **Criar um novo container com a imagem atualizada:**
   ```sh
   docker run -d --name nome_do_container -p 8000:8000 nome_da_imagem
   ```

---

## 🗂️ Trabalhando com Docker Compose

### Subir múltiplos containers definidos no `docker-compose.yml`:
```sh
docker-compose up -d
```
Explicação:
- `-d` → Roda os containers em background.
- O Docker Compose iniciará todos os serviços definidos no arquivo `docker-compose.yml`.

### Parar os serviços do Docker Compose:
```sh
docker-compose down
```
Isso interrompe e remove os containers gerenciados pelo Compose.

### Reiniciar os serviços:
```sh
docker-compose restart
```
Se precisar recarregar alguma configuração sem derrubar os containers, use esse comando.

### Ver logs dos serviços:
```sh
docker-compose logs -f
```
Monitoramento em tempo real dos logs gerados pelos containers.

---

## 📌 Conclusão

Agora você conhece os principais comandos do Docker! Com essas ferramentas, você pode gerenciar containers, reconstruir imagens e utilizar Docker Compose para gerenciar múltiplos serviços de forma eficiente. 🚀

🐳 **Bons estudos!**