import pandas as pd
import threading
import uuid
import simplejson as json
from pathlib import Path
from kafka import KafkaProducer, KafkaConsumer
from time import sleep


PATH = "upload_files/12843b037a874276ab21d61b9beda2e2.webm"
KAFKA_HOST = 'localhost:9092'
#df_test = pd.read_csv(PATH/'adult.test')
# In the real world, the messages would not come with the target/outcome of
# our actions. Here we will keep it and assume that at some point in the
# future we can collect the outcome and monitor how our algorithm is doing
# df_test.drop('income_bracket', axis=1, inplace=True)
#df_test['json'] = df_test.apply(lambda x: x.to_json(), axis=1)
#messages = df_test.json.tolist()


def start_producing():
	producer = KafkaProducer(bootstrap_servers=KAFKA_HOST, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
	for i in range(1):
		message_id = str(uuid.uuid4())
		message = {'request_id': message_id, 'data': PATH}

		producer.send('app_messages', value=message)
		producer.flush()

		print("\033[1;31;40m -- PRODUCER: Sent message with id {}".format(message_id))
		sleep(2)

if __name__ == '__main__':
    start_producing()
