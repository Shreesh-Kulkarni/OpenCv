import cv2 as c
v=c.VideoCapture(0)
while True:
    success,img=v.read()
    c.imshow("Webcam",img)
    if c.waitKey(1) and 0xFF==ord('q'):
        break
