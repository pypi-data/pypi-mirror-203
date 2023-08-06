import numpy as np


class Perceptron:
    def __init__(self, eta, epochs):
        self.weights = np.random.randn(3) * 1e-4  # Weights initilization
        print(f"initial weights : {self.weights}")
        self.eta = eta
        self.epochs = epochs

    def activationFunction(self, inputs, weights):
        z = np.dot(inputs, weights)  # z = W*X
        return np.where(z > 0, 1, 0)  # Condition If Ture or False

    def fit(self, x, y):
        self.x = x
        self.y = y

        X_with_bias = np.c_[self.x, -np.ones((len(self.x), 1))]  # Concatation
        print(f"X with Bias : {X_with_bias}")

        for epoch in range(self.epochs):
            print(f"===============>> {epoch}/{self.epochs}")
            y_hat = self.activationFunction(
                X_with_bias, self.weights
            )  # Forward Propogation
            print(f"Pridicted value : {y_hat}")
            self.error = self.y - y_hat
            print(f"Error: {self.error}")
            self.weights = self.weights + self.eta * np.dot(
                X_with_bias.T, self.error
            )  # Backward Propogation
            print(f"New weights : {self.weights}")
            print(f"===============>> end of {epoch}")

    def predict(self, x):
        X_with_bias = np.c_[x, -np.ones((len(x), 1))]
        return self.activationFunction(X_with_bias, self.weights)

    def total_loss(self):
        total_loss = np.sum(self.error)
        print(f"Total Loss : {total_loss}")
        return total_loss
