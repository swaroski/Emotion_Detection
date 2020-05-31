#!/usr/bin/env python
# coding: utf-8

# In[10]:
#This file overlays or superimposes heatmap over individual frames inside a folder. It uses eye-gaze co-ordinates. 

import cv2
import os
import glob
from scipy import ndimage
from skimage import io
import numpy as np
from PIL import Image
from heatmappy import Heatmapper
from collections import OrderedDict
import heatmap_points as points

def heatmap_generator(img_dir, heatmap_dir, histo_datafile):
    # Enter Directory of all images
    #img_dir = "./output_frames"  
    data_path = os.path.join(img_dir,'*g')
    files = glob.glob(data_path)
#    print(files)
#    
    heatmapper = Heatmapper(
    point_diameter=90,  # the size of each point to be drawn
    point_strength=0.8,  # the strength, between 0 and 1, of each point to be drawn
    opacity=0.65,  # the opacity of the heatmap layer
    colours='default',  # 'default' or 'reveal'
                        # OR a matplotlib LinearSegmentedColorMap object 
                        # OR the path to a horizontal scale image
    grey_heatmapper='PIL'  # The object responsible for drawing the points
                           # Pillow used by default, 'PySide' option available if installed
)
    professions_dict = points.getCordinatesDict(histo_datafile)
    for k, v in professions_dict.items():
#        print(k, v)
        if k == "frame":
            continue
        frame = Image.open(img_dir + "/" + k)
        heatmap = heatmapper.heatmap_on_img(v, frame)
        dest_path = heatmap_dir + "/" + k + ".png"
        #dest_path = os.path.join(".\\destination\\", '*g')
#        print(dest_path)
    
        heatmap.save(dest_path)
        
if __name__ == "__main__":
    heatmap_generator(img_dir, histo_datafile)        
        
