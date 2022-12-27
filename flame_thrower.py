#!/usr/bin/env python
# coding: utf-8

# In[11]:
'''The code converts a video file to a series of frames and then applies a heatmap to each frame. The heatmap is generated 
based on data from a CSV file. Finally, the frames with the heatmap are converted back to a video file, which is uploaded 
to an S3 bucket. The code first imports several modules, including video2frames, Heatmap_on_Frames, and frame_to_video, 
which are all custom modules. It also sets the locations of the input video file, the output frames, the heatmapped frames, 
and the output video file. The generate_video function is defined and takes a histo_datafile as an argument. 
Inside the function, the heatmap_generator function is called with the output_loc, heatmap_frames_dir, and histo_datafile 
as arguments. The frame2video function is then called with the heatmap_frames_dir and output_video_name as arguments. 
The output_video_name is then uploaded to an S3 bucket with the upload_file_to_bucket function.
Finally, if the script is run as the main script, the generate_video function is called with histo_datafile as the argument.'''

from video2frames import video2frames
import Heatmap_on_Frames as hf
import frame_to_video as fv
import utils.s3utils as s3

input_loc = "./temp/downloads/demo.mp4"
output_loc = "./temp/frames"
heatmap_frames_dir = "./temp/heatmapped_frames"
output_video_name = "./temp/uploads/abc.avi"
object_key = "processed/abc.avi"
BUCKET = "focusai-private-sb"


def generate_video(histo_datafile):
    # Since we are using the same video for embedding the heatmap on, we don't need to do the 
    # video2frame conversion every time. This will save some processing time.
    video2frames(input_loc, output_loc)
    hf.heatmap_generator(output_loc, heatmap_frames_dir, histo_datafile)
    fv.frame2video(heatmap_frames_dir, output_video_name)
    filename = os.path.basename(histo_datafile)
    print("Uploading eyegaze csv to S3: ", filename)
    s3.upload_file_to_bucket(output_video_name, filename, BUCKET)
    print("Video with heatmap uploaded to S3", output_video_name)
    s3.upload_file_to_bucket(output_video_name, object_key, BUCKET)

if __name__ == "__main__":
    generate_video(histo_datafile)

