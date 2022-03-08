import cv2
from cv2 import ORB
from cv2 import waitKey
cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    cv2.imshow("video",frame)
    if orb("q")==cv2.waitKey(1):
        break
