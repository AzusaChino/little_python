from rocketmq.client import Producer, Message
import json

namesrv = 'localhost:9876'

producer = Producer('PID-test')
producer.set_namesrv_addr(namesrv)
producer.start()

msg_body = {"id": "001", "name": "test_mq", "message": "abcdefg"}
ss = json.dumps(msg_body).encode('utf-8')

msg = Message('topic_name')
# msg.set_keys('xxxxxx')
# msg.set_tags('xxxxxx')
msg.set_body(ss)  # message body

retmq = producer.send_sync(msg)
print(retmq.status, retmq.msg_id, retmq.offset)
producer.shutdown()
