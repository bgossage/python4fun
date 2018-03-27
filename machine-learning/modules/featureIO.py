# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import numpy

#
# Setup path to modules...
#
sys.path.append( "../modules" )

#
# Define a function to test for a valid float string
def is_float( s ):
   ans = True
   try:
       float(s)
   except( ValueError, TypeError ):
      ans = False

   return ans

# end is_float() ~~~~~~~~~~~~~~~~~~~~~~~~

#
# Define a function to read a features CSV file
#
def read_features( filename ):

# Return values
    labels = []
    X = []
    Y = []

# Read the header column labels...
    with open( filename, "r" ) as file:
       first_line = file.readline().rstrip()
       labels  = first_line.split( ',' )

# Load the rest of the data...
    feature_data = numpy.loadtxt( filename,
                                  delimiter=',',
                                  skiprows=1,
                                  dtype='float',
                                  converters = {0: lambda s: is_float(s) or 0 }
                                )

# Get number of features...
    num_features = len( labels ) - 2
#
# The feature set is in the middle columns...
    X = feature_data[ :, 1:num_features ]

# The ground truth is in the last colum...
    Y = feature_data[ :, num_features+1]

# Return the three outputs as a tuple...
    return (labels, X, Y)

# end function read_features ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# EOF




