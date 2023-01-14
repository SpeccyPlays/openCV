#video example
import numpy as np
import cv2 as cv
<<<<<<< HEAD
cap = cv.VideoCapture(r'C:\Users\ben\Documents\GitHub\openCV\examples\chuckie.mp4')#note full path needed and r converts string to raw otherwise errors
=======
cap = cv.VideoCapture('chuckie.mp4')
>>>>>>> e0a5857ae7f81014fb43d66e65e36276103f6ccb
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()