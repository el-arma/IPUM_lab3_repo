import joblib


class SVMModel:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self, model_path="model/svm_iris_model_v1.joblib"):
        loaded_model = joblib.load(model_path)

        return loaded_model

    def predict(self, X):
        return self.model.predict(X)
