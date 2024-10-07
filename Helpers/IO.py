from pathlib import Path
import numpy as np
from skimage import io

def files_in_path(path:Path, pattern:str):
    if not path.isdir():
        raise ValueError("Path must be a directory")
    res = []
    for p in path.glob(pattern):
        res.append(p)
    return res


def write_array(data, path):
    np.save(str(path) + "\\" + path.name[:-5] + ".npy", data)

def read_array(path):
    return np.load(path)


def read_img_file(path):
    return io.imread(path)


