from kafka import KafkaProducer
import json
from csv import DictReader


def is_valid():
    # tells if the link is valid
    pass


def get_producer() -> KafkaProducer:
    bootstrap_servers = ["kafka"]
    topicname = "linkedin"
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    # producer = KafkaProducer()
    return producer


def send_to_consumer():
    # send data to consumer
    pass


def create_data(n=10):
    # scrape something from linkedin
    cons_error = 0  # consecutive error
    while cons_error != 20:
        if is_valid():
            send_to_consumer()
        else:
            cons_error += 1
        n += 1


if __name__ == "__main__":
    producer = get_producer()
    with open("data.csv") as f:
        csv_dict_reader = DictReader(f)
        for row in csv_dict_reader:
            ack = producer.send(topic="linkedin", value=json.dumps(row).encode("utf-8"))
            metadata = ack.get()

            print(metadata.topic, metadata.partition, metadata)
