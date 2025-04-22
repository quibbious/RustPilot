import pyautogui
import pyperclip
import keyboard as kb
import time 
import sys


SetupWindowPos = (1851, 51)
# sea level = 0m 
# height ceiling relative to sea level is 650m


def getXYZ():
    position_history = open("pos_history.log", "a")
    position_history.write("\n")
    pyautogui.moveTo(SetupWindowPos)
    pyautogui.click()
        
    pyautogui.press('f1')
    
    kb.write('console.clear')
    pyautogui.press('enter')
    
    kb.write('client.printpos')
    pyautogui.press('enter')
    
    kb.write('console.copy')
    pyautogui.press('enter')
    
    kb.write('console.clear')
    pyautogui.press('enter')
    pyautogui.press('f1')
    
    position = pyperclip.paste().strip()
    position = position[position.index('(') + 1:position.index(')')]  # Extracting coordinates part
    result = [float(num) for num in position.split(',')]
    position_history.write(f"{result}")
    return result

def getClimbRate(y1, y2, timeBetweenSnapshots: int=1):
    verticalDistance = y2 - y1
    climb_rate = verticalDistance / timeBetweenSnapshots
    
    return int(climb_rate)

def getRotation():
    pyautogui.moveTo(SetupWindowPos)
    pyautogui.click()
        
    pyautogui.press('f1')
    
    kb.write('console.clear')
    pyautogui.press('enter')
    
    kb.write('client.printrot')
    pyautogui.press('enter')
    
    kb.write('console.copy')
    pyautogui.press('enter')
    
    kb.write('console.clear')
    pyautogui.press('enter')
    pyautogui.press('f1')
    
    rotation = pyperclip.paste().strip()
    rotation = rotation[rotation.index('(') + 1:rotation.index(')')]  # Extracting coordinates part
    result = [float(num) for num in rotation.split(',')]
    
    return result

def plotLocation(points,interval):
    """plots current location of the minicopter (`point`) every `interval` seconds\n
    args:
        `points (int): number of points to plot`\n
        `interval (int): time between each point in seconds`
    """
    LocHistory = [[], # POINT NUMBER
                  []] # XYZ
    
    for point in range(0,points+1):
        kb.block_key('w')
        kb.block_key('a')
        kb.block_key('s')
        kb.block_key('d') # block movement keys to prevent movement during plotting or typing during CMD window
        
        location = getXYZ()
        LocHistory[0].append(point)
        LocHistory[1].append(location)
        kb.unblock_key('w')
        kb.unblock_key('a')
        kb.unblock_key('s')
        kb.unblock_key('d') # unblock movement keys because CMD window is gone
        
        
        time.sleep(interval)
        if kb.is_pressed('q'): # killswitch 
            print("killswitch triggered")
            break
        return LocHistory

# the map works as follows: 
# origin of the map is X: 0 Y: 0 Z: 0 (middle of the map, sea level)

# -X coordinates are East
# +X coords are West

# -Y coordinates are below sea level (0m)
# +Y coordinates are above sea level (0m)


# -Z coordinates are South
# +Z coordinates are North



# client.printrot holds the pitch, roll, and yaw 
# level and even flight holds values close to zero/360 degrees