#!/usr/bin/env python
# coding: utf-8

# In[1]:

'''This file converts frames to video only when the eye gaze heatmap is applied'''
import cv2
import os

image_folder = "C:\\Users\\bhise\\vision\\output_frames"
video_name = 'video.avi'
#outpath =  "C:\\Users\\bhise\\vision\\output_frames" 

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 25, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


# In[2]:





# In[ ]:



