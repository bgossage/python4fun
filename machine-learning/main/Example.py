import numpy as np
import matplotlib.pyplot as plt
from Simple_Logistic_Regression import Simple_Logistic_Regression

# Training data set is a matrix with N (rows) number of samples and M (columns) number of features.
# This training data contains one feature in the column one. Column two is what we will try to predict given the feature. Our algorithm returns prediction value from 0 to 1.
training_data = np.array([[0.5, 0], [0.75, 0], [1, 0],
                          [1.25, 0], [1.5, 0], [1.75, 0],
                          [2.0, 0], [4.0, 1], [4.25, 1],
                          [4.5, 1], [4.75, 1], [5.0, 1],
                          [5.5, 1]])

# Features (Predictor)
# Features (X) represent predictor values.. in our case, for example, it would be the number of kozak sequences found in a given analyzed genome as input..
Features = np.array([[0.5], [0.75], [1],
                    [1.25], [1.5], [1.75],
                    [2.0], [4.0], [4.25],
                    [4.5], [4.75], [5.0],
                    [5.5]])

# Output (Predict)
# The output (Y) is the correct output for the given input (Features).
Y = np.array([[ 0.], [ 0.], [ 0.],
              [ 0.], [ 0.], [ 0.],
              [ 0.], [ 1.], [ 1.],
              [ 1.], [ 1.], [ 1.],
              [ 1.]])

#####    Pre-processing
m = len(Y)
alpha = 0.1
regularization = 0
epoch = 5000
ones = np.ones((m,1))
X = np.concatenate((ones, Features), axis=1)

#####    Training
machine_learning = Simple_Logistic_Regression(alpha,regularization, epoch)

#As you can see, the function call to train our machine to predict is very simple.
Theta = machine_learning.Train(X, Y, m)

#####    Graph the result
plt.plot(Features, Y, 'ro')
plt.xlabel("Features (Predictor) labels")
plt.ylabel("Output (Predict) labels")

X = np.concatenate((ones, Features), axis=1)
hyp = machine_learning.Hypothesis(X, Theta)

plt.plot(Features, hyp, 'k-', lw=1)
plt.show()
