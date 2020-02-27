#!/usr/bin/env python
# coding: utf-8

# In[1]:


from heatmappy import Heatmapper
from PIL import Image
from video import VideoHeatmapper



# In[2]:


import os
UPLOAD_FOLDER = ".\\heatmappy\\assets"
filename = ("video.mp4")
example_vid = os.path.join(UPLOAD_FOLDER, filename)
example_points = [(100, 100, 25), (112, 92, 67), (17, 100, 36),(120, 90, 26), (110, 70, 16), (110, 130, 66)]

#img_heatmapper = Heatmapper()
#video_heatmapper = VideoHeatmapper(img_heatmapper)

heatmapper = Heatmapper(
    point_diameter=50,  # the size of each point to be drawn
    point_strength=0.2,  # the strength, between 0 and 1, of each point to be drawn
    opacity=0.65,  # the opacity of the heatmap layer
    colours='default',  # 'default' or 'reveal'
                        # OR a matplotlib LinearSegmentedColorMap object 
                        # OR the path to a horizontal scale image
    grey_heatmapper='PIL'  # The object responsible for drawing the points
                           # Pillow used by default, 'PySide' option available if installed
)

video_heatmapper = VideoHeatmapper(
    heatmapper  # the img heatmapper to use (like the heatmapper above, for example)
)

heatmap_video = video_heatmapper.heatmap_on_video_path(
    video_path=example_vid,
    points=example_points
)

heatmap_video.write_videofile('out.mp4', fps=24)





# In[ ]:





# In[ ]:




