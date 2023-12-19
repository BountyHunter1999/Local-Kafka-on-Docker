from kafka import KafkaConsumer
import json
import sys


def get_consumer() -> KafkaConsumer:
    bootstrap_servers = ["kafka"]
    topicname = "linkedin"
    consumer = KafkaConsumer(
        topicname,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset="earliest",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )
    return consumer


def export_to():
    pass


def consume_data():
    # send data to consumer
    consumer = get_consumer()

    try:
        for message in consumer:
            print("message is: ", message)
            print(message.value)
            print()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    consume_data()
