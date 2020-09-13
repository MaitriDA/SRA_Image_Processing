from PIL import Image,ImageDraw
import numpy as np
import matplotlib.pyplot as plt

#image=Image.open('input_box_blur.jpeg')
image=Image.open('lena.png')
input_value=image.load()

Box=[[1/25,1/25,1/25,1/25,1/25],
            [1/25,1/25,1/25,1/25,1/25],
            [1/25,1/25,1/25,1/25,1/25],
            [1/25,1/25,1/25,1/25,1/25],
            [1/25,1/25,1/25,1/25,1/25]] 

Gaussian=[[1/256,4/256,6/256,4/256,1/256],
               [4/256,6/256,24/256,6/256,4/256],
               [6/256,24/256,36/256,24/256,6/256],
               [4/256,6/256,24/256,6/256,4/256],
               [1/256,4/256,6/256,4/256,1/256]]  

Sharpen=[[-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1],
         [-1,-1,25,-1,-1],
         [-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1],]


kernel=Box
#kernel=Gaussian
#kernel=Sharpen
os=len(kernel)//2
New_image=Image.new("RGB",image.size)
draw=ImageDraw.Draw(New_image)

for x in range(os,image.width-os):
    for y in range(os,image.height-os):
        acc=[0,0,0]
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn=x+a-os
                yn=y+b-os
                value=input_value[xn,yn]
                acc[0]+=value[0]*kernel[a][b]
                acc[1]+=value[1]*kernel[a][b]
                acc[2]+=value[2]*kernel[a][b]
        draw.point((x,y),(int(acc[0]),int(acc[1]),int(acc[2])))

plt.imshow(New_image)
