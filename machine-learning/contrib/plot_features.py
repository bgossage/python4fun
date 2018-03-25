# -*- coding: utf-8 -*-
"""
A module for reading machine learning feature data inputs

"""

import sys
import matplotlib
import matplotlib.pyplot

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
    feature1 = 5
    feature2 = 7

# Check for command-line arguments...
    if( len(sys.argv) == 4 ):
       featuresFile = sys.argv[1]
       feature1 = int(sys.argv[2])
       feature2 = int(sys.argv[3])

# Read features file...
    header_labels, X, Y = featureIO.read_features( featuresFile )

# Get the desired columns...
    num_features = len( header_labels ) - 2

    print( "Index 1 = ", feature1, "  Index 2 = ", feature2, "\n" )

    x1 = X[:,feature1]
    x2 = X[:,feature2]
    colors =  Y.astype(int) * 50 + 1

    bx1 = x1[ Y==0 ]
    bx2 = x2[ Y==0 ]

    hx1 = x1[ Y==1 ]
    hx2 = x2[ Y==1 ]

    scale = 2

    matplotlib.pyplot.scatter( bx1, bx2, s = 2, c='r',
                               marker='+'
                             );
    matplotlib.pyplot.scatter( hx1, hx2, s=64,
                               c = 'b',
                               marker='o'
                             );
    matplotlib.pyplot.show()

except Exception as err:
   print( "An error occured: ", err )
   sys.exit( -1 )
except:
   print( "Unknown error \n" )
   sys.exit( -1  )



