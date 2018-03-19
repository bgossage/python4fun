import numpy as np

#####       Core Logistic Regression Algorithm Functions

class Simple_Logistic_Regression:

    def __init__(self, alpha, regularization, epoch):
        self.alpha = alpha
        self.regularization = regularization
        self.epoch = epoch

    def Sigmoid(self, hyp):
        sigmoid = 1 / (1 + np.exp(-hyp))
        return sigmoid

    def Hypothesis(self, X, Theta):
        hyp = np.matmul(X, Theta)
        hyp = self.Sigmoid(hyp)
        return hyp

    def Cost_function(self, hypothesis, Theta, Y, m):
        sum_one = np.ones(m).reshape((m, 1))
        sum_two = np.ones(2).reshape((2, 1))
        reg_Theta = np.array([[0], [Theta[1]]])
        part1 = np.matmul(Y.T, np.log(hypothesis)) + np.matmul((1 - Y).T, (np.log(1 - hypothesis)))
        part2 = (np.matmul(sum_two.T, np.square(reg_Theta))) * (self.regularization / 2)
        cost = (-1 / m) * (part1 + part2)
        return cost

    def Gradient_descent(self, Theta, X, Y, m):
        reg_Theta = np.array([[0], [Theta[1]]])
        hypothesis = self.Hypothesis(X, Theta)
        Theta = Theta - ((np.matmul(X.T, (hypothesis - Y)) / m) + self.regularization * reg_Theta) * self.alpha
        return Theta

    def Train(self, X, Y, m):
        Theta = np.array([[0], [0]])
        error = (np.empty(1)).reshape((1, 1))
        for i in range(self.epoch):
            Theta = self.Gradient_descent(Theta, X, Y, m)
            cost = self.Cost_function(self.Hypothesis(X, Theta), Theta, Y, m)
            if (i < self.epoch):
                error = np.concatenate((error[:], cost), axis=0)
        return Theta
