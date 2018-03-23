# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

#
# Setup path to modules...
#
sys.path.append( "../modules" )

import math
import numpy
import matplotlib.pyplot

def is_float( s ):
   is_float = True
   try:
       f = float(s)
   except( ValueError, TypeError ):
      is_float = False
      
# end is_float() ~~~~~~~~~~~~~~~~~~~~~~~~
try: 

    featuresFile = "../data/all_substrings.csv"
    featureName_1 = "GCCACCATGG"
    featureName_2 = "TATATAA"
    
    
    if( len(sys.argv) == 4 ):
       featuresFile = sys.argv[1]
       featureName_1 = sys.argv[2] 
       featureName_1 = sys.argv[3] 
    
    header_labels = []
    with open( featuresFile, "r" ) as file:
       first_line = file.readline().rstrip()
       header_labels  = first_line.split( ',' )       
       print( header_labels , "\n" )
       
    feature1 = header_labels.index(featureName_1)
    feature2 = header_labels.index(featureName_2)
    num_features = len( header_labels ) - 2;
    

    print( "Index 1 = ", feature1, "  Index 2 = ", feature2, "\n" )
    
    feature_data = numpy.loadtxt( featuresFile,
                                  delimiter=',',
                                  skiprows=1,
                                  dtype='float',
                                  converters = {0: lambda s: is_float(s) or 0 }
                                  )
    
    print( feature_data )
    
    x1 = feature_data[:,feature1]
    x2 = feature_data[:,feature2]
    
    X = feature_data[ :, 1:num_features ]
    Y = feature_data[ :, num_features+1]
    
    print( "X = ", X, "\n" )
    print( "Y = ", Y, "\n" )
   
except Exception as err:
   print( "An error occured: ", err )
   sys.exit( -1 )
except:
   print( "Unknown error \n" )
   sys.exit( -1  )
   
   

