#!/usr/bin/env python
# coding: utf-8

# In[11]:


from video2frames import video2frames
from write2csv import write2csv
import cv2
import csv
import os
import time
import Heatmap_on_Frames as hf
import frame_to_video

input_loc = ".\\input_video\\video1.mp4"
output_loc = ".\\output_frames"
path = ".\\output_frames"

video2frames()    

time.sleep(10)
hf.heatmap_generator()
time.sleep(25)

frame2video()
#write2csv()
        


# In[ ]:




