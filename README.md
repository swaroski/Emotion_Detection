# Multi-Modal Facial Detection
This project is built as a final project for AI Deep dive. It consists of the ability for the client serving the video to record users' facial features while they are watching a video, movie trailer, advertisement, product launch. The webcam starts simultaneously when the video on the browser loads - all happening inside the browser using WebRTC. The data collected from the webcam is passed to a Python file that detects emotions, tracks eye gaze and also predicts age and gender of the person watching the video. The project uses Fer2013 data. 

The idea of this project is to have a browser extension, Mobile App and a Web App that connects to Adtech platforms. Once connected, a user would be shown ads based on their cookies and they would be incentivized to watch those ads, instead of pressing "skips ad" as it often happens with video advertisements. While we ask for their consent to track the mentioned facial features. This data would allow advertising companies \ Publishers to understand what part of the ad the user is focussed on and also their engagement level. 

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
