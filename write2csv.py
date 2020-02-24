#!/usr/bin/env python
# coding: utf-8

# In[29]:


import cv2
import csv
import os

#setting path to the frames converted from the video
path = ".\\output_frames"

def write2csv():
    # get all the video file names
    video_file_names = []
    
    for x in os.listdir(path):
        video_file_names.append(x)
        
    data = (zip(video_file_names))    
    #iterate the list above and write to csv
    # The csv would be saved in "video csv data" folder
    with open(".\\video_csv_data\\{}_pixel.csv".format(x), 'a', newline = '') as f:  
        writer = csv.DictWriter(f, fieldnames = ['Filename'])
        writer.writeheader()
        writer = csv.writer(f, delimiter=',')
        for x in data:
            writer.writerow(x)

    f.close()
        
if __name__=="__main__":
    write2csv()
    
    


# In[ ]:





# In[ ]:




