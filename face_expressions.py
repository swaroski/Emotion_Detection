#!/usr/bin/env python
# coding: utf-8

# In[1]:

'''This file takes facial expressions from a webcam or a video file and displays seven expressions on the video display frame.
Here we are passing a video file and storing the expressions and frames as per FPS into a text file. Remember to change 
the file path and change the videocapture input to 0, 1, -1 accordingly'''


from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np
#from keras.models import load_model
import csv
import time
import os
#prevent showing information/warning logs including libpng warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#file = "C:\\Users\\bhise\\vision\\video1.mp4"
frame_images = []

def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x

detect_model_path = './data/haarcascade_frontalface_default.xml'


face_detection = cv2.CascadeClassifier(detect_model_path)
emotion_classifier = load_model('./data/recog.h5')
EMOTIONS = ["angry", "disgust", "scared", "happy", "sad", "surprised", "neutral"]

def gen(file):
#    cv2.namedWindow('cam')
    #print("After naming window", file)
    cap = cv2.VideoCapture(file)
    #print("captain plaenet is here")
    predictions = list()
    count =0
    #print("Framecount: ", cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #print("PosFrames: ",  cap.get(cv2.CAP_PROP_POS_FRAMES))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret is False:
            break
        #print("Return Value:", ret)
        #frame = imutils.resize(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       # cv2.imshow('frame', gray)
       # #print("what is gray", gray)
        faces = face_detection.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, 
                                                minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)
        
        if frame is None:
            continue 
        fps = cap.get(cv2.CAP_PROP_FPS)
        canvas = np.zeros((250, 300, 3), dtype = "uint8")
        frameClone = frame.copy()
        timestamps = cap.get(cv2.CAP_PROP_POS_MSEC)
        #timestamps = [cap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))]
        calc_timestamps = [0.0]
        if len(faces) > 0:
            faces = sorted(faces, reverse = True, key = lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = faces

            img = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(img, (48, 48))
            roi = roi.astype("float")/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis = 0)

            pred = emotion_classifier.predict(roi)[0]
            emotion_probability = np.max(pred)
            label = EMOTIONS[pred.argmax()]
            #print(label)

            #font = cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8  # Creates a font
            x = 100  # position of text
            y = 200  # position of text
            #print("Before cv2.puttext")
            cv2.putText(frameClone, label, (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255), lineType=cv2.LINE_AA)
            #print("after cv2") 
            calc_timestamps.append(calc_timestamps[-1] + 1000/fps)
            curr_time = int(round(time.time() * 1000))
            frame_images.append(curr_time)
            curr_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            count += 1
            predictions.append(label)
            #print("bas bhi kar")
            data = (zip(predictions, frame_images))
            #print("after data zip") 

        with open("./static/db/histo_perso.txt", "a", newline = '') as d:
            #print("inside open")
            #d.write("density  Time" +'\n')
            #writer = csv.DictWriter(d, fieldnames=["X", "Time"])
            #writer.writeheader()
            writer = csv.writer(d, delimiter=',') 
            for row in (data):
                #print(row)
                writer.writerow(row)
                #writer.writerow(zip(data))
            d.close()
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            #print("done")
        # If the number of captured frames is equal to the total number of frames,
        # we stop
            break
       # cv2.imshow('cam', frameClone)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    gen(file)    


# In[ ]:




