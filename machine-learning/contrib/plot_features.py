# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import matplotlib


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
    featureName_1 = "GCCACCATGG"
    featureName_2 = "TATATAA"

# Check for command-line arguments...
    if( len(sys.argv) == 4 ):
       featuresFile = sys.argv[1]
       featureName_1 = sys.argv[2]
       featureName_1 = sys.argv[3]

# Read features file...
    header_labels, X, Y = featureIO.read_features( featuresFile )

# Get the desired columns...
    feature1 = header_labels.index(featureName_1)-1
    feature2 = header_labels.index(featureName_2)-1
    num_features = len( header_labels ) - 2

    print( "Index 1 = ", feature1, "  Index 2 = ", feature2, "\n" )

    x1 = X[:,feature1]
    x2 = X[:,feature2]
    colors =  Y.astype(int) * 50 + 1

    print( colors )

    matplotlib.pyplot.scatter( x1, x2, colors );
    matplotlib.pyplot.show()

except Exception as err:
   print( "An error occured: ", err )
   sys.exit( -1 )
except:
   print( "Unknown error \n" )
   sys.exit( -1  )



