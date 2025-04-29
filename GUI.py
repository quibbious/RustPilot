import cv2
import wincam
import keyboard
import numpy as np
import random
from threading import Thread
import time

ALTITUDE = 0
SPEED = 0
PITCH = 0
YAW = 0 # heading
def getValues():
    while True:
        global ALTITUDE, SPEED, PITCH, YAW
        time.sleep(2)
        # from main import ALTITUDE, SPEED, PITCH, YAW, AP_RUNNING
        ALTITUDE = random.randint(250,280)
        SPEED = random.randint(50,70)
        PITCH = random.randint(-5,5)
        YAW = random.randint(350,360)
        AP_RUNNING = True
        print(ALTITUDE,SPEED,PITCH,YAW)
        

getValues_thread = Thread(target=getValues) 

# from main import RUNNING_AP, ALTITUDE, SPEED, PITCH, ROLL, YAW
# start menu

with wincam.DXCamera(0,0, 1280, 720, fps=165) as camera:
    
    getValues_thread.start()
    while True:
        
        frame, timestamp = camera.get_bgr_frame()
        img = np.array(frame)
        
 

        cv2.putText(img,f"AUTOPILOT = {str(RUNNING_AP).upper()}", (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img,f"ALT = {ALTITUDE}", (450, 50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(img,f"SPD = {SPEED}", (650, 50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(img,f"PITCH = {str(PITCH).upper()}", (50, 100),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(img,f"HEADING = {str(YAW).upper()}", (50, 150),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        cv2.imshow("AutoPilot Data Panel", img)
        
        if cv2.waitKey(1) & 0xFF == 27: # if q -> quit
            break