from .DistMeasure import cosine_sim
from FeatureExtraction.Vectorizer import vectorize_dataset
from Clustering.CKMeans import cluster_vectors, mean_of_clusters

class HOGBasedClassifier:
    def __init__(self):
        self.ok_model = None
        self.def_model = None

    def data_to_model(self, ok_img_list, def_img_list):
        vectorized_oks = vectorize_dataset(ok_img_list)
        vectorized_defs = vectorize_dataset(def_img_list)

        self.ok_model = mean_of_clusters(cluster_vectors(vectorized_oks))
        self.def_model = mean_of_clusters(cluster_vectors(vectorized_defs))

        return self.ok_model, self.def_model

    def change_models(self, ok_model, def_model):
        self.ok_model = ok_model
        self.def_model = def_model

    def predict(self, test_imgs:list):
        test = vectorize_dataset(test_imgs)
        predictions = []
        for vec in test:
            max_def = 0
            max_ok = 0
            for final in self.def_model:
                loc_res = cosine_sim(vec, final)
                if loc_res > max_def:
                    max_def = loc_res
            for final in self.ok_model:
                loc_res = cosine_sim(vec, final)
                if loc_res > max_ok:
                    max_ok = loc_res
            predictions.append("def" if max_def > max_ok else "ok")
        return predictions