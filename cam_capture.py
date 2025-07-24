import os
import time
import cv2

def capture_image(path="/tmp/cam.jpg"):
    os.system(f"libcamera-still -n -t 1000 -o {path}")
    time.sleep(1)
    img = cv2.imread(path)
    return img
