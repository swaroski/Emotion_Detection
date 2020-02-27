#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os



def frame2video():
    image_folder = ".\\destination"
    video_name = 'video_new.avi'
    #outpath =  "C:\\Users\\bhise\\vision\\output_frames" 

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 25, (width,height))
    
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
    
    


# In[2]:





# In[ ]:




