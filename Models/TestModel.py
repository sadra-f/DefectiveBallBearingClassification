
class Img_model:
    def __init__(self, img, vector, visual, cls:{"def", "ok"}):
        self.img = img
        self.vector = vector
        self.visual = visual
        self.cls = cls
        self.prediction = None