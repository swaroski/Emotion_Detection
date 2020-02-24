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
1) The webcam gets converted into a video blob in app1.py and gets uploaded to a folder 
