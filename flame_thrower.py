#!/usr/bin/env python
# coding: utf-8

# In[11]:

''' This file is part of a trio of three files - the other two being write2csv.py and video2frames.py. 
The later converts video to frames and the former creates a csv files with frame names. These would be useful for 
applying heatmap from eye gaze data'''

from video2frames import video2frames
from write2csv import write2csv
import cv2
import csv
import os
import time

input_loc = ".\\input_video\\vtest.avi"
output_loc = ".\\output_frames"
path = ".\\output_frames"

video2frames()    

time.sleep(10)
write2csv()
        


# In[ ]:




