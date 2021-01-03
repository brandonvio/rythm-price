from src.KafkaUtil import KafkaUtil


k = KafkaUtil()

k.kafka_send({
    "message": "This is a test!"
})
