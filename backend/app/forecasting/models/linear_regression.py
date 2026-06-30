import joblib

from sklearn.linear_model import LinearRegression


class RevenueLinearRegression:

    def __init__(self):

        self.model = LinearRegression()

    def train(self, X_train, y_train):

        self.model.fit(
            X_train,
            y_train,
        )

    def predict(self, X):

        return self.model.predict(X)

    def save(self, path):

        joblib.dump(
            self.model,
            path,
        )

    def load(self, path):

        self.model = joblib.load(path)