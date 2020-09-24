import cv2
import numpy
import os

'''
grayImage = cv2.imread('C:\Users\Desktop02\Pictures\me.PNG', cv2.CV_LOAD_IMAGE_GRAYSCALE)
#cv2.imwrite('C:\Users\Desktop02\Pictures\me_grayscale.jpg', grayImage)
byteArray = bytearray(grayImage)
print byteArray
'''

# Make an array of 120, 000 random bytes.
randomByteArray = bytearray(os.urandom(120000))

flatNumpyArray = numpy.array(randomByteArray)

# Convert the array to make a 400x300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('C:\Users\Desktop02\Documents\OpenCV_pythonFiles\chapter2\RandomGray.png', grayImage)

# Convert the array to make a 400x300 color image.
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('C:\Users\Desktop02\Documents\OpenCV_pythonFiles\chapter2\RandomColor.png', bgrImage)

