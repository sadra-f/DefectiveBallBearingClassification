from FeatureExtraction.HOG import hog_extraction
from Helpers.IO import files_in_path
from statics.Config import DATASET_FILE_PATTERN
from skimage import io
import numpy as np


def vectorize_test_dataset(img_list):
    for img in img_list:
        img.img = vectorize_img(img.img)

def vectorize_dataset(img_list):
    res = []
    for img in img_list:
        res.append(vectorize_img(img))

    return res


def vectorize_img(img):
    return hog_extraction(img)