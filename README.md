# Emotion_Detection
This project is built as a final project for AI Deep dive. It consists of the ability for the user to record a user while they are watching a video, movie review, advertisement. The webcam starts simultanoeusly when the video on the browser loads - all happening at inside the browser. The data collected from the webcam is passed to a Python file that detects Emotion Detection. The project uses Fer2013 data.  

Use app1.py to run instead of main.py
app1.py runs the flask server

At the backend, 
1) the video file gets converted to frames using video2frames.py - the output can be stored in output_frames;
2) write2csv.py gets these frames and converts then to csv - naming each frame with a jpg name and numer;
3) another file will fixpos2Densemap(under const) adds heatmap on the frames;
4) frame_to_video.py converts the video with heatmap back to a video

Feature extractions:
1) The webcam gets converted into a video blob in app1.py and gets uploaded to a folder "upload_files". This can also be a S3 bucket;
2) The webcam video from the upload_files folder is pulled by VideoProducer.py;
3) VideoProducer sends this data to consumer_Expression.py and consumer_eyeGaze.py;
4) These in turn send the data to face_expressions.py and eye_gaze_analysis.py respectively;
5) The output from face_expressions will be a csv file;
6) The output from eye_gaze_analysis will be a txt file, which will be sent to fixpos2Densemap above. 

Note: Here I have hard coded the VideoProducer to take video.mp4 and video1.mp4 for expressions and eye_gaze_analysis

watcher.py folder is an Event Handler. It is currently set to the "output" folder. Any change in that folder will trigger a response from this file. One can set this to S3 bucket or refer to this :
https://github.com/gwenshap/lambda_s3_kafka/blob/master/lambda_s3_kafka.py

Use Python 3.6.5 
