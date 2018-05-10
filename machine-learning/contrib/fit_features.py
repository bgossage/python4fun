# -*- coding: utf-8 -*-
"""
A module for reading machine learning feature data inputs

"""

import sys
import matplotlib
import matplotlib.pyplot
import sklearn.svm
from sklearn.model_selection import validation_curve
from sklearn.metrics import precision_recall_fscore_support
import numpy
#
# Setup path to modules...
#
sys.path.append( "../modules" )

import featureIO


#
# Begin main program...
#
try:
#
# Define default inputs...
#
    featuresFile = "../data/all_substrings.csv"


# Check for command-line arguments...
    if( len(sys.argv) == 2 ):
       featuresFile = sys.argv[1]


# Read features file...
    header_labels, X, Y = featureIO.read_features( featuresFile )

    m, n = X.shape

# Randomize the rows of X and Y...
    random_indices = numpy.random.permutation( m )

    Xrand = X[ random_indices ]
    Yrand = Y[ random_indices ]

# Divide the examples into training, validation, and test sets...
    sections = numpy.trunc([m*0.6, m*0.8, m]).astype(int)

    Xtrain, Xval, Xtest, end = numpy.split( Xrand, sections )
    Ytrain, Yval, Ytest, end = numpy.split( Yrand, sections )

# Train on the training set...
    model = sklearn.svm.SVC( C=1.0, gamma=1.0 )
    model.fit( Xtrain, Ytrain )

# Compute metrics for the training and validation sets for different
# values of the regularization parameter 'C"...
# NOTE: creates own subsets
    Cvals = numpy.linspace(1.0,5.0, 10)

    c_train_scores, c_valid_scores = validation_curve( sklearn.svm.SVC(),
                                                   X, Y,
                                                   "C", Cvals
                                                  )
    gammaVals = numpy.linspace(0.1,5.0, 10)

    gamma_train_scores, gamma_valid_scores = validation_curve( sklearn.svm.SVC(),
                                                                X, Y,
                                                               param_name="gamma",
                                                               param_range=gammaVals
                                                             )


# TODO: Repeat for gamma and plot the scores vs (C, gamma).


# Predict the test set...
    Yp = model.predict( Xtest )

# Compute test metrics...
    precision, recall, fscore, support = precision_recall_fscore_support( Ytest, Yp )

## precision = TP / (TP + FP)
## recall = TP / (TP + FN)
## fscore = 2 * (precision * recall) / (precision + recall)

    print('bacterial precision: {}'.format(precision[0]))
    print('bacterial recall:    {}'.format(recall[0]))
    print('bacterial fscore:    {}'.format(fscore[0]))
    print('bacterial support:   {}'.format(support[0]))

    print('human     precision: {}'.format(precision[1]))
    print('human     recall:    {}'.format(recall[1]))
    print('human     fscore:    {}'.format(fscore[1]))
    print('human     support:   {}'.format(support[1]))

 #   matplotlib.pyplot.legend(loc='upper right')
 #   matplotlib.pyplot.show()

except Exception as err:
   print( "An error occured: ", err )
   sys.exit( -1 )
except:
   print( "Unknown error \n" )
   sys.exit( -1  )



