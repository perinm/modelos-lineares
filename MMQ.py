import numpy as np


class MMQ():
    #     def __init__(self, x, y):
    #         self.x = np.array(x)
    #         self.y = np.array(y)
    #         self.n = x.shape[0]

    def fit(self, x, y):
        """
        x and y must be lists or tuples
        this function calculates values a and b for linear model

        """
        x = np.array(x)
        y = np.array(y)
        n = x.shape[0]

        # Q1, Q2, Q3 e Q4
        q1 = np.sum(x * y)
        q2 = (1 / n) * np.sum(y) * np.sum(x)
        q3 = np.sum(x ** 2)
        q4 = (1 / n) * np.sum(x) ** 2
        self.a = (q1 - q2) / (q3 - q4)
        self.b = (1 / n) * np.sum(y) - (self.a / n) * np.sum(x)
        print("O valor de a é:", self.a)
        print("O valor de b é:", self.b)
        print(self)

    def predict(self, x1):
        pass

    def mostra_funcao(self):
        print(self)

    def __str__(self):
        return ("função: y = %.2f*x + %.2f" % (self.a, self.b))