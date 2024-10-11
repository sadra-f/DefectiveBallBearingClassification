
class Single_class_Evaluator:
    def __init__(self):
        self.all = None
        self.TP = None
        self.TN = None
        self.FN = None
        self.FP = None
        self.accuracy = None
        self.precision = None
        self.recall = None
        self.f1 = None


    def evaluate(self, test_res):
        self.all = len(test_res)
        self.TP = len([1 for i in test_res if i.cls==i.pred and i.cls=="ok"])
        self.TN = len([1 for i in test_res if i.cls==i.pred and i.cls=="def"])
        self.FN = len([1 for i in test_res if i.cls!=i.pred and i.cls=="def"])
        self.FP = len([1 for i in test_res if i.cls!=i.pred and i.cls=="ok"])
        self.accuracy = ( self.TP + self.TN ) / (all)
        self.precision = self.TP / (self.TP + self.FP)
        self.recall = self.TP / (self.TP + self.FN)
        self.f1 = ( 2 * self.precision * self.recall ) / (self.precision + self.recall)
        return {
            "all": self.all,
            "TP" : self.TP,
            "TN" : self.TN,
            "FN" : self.FN,
            "FP" : self.FP,
            "Accuracy" : self.accuracy,
            "Precision" : self.precision,
            "recall" : self.recall,
            "f1 score" : self.f1,
        }

