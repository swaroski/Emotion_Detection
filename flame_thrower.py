#!/usr/bin/env python
# coding: utf-8

# In[11]:
#converts the video with heatmap back to a video. It first executes the videos2frames.py to convert video to frames.
#Then a heatmap is applied over those frames using heatmap_generator. Lastly, the frames with the heatmap are converted back to a video.  

from video2frames import video2frames
from write2csv import write2csv
import cv2
import csv
import os
import time
import Heatmap_on_Frames as hf
import frame_to_video as fv
import utils.s3utils as s3

input_loc = "./temp/downloads/demo.mp4"
output_loc = "./temp/frames"
heatmap_frames_dir = "./temp/heatmapped_frames"
#histo_datafile = "./static/db/histo_eyes.csv"
#histo_datafile = "./temp/data/b74830fb-12e2-4205-b150-f0d8c1b4ee07_eyes.csv"
output_video_name="./temp/uploads/abc.avi"
object_key="processed/abc.avi"
BUCKET="focusai-private-sb"


#video2frames(input_loc)    

#time.sleep(10)
#hf.heatmap_generator(output_loc, heatmap_frames_dir, histo_datafile)
#time.sleep(10)

#fv.frame2video(heatmap_frames_dir, output_video_name)

#s3.upload_file(f"processed/abc.avi", BUCKET)
#s3.upload_file_to_bucket(output_video_name, f"processed/abc.avi", BUCKET)
####write2csv()

def generate_video(histo_datafile):
    #Since we are using the same video for embedding the heatmap on, we don't need to do the 
    #video2frame conversion everytime. This will save some processing time.
    #video2frames(input_loc)
    #time.sleep(10)
    print("Generate video file ")
    hf.heatmap_generator(output_loc, heatmap_frames_dir, histo_datafile)
    #time.sleep(10)
    fv.frame2video(heatmap_frames_dir, output_video_name)
    filename=os.path.basename(histo_datafile)
    print("Uploading eyegaze csv to S3: ", filename)
    s3.upload_file_to_bucket(output_video_name, filename, BUCKET)

    print("Video with heatmap uploaded to S3", output_video_name)
    s3.upload_file_to_bucket(output_video_name, object_key, BUCKET)


if __name__ == "__main__":
    generate_video(histo_datafile)
