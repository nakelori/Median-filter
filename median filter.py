import cv2
import numpy as np

img = cv2.imread('view.png')
i = 0   
j = 0
img1 = img.copy()


for i in range(3,img.shape[0]-3,1):
    for j in range(3,img.shape[1]-3,1):
        # Blue Channel (Channel 0)
        medianB = np.array([
        [img[i-3][j-3][0], img[i-3][j-2][0], img[i-3][j-1][0], img[i-3][j][0], img[i-3][j+1][0], img[i-3][j+2][0], img[i-3][j+3][0]],
        [img[i-2][j-3][0], img[i-2][j-2][0], img[i-2][j-1][0], img[i-2][j][0], img[i-2][j+1][0], img[i-2][j+2][0], img[i-2][j+3][0]],
        [img[i-1][j-3][0], img[i-1][j-2][0], img[i-1][j-1][0], img[i-1][j][0], img[i-1][j+1][0], img[i-1][j+2][0], img[i-1][j+3][0]],
        [img[i][j-3][0],   img[i][j-2][0],   img[i][j-1][0],   img[i][j][0],   img[i][j+1][0],   img[i][j+2][0],   img[i][j+3][0]],
        [img[i+1][j-3][0], img[i+1][j-2][0], img[i+1][j-1][0], img[i+1][j][0], img[i+1][j+1][0], img[i+1][j+2][0], img[i+1][j+3][0]],
        [img[i+2][j-3][0], img[i+2][j-2][0], img[i+2][j-1][0], img[i+2][j][0], img[i+2][j+1][0], img[i+2][j+2][0], img[i+2][j+3][0]],
        [img[i+3][j-3][0], img[i+3][j-2][0], img[i+3][j-1][0], img[i+3][j][0], img[i+3][j+1][0], img[i+3][j+2][0], img[i+3][j+3][0]]
        ])

# Green Channel (Channel 1)
        medianG = np.array([
        [img[i-3][j-3][1], img[i-3][j-2][1], img[i-3][j-1][1], img[i-3][j][1], img[i-3][j+1][1], img[i-3][j+2][1], img[i-3][j+3][1]],
        [img[i-2][j-3][1], img[i-2][j-2][1], img[i-2][j-1][1], img[i-2][j][1], img[i-2][j+1][1], img[i-2][j+2][1], img[i-2][j+3][1]],
        [img[i-1][j-3][1], img[i-1][j-2][1], img[i-1][j-1][1], img[i-1][j][1], img[i-1][j+1][1], img[i-1][j+2][1], img[i-1][j+3][1]],
        [img[i][j-3][1],   img[i][j-2][1],   img[i][j-1][1],   img[i][j][1],   img[i][j+1][1],   img[i][j+2][1],   img[i][j+3][1]],
        [img[i+1][j-3][1], img[i+1][j-2][1], img[i+1][j-1][1], img[i+1][j][1], img[i+1][j+1][1], img[i+1][j+2][1], img[i+1][j+3][1]],
        [img[i+2][j-3][1], img[i+2][j-2][1], img[i+2][j-1][1], img[i+2][j][1], img[i+2][j+1][1], img[i+2][j+2][1], img[i+2][j+3][1]],
        [img[i+3][j-3][1], img[i+3][j-2][1], img[i+3][j-1][1], img[i+3][j][1], img[i+3][j+1][1], img[i+3][j+2][1], img[i+3][j+3][1]]
        ])      

# Red Channel (Channel 2)
        medianR = np.array([
        [img[i-3][j-3][2], img[i-3][j-2][2], img[i-3][j-1][2], img[i-3][j][2], img[i-3][j+1][2], img[i-3][j+2][2], img[i-3][j+3][2]],
        [img[i-2][j-3][2], img[i-2][j-2][2], img[i-2][j-1][2], img[i-2][j][2], img[i-2][j+1][2], img[i-2][j+2][2], img[i-2][j+3][2]],
        [img[i-1][j-3][2], img[i-1][j-2][2], img[i-1][j-1][2], img[i-1][j][2], img[i-1][j+1][2], img[i-1][j+2][2], img[i-1][j+3][2]],
        [img[i][j-3][2],   img[i][j-2][2],   img[i][j-1][2],   img[i][j][2],   img[i][j+1][2],   img[i][j+2][2],   img[i][j+3][2]],
        [img[i+1][j-3][2], img[i+1][j-2][2], img[i+1][j-1][2], img[i+1][j][2], img[i+1][j+1][2], img[i+1][j+2][2], img[i+1][j+3][2]],
        [img[i+2][j-3][2], img[i+2][j-2][2], img[i+2][j-1][2], img[i+2][j][2], img[i+2][j+1][2], img[i+2][j+2][2], img[i+2][j+3][2]],
        [img[i+3][j-3][2], img[i+3][j-2][2], img[i+3][j-1][2], img[i+3][j][2], img[i+3][j+1][2], img[i+3][j+2][2], img[i+3][j+3][2]]
        ])

        img1[i][j][0] = np.median(medianB)  
        img1[i][j][1] = np.median(medianG)
        img1[i][j][2] = np.median(medianR)
        
cv2.imshow('show',img1)
cv2.waitKey(0)