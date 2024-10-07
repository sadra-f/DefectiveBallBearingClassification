from Classification.Classifier import HOGBasedClassifier as HBC
from statics.Paths import def_model_path, ok_model_path, test_def_path, test_ok_path
from Helpers.IO import read_array, read_imgs_in_path
from itertools import chain

def main():
    classifier = HBC()
    ok_model = read_array(ok_model_path)
    def_model = read_array(def_model_path)
    classifier.change_models(ok_model, def_model)
    tests = read_imgs_in_path(test_ok_path)
    tests2 = read_imgs_in_path(test_def_path)
    res = classifier.predict(tests2)
    print(res)

if __name__ == '__main__':
    main()