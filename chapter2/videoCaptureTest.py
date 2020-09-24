import numpy as np
import cv2

#https://stackoverflow.com/questions/35242735/can-not-read-or-play-a-video-in-opencvpython-using-videocapture

# Capture video from file
cap = cv2.VideoCapture('C:\Users\Desktop02\Documents\OpenCV_pythonFiles\chapter2\boxed-delete.avi')

while True:

    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()