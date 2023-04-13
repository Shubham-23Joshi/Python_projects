import os
import time
#import cv2 as cv
#import numpy as np
from pycoral.utils import edgetpu
from pycoral.utils import dataset
from pycoral.adapters import common
from pycoral.adapters import classify
from PIL import Image
from imutils.video import VideoStream
import imutils

vs = VideoStream(src=1).start()
print("starting video stream...")
time.sleep(2.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    test = frame.copy()
    cv.imshow("Test Frame", test)
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break
        
cv.destroyAllWindows()
vs.stop()