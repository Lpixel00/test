#
import cv2
import numpy as np
import matplotlib.pyplot as plt

# mat image
#img=np.zeros((100,100),np.uint8)

#cv2.rectangle(img,(0,50),(100,100),(255),-1)
#if use -1,
#if not use -1
#cv2.circle(img,(50,50),25,127,-1)

#cv2.imshow("img",img)

#plt.hist(img.ravel(),256,[0,256])
#plt.show()

# gray image
#img=cv2.imread('road/1.jpg',0)

#plt.hist(img.ravel(),256,[0,256])
#plt.show()

#bgr image
img=cv2.imread('road/1.jpg')
b,g,r=cv2.split(img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()