from pathlib import Path


train_def_path = Path("Dataset/casting_data/casting_data/train/def_front/")
train_ok_path = Path("Dataset/casting_data/casting_data/train/ok_front/")

ok_transformed_path = Path("Dataset/transformed/ok/")
def_transformed_path = Path("Dataset/transformed/def/")

ok_model_path = Path("Dataset/transformed/oks.npy")
def_model_path = Path("Dataset/transformed/defs.npy")

test_ok_path = Path("Dataset/casting_data/casting_data/test/ok_front")
test_def_path = Path("Dataset/casting_data/casting_data/test/def_front")