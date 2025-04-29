import pyautogui
import time
import os 
from Instruments import getXYZ, getClimbRate, getRotation, plotLocation
import keyboard as kb
import sys 
global RUNNING_AP, ALTITUDE, SPEED, PITCH, YAW


if os.path.exists("pos_history.log"): 
    os.remove("pos_history.log") 
else: 
    pass

with open("pos_history.log", "a") as position_history:
    
    position_history.write("--- AUTOPILOT POSITION HISTORY ---")
    
    
    
SetupWindowPos = (1851, 51)
MSL: int = 0
MAX_HEIGHT: int = 605 # relative to KoalaKopters Practice server, max height for most servers is ~300


# this is the REAL minicopter scripts
class MiniControls(): 
    def __init__():
        MSL: int = 0
        MAX_HEIGHT: int = 605
        SetupWindowPos = (1851, 51)

    def startup():
        pyautogui.press('w')
        time.sleep(5.5)
        print("startup complete")
        return 1
    def up(seconds=1):    
        with pyautogui.hold("w"):
            print(f"going up for {seconds} seconds")
            time.sleep(seconds)
            print("up complete")
            return 1

    
    def down(seconds=1):
        with pyautogui.hold("s"):
            print(f"going down for {seconds} seconds")
            time.sleep(seconds)
            print("down complete")
            return 1
    
    def Hover(seconds=10):
        #attempts to hover in place
        start_time = time.time()
        while time.time() - start_time < seconds:
            print("hovering")
            pyautogui.press("w")
            pyautogui.press("w")
            pyautogui.press("w")
            pyautogui.press("w")
            pyautogui.press("w")
            time.sleep(1.25)
            
    
    def Exit():
        pyautogui.press('space')
        print("exiting minicopter")
        return 1
    
    def E_STOP():
        with pyautogui.hold('s'):
            print("EMERGENCY STOP")
            time.sleep(7)
            pyautogui.press('x')
            time.sleep(0.5)
            pyautogui.press('x')
            print("emergency stop complete")

time.sleep(3)
RUNNING_AP = True
MiniControls.startup()
MiniControls.up(10)
time.sleep(5)
plotLocation(10,3)


if kb.is_pressed('q'):
    print("killswitch triggered")
    sys.exit()

position_history.close()