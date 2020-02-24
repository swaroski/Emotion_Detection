#!/usr/bin/env python
# coding: utf-8

# In[ ]:

'''This file acts as a Kafka consumer for data from VideoProducer.py. The data file is then sent to face_expressions.py file. 
Remember to change KAFKA_HOST port when using on AWS. One can also pass the output to the flask server and display it on the browser'''
#from flask import Flask, Response
from kafka import KafkaConsumer

#data from producer to be consumed and passed through this file
import face_expressions as ver
from json import loads

#consumer = KafkaConsumer('new_topic', bootstrap_servers='54.210.48.50:9092')
KAFKA_HOST = '192.168.99.100:9092'

#app = Flask(__name__)


#def kafkastream():
    #for message in consumer:
        
        #yield (b'--frame\r\n'
               #b'Content-Type: image/jpeg\r\n\r\n' + message.value + b'\r\n\r\n')

def start_consuming():
    consumer = KafkaConsumer('app_messages', bootstrap_servers=KAFKA_HOST, value_deserializer=lambda v: loads(v.decode('utf-8')))

    for msg in consumer:
        file_path = msg.value
        file = file_path.get('data')
        
        ver.gen(file)
            

#@app.route('/')
#def index():
 #   return Response(kafkastream(),
  #                  mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    start_consuming()
