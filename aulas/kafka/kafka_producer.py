# Caso não possua a lib confluent_kafka, instale com: pip install confluent_kafka
import time
import json
from confluent_kafka import Producer, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic

DEFAULT_BROKER = "localhost:9092"
TOPIC_NAME = "aula_kafka"

class KafkaFeedbackProducer:
    def __init__(self, broker=DEFAULT_BROKER, topic=TOPIC_NAME):
        self.broker = broker
        self.topic = topic
        self.producer_config = {
            "bootstrap.servers": self.broker,
        }
        self.admin_config = {
            "bootstrap.servers": self.broker,
        }
        self.producer = Producer(self.producer_config)
        self.admin_client = AdminClient(self.admin_config)
        self.ensure_topic_exists()

    def delivery_report(self, err, msg):
        """Callback para reportar o resultado do envio."""
        if err is not None:
            print(f"Falha ao entregar mensagem: {err}")
        else:
            print(f"Mensagem entregue: {msg.topic()} [{msg.partition()}]")

    def ensure_topic_exists(self):
        """Verifica se o tópico existe e o cria caso não exista."""
        topics = self.admin_client.list_topics(timeout=10).topics
        if self.topic in topics:
            print(f"Tópico '{self.topic}' já existe.")
            return

        new_topic = NewTopic(self.topic, num_partitions=1, replication_factor=1)
        fs = self.admin_client.create_topics([new_topic])
        for topic, f in fs.items():
            try:
                f.result()  # aguarda a criação
                print(f"Tópico '{topic}' criado com sucesso.")
            except Exception as e:
                print(f"Falha ao criar o tópico '{topic}': {e}")

    def produce_message(self, message_data: dict):
        """Produz a mensagem convertida em JSON para o tópico."""
        try:
            message = json.dumps(message_data)
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} Produzindo mensagem: {message}")
            self.producer.produce(self.topic, value=message, callback=self.delivery_report)
            # Poll para processar o callback
            self.producer.poll(0)
        except KafkaException as e:
            print(f"Erro ao produzir mensagem: {e}")

    def produce_messages(self, messages):
        """Produz uma lista de mensagens para o tópico."""
        for message in messages:
            self.produce_message(message)
        # Garantir que todas as mensagens sejam enviadas antes de terminar
        self.producer.flush()

if __name__ == "__main__":
    producer = KafkaFeedbackProducer()

    # Lista de dicionários com objetos mockados (pessoas)
    pessoas = [
        {"nome": "Alice", "idade": 30, "cidade": "São Paulo"},
        {"nome": "Bob", "idade": 25, "cidade": "Rio de Janeiro"},
        {"nome": "Carol", "idade": 27, "cidade": "Belo Horizonte"},
        {"nome": "David", "idade": 35, "cidade": "Curitiba"},
        {"nome": "Eve", "idade": 22, "cidade": "Porto Alegre"}
    ] * 200

    # Produzir as mensagens
    producer.produce_messages(pessoas)