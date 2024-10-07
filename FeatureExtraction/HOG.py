import numpy as np
from skimage import io, color
from skimage.feature import hog

def hog_extraction(image, visualize=False):
    gray_img = color.rgb2gray(image)
    if visualize:
        vector, img =  hog(gray_img, pixels_per_cell=(2, 2), cells_per_block=(2, 2), visualize=True)
        return vector, img
       
    vector = hog(gray_img, pixels_per_cell=(2, 2), cells_per_block=(2, 2), visualize=False)

    return vector