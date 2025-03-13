import json
import time
from kafka import KafkaConsumer

TOPIC_NAME = "aula_kafka"
GROUP_ID = "aula_kafka_group"

def main():
    # Configurando o consumer para o tópico 'feedback' com auto commit desabilitado
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        group_id=GROUP_ID,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("Kafka Consumer iniciado e escutando o tópico kafka...")

    # Loop infinito para processamento contínuo das mensagens
    for message in consumer:
        try:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Nova mensagem recebida: {message.value}")
            # Simula um processamento mais demorado
            #time.sleep(1)
            # Confirma o processamento da mensagem
            consumer.commit()
        except Exception as e:
            print(f"Erro ao processar a mensagem: {e}")

if __name__ == '__main__':
    main()