import json
from kafka import KafkaProducer
from src.EnvUtil import EnvUtil

kafka_sasl_plain_username = EnvUtil.get_secret("confluent_sasl_plain_username")
kafka_sasl_plain_password = EnvUtil.get_secret("confluent_sasl_plain_password")
kafka_bootstrap_servers = EnvUtil.get_env("KAFKA_BOOTSTRAP_SERVERS")
kafka_topic = EnvUtil.get_env("KAFKA_TOPIC")


print("kafka_bootstrap_servers:" + kafka_bootstrap_servers)
print("kafka_topic:" + kafka_topic)


class KafkaUtil:
    def __init__(self) -> None:
        super().__init__()
        self.kafka_producer = KafkaProducer(
            bootstrap_servers=[kafka_bootstrap_servers],
            security_protocol="SASL_SSL",
            sasl_mechanism="PLAIN",
            sasl_plain_username=kafka_sasl_plain_username,
            sasl_plain_password=kafka_sasl_plain_password,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def kafka_send(self, message) -> None:
        self.kafka_producer.send(kafka_topic, value=message)
        self.kafka_producer.flush()
