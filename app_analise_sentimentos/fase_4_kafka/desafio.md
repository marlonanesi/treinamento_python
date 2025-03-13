# 🏆 Desafio de Refatoracao

## 🎯 Objetivo

Neste desafio, voce refatorara a aplicacao de **analise de sentimentos** desenvolvida durante o curso, transformando-a em um **CRUD completo**. Para isso, aplicaremos conceitos avancados de **orquestracao**, utilizando **MongoDB, Kafka, Docker e Docker Compose**.

O que voce vai praticar:
- **Programacao Orientada a Objetos (POO)** 🛠️ → Aplicando os principios aprendidos no modulo de Python.
- **Legibilidade e boas praticas** 📌 → Seu codigo deve ser claro e bem estruturado. Caso tenha duvidas, utilize uma **ferramenta de IA** para sugerir melhorias, mas sempre com discernimento critico.
- **Utilizacao de IA como ferramenta auxiliar** 🤖 → IA pode te ajudar, mas a decisao final e o entendimento do codigo sao sempre seus.

💡 **Dica:** Caso queira versionar no Git para revisao, clone o repositorio do curso e crie uma **branch com seu nome**. Se preferir trabalhar localmente sem Git, organize os arquivos dentro de uma pasta nomeada como **fase_4_desafio**.

## 🔥 Proposito do Desafio

A ideia e **evoluir seu senso critico** e aprofundar sua compreensao sobre a orquestracao de aplicacoes de medio porte. Com isso, voce aprendera a:
- Refatorar codigo mantendo a logica original, mas aplicando boas praticas.
- Reutilizar componentes e conceitos ja aprendidos.
- Explorar ferramentas de **Inteligencia Artificial** para aprimorar seu codigo e potencializar sua produtividade.

---

## 🚀 Desafios Disponiveis

### 🛠️ 1. CRUD Sincrono (Sem Kafka)  
Esta versao inicial mantem a comunicacao **direta entre a API e o MongoDB**, sem utilizar mensageria assincrona.

📌 **Objetivo:** Refatorar a aplicacao para um CRUD funcional utilizando **FastAPI** e **Streamlit**.

#### ⚙️ Backend (FastAPI)
- **Criar API para cadastro de usuario (POST)** → Recebe `nome`, `idade` e `login` e persiste no MongoDB.
- **Criar API para consulta de usuarios (GET)** → Retorna todos os usuarios cadastrados.
- **Criar API para atualizacao de usuario (PUT)** → Recebe `ID` e os novos dados (`nome`, `idade`, `login`) e atualiza no banco.
- **Criar API para exclusao de usuario (DELETE)** → Recebe `ID` e remove o usuario do banco.

#### 🎨 Frontend (Streamlit)
- **Tela de Cadastro** → Inputs para `nome`, `idade` e `login`.
- **Aba para Listagem** → Exibe os usuarios cadastrados.
- **Aba para Edicao/Exclusao** → Permite selecionar um usuario pelo `ID`, editar seus dados e confirmar a alteracao ou remocao.

---

### ⚡ 2. CRUD Assincrono (Com Kafka)  
Agora, vamos evoluir para uma arquitetura **event-driven**, onde as operacoes de **cadastro, edicao e exclusao** serao enviadas para um **topico Kafka**, e um **consumidor** processara as mensagens assincronamente.

📌 **Objetivo:** Implementar um CRUD assincrono utilizando Kafka para mensageria.

#### ⚙️ Backend (FastAPI)
- **Criar API para cadastro de usuario (POST)** → Envia `nome`, `idade` e `login` para o topico Kafka `cadastro_usuario`. O **consumer** processara e salvara no banco.
- **Criar API para consulta de usuarios (GET)** → Consulta direta no MongoDB.
- **Criar API para atualizacao de usuario (PUT)** → Envia `ID`, `nome`, `idade` e `login` para o topico `altera_usuario`. O **consumer** processara e atualizara no banco.
- **Criar API para exclusao de usuario (DELETE)** → Envia `ID` para o topico `deleta_usuario`. O **consumer** processara e excluirá do banco.

#### 🎨 Frontend (Streamlit)
- **Tela de Cadastro** → Inputs para `nome`, `idade` e `login`.
- **Aba para Listagem** → Exibe os usuarios cadastrados.
- **Aba para Edicao/Exclusao** → Selecao do usuario pelo `ID`, edicao dos dados e confirmacao da atualizacao.

---

## 📝 Pseudo Codigo - Kafka Consumer  

```python
from confluent_kafka import Consumer, KafkaError, KafkaException

conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'meu_grupo', 'auto.offset.reset': 'earliest'}
consumer = Consumer(conf)
consumer.subscribe(['cadastro_usuario', 'altera_usuario', 'deleta_usuario'])

def process_cadastro_usuario(message):
    print(f'Processando cadastro: {message.value().decode("utf-8")}')

def process_altera_usuario(message):
    print(f'Processando alteracao: {message.value().decode("utf-8")}')

def process_deleta_usuario(message):
    print(f'Processando exclusao: {message.value().decode("utf-8")}')

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        
        if msg.topic() == 'cadastro_usuario':
            process_cadastro_usuario(msg)
        elif msg.topic() == 'altera_usuario':
            process_altera_usuario(msg)
        elif msg.topic() == 'deleta_usuario':
            process_deleta_usuario(msg)

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
```

---

## 🌟 Beneficios da Arquitetura Assincrona  

Optar por uma abordagem assincrona utilizando Kafka traz diversos beneficios para aplicacoes distribuidas:

👉 **Maior Escalabilidade** → Como as operacoes sao processadas independentemente, o sistema pode lidar com alto volume de requisicoes sem sobrecarregar o backend.  
👉 **Melhor Resiliencia** → O uso de filas garante que as mensagens nao sejam perdidas em caso de falha temporaria do sistema.  
👉 **Desacoplamento entre Servicos** → O produtor (API) e o consumidor (banco de dados) operam de forma independente, reduzindo dependencias diretas.  
👉 **Distribuicao de Carga** → Permite escalar consumidores horizontalmente para lidar com grandes volumes de dados.  
👉 **Menor Latencia Percebida** → Como a API apenas enfileira mensagens, as respostas para o cliente sao rapidas.  

Com essa arquitetura, sua aplicacao ganhara **eficiencia, confiabilidade e flexibilidade**, tornando-se mais robusta para lidar com demandas reais em larga escala.  

🚀 **Boa refatoracao e bons estudos!**  
