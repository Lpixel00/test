#hsv

import cv2
import numpy as np

def nothing(x):
   pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",0,255,nothing)
cv2.createTrackbar("US","Tracking",0,255,nothing)
cv2.createTrackbar("UV","Tracking",0,255,nothing)


img=cv2.imread('qiqiu/1.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

l_h=cv2.getTrackbarPos("LH","Tracking")
print(l_h)
l_s=cv2.getTrackbarPos("LS","Tracking")
l_v=cv2.getTrackbarPos("LV","Tracking")

l_b=np.array([l_h,l_s,l_v])
u_h=cv2.getTrackbarPos("UH","Tracking")
u_s=cv2.getTrackbarPos("US","Tracking")
u_v=cv2.getTrackbarPos("UV","Tracking")
u_b=np.array([u_h,u_s,u_v])

mask=cv2.inRange(hsv,l_b,u_b)

res=cv2.bitwise_and(img,img,mask=mask)

cv2.imwrite('qiqiu/a.jpg',hsv)
cv2.imwrite('qiqiu/b.jpg',mask)
cv2.imwrite('qiqiu/c.jpg',res)
cv2.imshow('hsv',hsv)
cv2.imshow('mask',mask)
cv2.imshow('res',res)



cv2.waitKey(0)#when press any key,it will close the imshow windows
  
   