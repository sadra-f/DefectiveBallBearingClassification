from FeatureExtraction.HOG import hog_extraction
from Helpers.IO import files_in_path
from statics.Config import DATASET_FILE_PATTERN
from skimage import io
import numpy as np



def vectorize_dataset(dataset_path, limit:int):
    file_path_list = files_in_path(dataset_path, DATASET_FILE_PATTERN)
    res = []
    for path in file_path_list[:limit]:
        res.append(vectorize(path))

    return res


def vectorize(data_path):
    image = io.imread(data_path)
    res = hog_extraction(image)
    return res