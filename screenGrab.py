import numpy as np
import cv2 as cv
import pyautogui


while(True):

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Capture Window', screenshot) 


    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')