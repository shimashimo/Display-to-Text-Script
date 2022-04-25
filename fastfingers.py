import pytesseract
from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui, time
time.sleep(1)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def fastFingers(words):
    pyautogui.FAILSAFE = True
    for word in words:
        pyautogui.typewrite(word)
        pyautogui.press("space")
        time.sleep(4)


while(True):
    x = 800
    y = 250

    width = 1000
    height = 200
    img = ImageGrab.grab(bbox=(x, y, x+width, y+height),include_layered_windows= False,all_screens=True)

    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('Capture Window', img)


    text = pytesseract.image_to_string(img)
    text = text.split()
    fastFingers(text)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

