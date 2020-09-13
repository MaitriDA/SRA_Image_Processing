#NOTE-not getting the code for Bound Concept
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image

img=plt.imread('rotate.png')
print(img.shape)
h,w,num_channels=img.shape
degree=int(input("Enter the angle "))
radian=(degree*math.pi)/180
max_len=int(math.sqrt(h*h+w*w))
rotated_img=np.zeros((max_len,max_len,num_channels))
print(rotated_img.shape)
mid_r=int(max_len/2)
mid_c=int(max_len/2)
cos=math.cos(radian)
sin=math.sin(radian)

#r,c=Old Cordinates
#x,y=New Cordinates

#[[cos sin]
  #[-sin cos]]
for r in range(max_len):
    for c in range(max_len):
        y=(r-mid_c)*cos+(c-mid_r)*sin
        x=-(r-mid_c)*sin+(c-mid_r)*cos
        y+=mid_c
        x+=mid_r
        y=int(y)
        x=int(x)
        if(x>=0 and y>=0 and x<w and y<h):
            rotated_img[r,c]=img[y,x]
            
plt.imshow(rotated_img)