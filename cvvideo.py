
import numpy as np
import cv2

from PIL import Image
from numpy import asarray



cap = cv2.VideoCapture(0)

def videomerge():
    if a == 1:
        image = cv2.imread("nature.jpeg")
    elif a == 2:
        image = cv2.imread("ocean.jpg")
    elif a == 3:
        image = cv2.imread("nice.jpg")
    elif a == 4:
        image = cv2.imread("pic5.jpg")
    elif a == 5:
        image = cv2.imread("dinesh.jpeg")
    elif a == 6:
        image = cv2.imread("brothers.JPG")
    else:
        print('no image found')


    while True:
        ret, frame = cap.read()
        image = cv2.resize(image, (frame.shape[1], frame.shape[0]))
        blended = cv2.addWeighted(image, 0.45, frame, 1, gamma=0.4)

        cv2.imshow('frame', frame[20:])
        cv2.imshow('blended frame', blended)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


a = int(input('select a number between 1 to 6'))
if a == 1:
    videomerge()
elif a==2:
    videomerge()
elif a==3:
    videomerge()
elif a==4:
    videomerge()
elif a==5:
    videomerge()
elif a==6:
    videomerge()
else:
    print('your number not in range')

cap.release()


cv2.destroyAllWindows()