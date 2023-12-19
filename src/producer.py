from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin.new_partitions import NewPartitions
import json
from csv import DictReader


def is_valid():
    # tells if the link is valid
    pass


def key_divider(*args, **kwargs):
    print(args)
    print(kwargs)


# def get_producer() -> KafkaProducer:
#     client = KafkaAdminClient(bootstrap_servers="kafka")
#     topic_name = "linkedin"
#     new_partition_count = 2

#     rsp = client.create_partitions({"linkedin": NewPartitions(2)})
#     return client


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


def send_message():
    pass


class MeinKafkaProducer:
    def __init__(
        self, servers: str | list = "kafka", topic: str = "my_topic", partition: int = 1
    ) -> None:
        self.topic = topic
        self.partition = partition
        self.servers = servers
        self.producer = KafkaProducer(
            bootstrap_servers=self.servers,
            key_serializer=self.key_serializer,
            value_serializer=self.serializer,
            partitioner=self.partitioner,
        )

    def serializer(self, data):
        return json.dumps(data).encode("utf-8")

    def key_serializer(self, data):
        return json.dumps(data).encode("utf-8")

    def partitioner(self, key_bytes, all_partitions, available_partitions):
        key = json.loads(key_bytes)
        return available_partitions[(key % self.partition) - 1]

    def send(self, key, value, **kwargs):
        # self.producer.send(
        #         topic=self.topic, value=json.dumps(row).encode("utf-8"), partition=i % 2
        # )
        return self.producer.send(topic=self.topic, key=key, value=value)


if __name__ == "__main__":
    producer = MeinKafkaProducer("kafka", "linkedin", 2)
    # producer = get_producer()
    i = 0
    with open("data.csv") as f:
        csv_dict_reader = DictReader(f)
        for row in csv_dict_reader:
            ack = producer.send(
                key=i,
                value=row,
            )
            metadata = ack.get()

            print(metadata.topic, metadata.partition, metadata)
            i += 1
