from pathlib import Path
import numpy as np
from skimage import io

def files_in_path(path:Path, pattern:str):
    if not path.is_dir:
        raise ValueError("Path must be a directory")
    res = []
    for p in path.glob(pattern):
        res.append(p)
    return res


def write_array(data, path, name=None):
    if name is None:
        np.save(str(path) + "\\" + path.name[:-5] + ".npy", data)
        return
    
    np.save(str(path) + "\\" + name + ".npy", data)

def read_array(path):
    return np.load(path)


def read_img_file(path):
    return io.imread(path)


def read_imgs_in_path(dir, limit=None):
    file_paths = files_in_path(dir, "*.jpeg")
    if limit is not None:
        file_paths = file_paths[:limit]
    res = []
    for path in file_paths:
        res.append(read_img_file(path))
    return res
