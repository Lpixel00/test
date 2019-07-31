import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('binary/4.jpg')
image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

contours,_ =cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("no of shape {0}".format(len(contours)))

#这种方法，如果是圆形，曲线也是圆弧形，跟着曲线形状一样。
for cnt in contours:
   epsilon=0.01*cv2.arcLength(cnt,True)
   approx=cv2.approxPolyDP(cnt,epsilon,True)
   img=cv2.drawContours(img,[approx],0,(0,255,0),3)



#如果是圆形，就有一个外切矩形，看上去好像是把形状包装起来。
#for cnt in contours:
#  rect=cv2.minAreaRect(cnt)
#   box=cv2.boxPoints(rect)
#   box=np.int0(box)
#   img=cv2.drawContours(img,[box],0,(0,255,0),3)

plt.figure("Example")
plt.imshow(img)
plt.title("Example")
plt.show()

