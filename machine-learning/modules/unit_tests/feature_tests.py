#!/usr/bin/python

"""
features module unit tests.

Each class/method is tested against expected results from the given inputs.

(Uses the unit test module from the python libraries (similar to JUnit.)

"""

import sys

sys.path.append( ".." )


import unittest
import features

from Bio import SeqIO

class Feature_tests( unittest.TestCase ):

   """
      .
   """
   def test_compute( self ):

       seq_str = "GCTATAATAA"

       feature = features.PribnowBox()

       feature.compute( seq_str )

       self.assertEqual( feature.value, 1 )

       feature = features.MeltingTemperature()

       feature.compute( seq_str )

       self.assertFloatEqual( feature.value, 8.0, 0.001 )

       feature_set = { features.PribnowBox(),
                       features.MeltingTemperature()
                     }

       for feature in feature_set:

          feature.compute( seq_str )

          print( feature.name, " = ", feature.value )


       #end for

# end class Feature_tests

if __name__ == '__main__':
    unittest.main()

# EOF
