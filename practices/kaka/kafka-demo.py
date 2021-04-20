from kafka import KafkaProducer, KafkaAdminClient
from kafka.errors import KafkaError
from kafka.admin import NewTopic

localHost = "127.0.0.1:9092"
devHost = "172.31.103.161:9092"


class Demo:
    producer = None
    adminClient = None

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=[devHost])
        if self.producer:
            print("producer init success")
        # self.adminClient = KafkaAdminClient(bootstrap_servers=[localHost])
        # topics = self.adminClient.list_topics()
        #
        # topic = NewTopic(name="scv-log-transfer", num_partitions=1, replication_factor=1)
        # self.adminClient.create_topics(new_topics=[topic])

    def test(self):
        fut = self.producer.send("scv-log-transfer", value="test kafka from python".encode("utf-8"))
        try:
            record_metadata = fut.get(timeout=10)

            print(record_metadata)
        except KafkaError as e:
            print(e)
            pass


if __name__ == '__main__':
    d = Demo()
    for i in range(10):
        d.test()
