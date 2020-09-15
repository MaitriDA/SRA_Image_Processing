import numpy as np
import matplotlib.pyplot as plt
vertical_f=[[-1,-2,-1],[0,0,0],[1,2,1]]

horizontal_f=[[-1,0,1],[-2,0,2],[-1,0,1]]

#img = plt.imread('Cube.jpg')
img = plt.imread('Dog.png')
n,m,d = img.shape
edges_img = img.copy()

for row in range(3, n-2):
    for col in range(3, m-2):
        
        #creating a 3x3 box
        local_pixels = img[row-1:row+2, col-1:col+2, 0]
        
        vertical_transformed_pixels = vertical_f*local_pixels
        vertical_score = vertical_transformed_pixels.sum()/4
        
        horizontal_transformed_pixels = horizontal_f*local_pixels
        horizontal_score = horizontal_transformed_pixels.sum()/4
        
        edge_score = (vertical_score**2 + horizontal_score**2)**.5
        edges_img[row, col] = [edge_score]*3

edges_img = edges_img/edges_img.max()
plt.imshow(edges_img)