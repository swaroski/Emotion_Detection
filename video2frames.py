#!/usr/bin/env python
# coding: utf-8

# In[69]:


import cv2
import time
import os

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
    # Create output directory if it doesn't exist
    if not os.path.exists(output_loc):
        os.mkdir(output_loc)

    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1

    # Start converting the video
    count = 0
    print("Converting video..\n")  
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        if ret:
            cv2.imwrite(f"{output_loc}/{count+1:05d}.jpg", frame)
            count += 1
        else:
            break

    cap.release()
    print(f"Done extracting frames.\n{count} frames extracted")

if __name__=="__main__":
    video2frames()


if __name__=="__main__":
    video2frames()
    
    
    
    
   
    


# In[ ]:




