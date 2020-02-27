#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sys import platform as sys_pf
if sys_pf == 'darwin':
    # necessary for matplotlib on OSX, see https://stackoverflow.com/questions/43066073/matplotlib-tkinter-opencv-crashing-in-python-3
    import matplotlib
    matplotlib.use("MacOSX")
from matplotlib import pyplot as plt
import cv2
import autopy
import seaborn as sns
import time
import imutils
import csv
import pandas as pd
import time
#from datetime import datetime
frame_images=[]
file = "C:\\Users\\bhise\\vision\\video.mp4"

ESCAPE_KEY = 'q'
# Standards: use constants like this to follow DRY
# and reduce the occurrence of "magic numbers" in your code that lack context
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
#t0 = time.time()
                   
        
def transform_video_coordinates_to_screen(eye_x_pos, eye_y_pos):
    if not video_resolution:
        return (eye_x_pos, eye_y_pos)

    return (
        eye_x_pos / video_resolution[0] * screen_resolution[0],
        eye_y_pos / video_resolution[1] * screen_resolution[1],
    )
    
def update_mouse_position(hough_circles, eye_x_pos, eye_y_pos, roi_color2):
    try:
        for circle in hough_circles[0, :]:
            # Standards: DRY (don't repeat yourself), define circle_center once and use it twice.
            circle_center = (circle[0], circle[1])
            # draw the outer circle
            cv2.circle(
                img=roi_color2,
                center=circle_center,
                radius=circle[2],
                color=WHITE,
                thickness=2
            )
            # print("drawing circle")
            # draw the center of the circle
            cv2.circle(
                img=roi_color2,
                center=circle_center,
                radius=2,
                color=WHITE,
                thickness=3
            )

            # print(i[0],i[1])

            x_pos = int(eye_x_pos)
            y_pos = int(eye_y_pos)
            autopy.mouse.move(x_pos, y_pos)
    except Exception as e:
        # Standards: exception handling in try: except cases should generally be as specific as possible. What type of
        # exception are you expecting to encounter here? Instead of capturing "Exception" capture that specific class of exception.
        print('Exception:', e)

face_cascade = cv2.CascadeClassifier(
    ".\\data\\haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    ".\\data\\haarcascade_righteye_2splits.xml"
)

def run_tracker(file):
    #number signifies camera
    cv2.namedWindow('cam')
    video_capture = cv2.VideoCapture(file)
    cv2.startWindowThread()
    eye_x_positions = list()
    eye_y_positions = list()
    
    #end = 0
    # Timer
    #global k
    #k = 0
    #max_time = 65
    #start = time.time()
    #t1 = time.time() # current time
    #num_seconds = t1 - t0 # diff
    #if num_seconds > 30:  # e.g. break after 30 seconds
     #   break
    #eye_x_positions = list()
    #eye_y_positions = list()
    count = 0
    #key_pressed = None
    while True:
        success, image = video_capture.read()
        #image = imutils.resize(image)
        #t1 = time.time() # current time
        #num_seconds = t1 - t0 # diff
        #if num_seconds > 30:  # e.g. break after 30 seconds
        #    break
        if image is None:
            continue
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frameClone = image.copy()
        #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        fps = video_capture.get(cv2.CAP_PROP_FPS)
        frame_count = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        timestamps = video_capture.get(cv2.CAP_PROP_POS_MSEC)
        #timestamps = [video_capture.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))]
        calc_timestamps = [0.0]
        #count = 0

        for (eye_x, eye_y, eye_width, eye_height) in eyes:
            # Standards: may be good to explicitly call out the parameters being passed to methods,
            # if you are not explicitly declaring these values as variables with informative names
            cv2.rectangle(
                img=image,
                pt1=(eye_x, eye_y),
                pt2=(eye_x + eye_width, eye_y + eye_height),
                color=GREEN,
                thickness=2
            )
            roi_gray2 = gray[eye_y: eye_y + eye_height, eye_x: eye_x + eye_width]
            roi_color2 = image[eye_y: eye_y + eye_height, eye_x: eye_x + eye_width]
            # Standards: As above, it may be good to describe the parameters being passed
            # but in this case I had a hard time reconciling the positional arguments here with expected parameters
            hough_circles = cv2.HoughCircles(
                roi_gray2,
                cv2.HOUGH_GRADIENT,
                1,
                200,
                param1=200,
                param2=1,
                minRadius=0,
                maxRadius=0
            )
            # Standards: DRY (don't repeat yourself), calculate eye positions once and use them below
            #timestamps.append(video_capture.get(cv2.CAP_PROP_POS_MSEC))
            calc_timestamps.append(calc_timestamps[-1] + 1000/fps)
            eye_x_pos = (eye_x + eye_width) / 2
            eye_y_pos = (eye_y + eye_height) / 2
            #print(eye_x_pos, eye_y_pos)
            eye_x_positions.append(eye_x_pos)
            eye_y_positions.append(eye_y_pos)
            curr_time = int(round(time.time() * 1000))
            #frame_images.append(curr_time)
            
            curr_frame = int(video_capture.get(cv2.CAP_PROP_POS_FRAMES))
            converted_name = format(curr_frame, "05d") + ".jpg"
            #print('{}.jpg'.format(curr_frame,"05d"))
            print(converted_name)
            frame_images.append(converted_name)
            #print(type(curr_frame))
            count += 1
            # Standards: in general in the interests of improving readability, move logical chunks
            # of code out into their own classes, methods, or functions to make it easier to understand overall
            # program flow
            update_mouse_position(hough_circles, eye_x_pos, eye_y_pos, roi_color2)

        #cv2.imshow('img', image)
        cv2.imshow('cam', frameClone)
        # Standards: code like this can be hard to understand, so comments explicitly describing operation are desirable:
        # This reduces cv2.waitKey() response to 8 bit integer, representing ASCII input
        #if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
         #   break        
        if video_capture.get(cv2.CAP_PROP_POS_FRAMES) == video_capture.get(cv2.CAP_PROP_FRAME_COUNT):
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #if key_pressed == ESCAPE_KEY:
         #   break
        #cv2.imshow('asd', image)    
        if cv2.getWindowProperty('cam', 11) == 1:
            break
    # close window
    video_capture.release()
    cv2.destroyAllWindows()

    # plot heatmap
    #plot_data(eye_x_positions, eye_y_positions)
    data = (zip(eye_x_positions, eye_y_positions, frame_images))
    
    print (video_capture.get(cv2.CAP_PROP_POS_MSEC))
    
    print(data)
    
    # Once reaching the end, write the results to the personal file and to the overall file
    #if end-start > max_time - 1:
    print(data)
    with open(".\\static\\db\\histo_eyes.csv", "a", newline = '') as d:
            #d.write("density  Time" +'\n')
            #writer = csv.DictWriter(d, fieldnames=["X", "Y", "name"],delimiter=',')
            #writer.writeheader()
            writer = csv.writer(d, delimiter=',') 
            writer.writerow(["X", "Y", "frame"])
            #writer.writerow(header)
            for row in (data):
                writer.writerow(row)
                #writer.writerow(zip(data))
            d.close()
            
    #with open(".\\static\\db\\histo_eyes.csv", "a", newline='') as d:
                #d.write("eye_coordinates" +'\n')
                 
     #           writer = csv.DictWriter(d, fieldnames=["X", "Y", "Time"])
      #          writer.writeheader()
                
       #         writer = csv.writer(d, delimiter=',') 
                
        #        for row in (data):
         #          writer.writerow(row)
                    
                    #writer.writerow(zip(data))
          #      d.close()
     
    
        
        # If the number of captured frames is equal to the total number of frames,
        # we stop
                  
    #with open("C:\\Users\\bhise\\Modal_detection\\static\db\\histo_eyes.txt", "a") as d:
     #   d.write("eye_coordinates" +'\n')
      #  for val in data:
       #     d.write(str(val)+'\n')
        #d.close()
            
               
            
                
#def plot_data(x, y):
 #   h, x, y, p = plt.hist2d(x, y)               # generates 2d heatmap
  #  plt.clf()
    #plt.imshow(h, interpolation = "gaussian")   # draws heatmap
   # plt.axis("off")
    #plt.show()
    #sns.set()
   
    


if __name__ == "__main__":
    run_tracker(file)


# 
# q## 


# ## 
