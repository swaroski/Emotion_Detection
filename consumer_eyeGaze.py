

'''This file acts as a Kafka consumer for data from VideoProducer.py. The data file is then sent to eye_gaze_analysis.py file. 
Remember to change KAFKA_HOST port when using on AWS. One can also pass the output to the flask server and display it on the browser'''

#from flask import Flask, Response
from kafka import KafkaConsumer
import eye_gaze_analysis as EG
from json import loads
import utils.s3utils as s3_lib

#consumer = KafkaConsumer('new_topic', bootstrap_servers='54.210.48.50:9092')

#KAFKA_HOST = '34.238.238.18:9092'
KAFKA_HOST = 'localhost:9092'

BUCKET="focusai-private-sb"



#app = Flask(__name__)


#def kafkastream():
    #for message in consumer:
        
        #yield (b'--frame\r\n'
               #b'Content-Type: image/jpeg\r\n\r\n' + message.value + b'\r\n\r\n')

def start_consuming():
    consumer = KafkaConsumer('app_messages', bootstrap_servers=KAFKA_HOST, value_deserializer=lambda v: loads(v.decode('utf-8')))

    for msg in consumer:
        print("Message in consumer: ", msg)
        file_path = msg.value
        file = file_path.get('data')
        print("The data path is : ", file)
        #Look for this file in S3, and download it to /downloads folder
        download_file =   "./downloads/" + file
        s3_lib.download_file_local(file, BUCKET, download_file)
        EG.run_tracker(download_file)
            

#@app.route('/')
#def index():
 #   return Response(kafkastream(),
  #                  mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    start_consuming()
