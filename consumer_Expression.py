#!/usr/bin/env python
# coding: utf-8

# In[ ]:

'''This file acts as a Kafka consumer for data from VideoProducer.py. The data file is then sent to face_expressions.py file. 
Remember to change KAFKA_HOST port when using on AWS. One can also pass the output to the flask server and display it on the browser.

This code is a Kafka consumer that listens for messages on the 'app_messages' topic. When a message is received, it retrieves the 
file path specified in the message and downloads the file from an S3 bucket using the s3_lib.download_file_local function. 
It then calls the ver.gen function with the downloaded file as input.'''
import face_expressions as ver
from json import loads
import utils.s3utils as s3_lib

KAFKA_HOST = 'localhost:9092'
BUCKET = "focusai-private-sb"

def start_consuming():
    consumer = KafkaConsumer('app_messages', bootstrap_servers=KAFKA_HOST, value_deserializer=lambda v: loads(v.decode('utf-8')))
    for msg in consumer:
        file_path = msg.value
        file = file_path.get('data')
        download_file = "./downloads/" + file
        s3_lib.download_file_local(file, BUCKET, download_file)
        ver.gen(download_file)

if __name__ == '__main__':
    start_consuming()



