import numpy as np


class MMQ():
    def __init__(self, x=[], y=[]):
        self.x = x
        self.y = y
        self.dimension = len(x)
        self.a = None
        self.b = None

    def coef_a(self):
        """
        x and y must be lists or tuples
        this function calculates values a and b for linear model

        """
        term_1 = np.dot(self.x, self.y)
        n = self.dimension
        term_2 = np.sum(self.x) * np.sum(self.y)
        squared_x = np.dot(self.x,self.x)
        squared_sum = np.sum(self.x) ** 2
        epsilon = 10**-9

        up_term = term_1 - (1/n) * term_2
        down_term = squared_x - (1/n) * squared_sum + epsilon

        coef = up_term/down_term

        return term_1, n, term_2, squared_x,coef

    def coef_b(self):
        term_1 = np.sum(self.y)
        n = self.dimension
        x_sum = np.sum(self.x)
        a = self.coef_a()[5]
        coef = (1/n) * (term_1 - a * x_sum)
        return [term_1, n, x_sum, round(coef, 2)]

    # def predict(self, x1):
    #     pass
    #
    # def mostra_funcao(self):
    #     print(self)
    #
    # def __str__(self):
    #     return "função: y = %.2f*x + %.2f" % (self.a, self.b)
