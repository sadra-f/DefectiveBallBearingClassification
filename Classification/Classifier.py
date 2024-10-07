from .DistMeasure import cosine_sim


class HOGBasedClassifier:
    def __init__(self, ok_model, def_model):
        self.ok_model = ok_model
        self.def_model = def_model


    def predict(self, test:list):
        predictions = []
        for vec in test:
            max_def = 0
            max_ok = 0
            for final in self.model_def:
                loc_res = cosine_sim(vec, final)
                if loc_res > max_def:
                    max_def = loc_res
            for final in self.model_ok:
                loc_res = cosine_sim(vec, final)
                if loc_res > max_ok:
                    max_ok = loc_res
            predictions.append("def" if max_def > max_ok else "ok")
        return predictions