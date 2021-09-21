from typing import Text
import cv2 as c
import numpy as np
def blank():
    img=np.zeros((480,480),np.uint8)
    c.imshow("Blank",img)
    c.waitKey(1000)
def bg():
    img=np.zeros((512,512,3),np.uint8)
    img[20:30,45:401]=(255,0,0)
    c.imshow("Bg",img)
    c.waitKey(1000)
def line(img):
    c.line(img,(0,0),(512,490),(0,255,0),4)    
    c.imshow("Lines go brr",img)
    c.waitKey(0)
def rect(img):
    c.rectangle(img,(69,420),(42,69),(255,0,0),c.FILLED)    
    c.putText(img,"CR7 is the undisputed GOAT",(55,42),c.FONT_ITALIC,1,(255,0,0),2)
    c.imshow("CR7",img)
    c.waitKey(0)
img=np.zeros((512,512,3),np.uint8)
rect(img)    


