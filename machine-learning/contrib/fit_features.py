# -*- coding: utf-8 -*-
"""
A module for reading machine learning feature data inputs

"""

import sys
import matplotlib
import matplotlib.pyplot
import sklearn.svm
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


# Get the desired columns...
    num_features = len( header_labels ) - 2

    model = sklearn.svm.SVC( C=1.0, gamma=1.0 )
    model.fit( X, Y )

    Xin = X[m-1,:].reshape(1,-1)

    Yp = model.predict( Xin )

    Yp

 #   matplotlib.pyplot.legend(loc='upper right')
 #   matplotlib.pyplot.show()

except Exception as err:
   print( "An error occured: ", err )
   sys.exit( -1 )
except:
   print( "Unknown error \n" )
   sys.exit( -1  )



