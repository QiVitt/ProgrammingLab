# TO DO..

class Model(object):

    def fit(self):
        pass

    def predict(self):
        pass

class LinearModel(Model):

    def __init__(self):
        self.angular_coeff = None
        self.intercept = None
        self.train_data = None

    def fit(self, train_data):
        pass