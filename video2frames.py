#!/usr/bin/env python
# coding: utf-8

# In[69]:


import cv2
import time
import os
import csv

input_loc = ".\\input_video\\video1.mp4"
output_loc = ".\\output_frames"

def video2frames():
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    fps = cap.get(cv2.CAP_PROP_FPS)

    timestamps = [cap.get(cv2.CAP_PROP_POS_MSEC)]
    calc_timestamps = [0.0]
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    
    
    #print ("Number of frames: ", video_length)
    count = 0
    
    print ("Converting video..\n")  
           
    # Start converting the video
    while cap.isOpened():
        
        # Extract the frame
        ret, frame = cap.read()
        
                              
        # Write the results back to output location.
        if ret:
            cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
            count = count + 1
            timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))
            calc_timestamps.append(calc_timestamps[-1] + 90/fps)
            
        else:
            break
                                   
    cap.release()
    time_end = time.time()             
    
                                   
            # Print stats
    print("")        
    print ("Done extracting frames.\n%d frames extracted" % count)
    print ("It took %d seconds forconversion." % (time_end-time_start))
            

if __name__=="__main__":
    video2frames()
    
    
    
    
   
    


# In[ ]:




