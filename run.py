from Classification.Classifier import HOGBasedClassifier as HBC
from statics.Paths import *
from Helpers.IO import read_array, read_imgs_in_path
from itertools import chain
# from Preprocessing.Vectorizer import vectorize_dataset
# from Clustering.CKMeans import cluster_vectors, mean_of_clusters
# from Helpers.IO import write_array 
def main():
    # def_dataset = read_imgs_in_path(train_def_path)
    # ok_dataset = read_imgs_in_path(train_ok_path)

    # def_dataset = vectorize_dataset(def_dataset)
    # ok_dataset = vectorize_dataset(ok_dataset)

    # def_dataset = cluster_vectors(def_dataset)
    # ok_dataset = cluster_vectors(ok_dataset)

    # def_dataset = mean_of_clusters(def_dataset)
    # ok_dataset = mean_of_clusters(ok_dataset)

    # write_array(def_dataset, def_model_path)
    # write_array(ok_dataset, ok_model_path)

    classifier = HBC()
    ok_model = read_array(ok_model_path)
    def_model = read_array(def_model_path)
    classifier.change_models(ok_model, def_model)
    tests = read_imgs_in_path(test_ok_path)
    tests2 = read_imgs_in_path(test_def_path)
    ok_test_res = classifier.predict(tests)
    def_test_res = classifier.predict(tests2)
    print(ok_test_res)
    print(def_test_res)

if __name__ == '__main__':
    main()