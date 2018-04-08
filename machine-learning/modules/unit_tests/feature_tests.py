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


class Feature_tests( unittest.TestCase ):

   """
      .
   """
   def test_compute( self ):

       seq_str = "GCTATAATAA"

       feature = features.PribnowBox()

       feature.compute( seq_str )

       print( feature.name, "= ", feature.value )

       feature = features.MeltingTemperature()

       feature.compute( seq_str )

       print( feature.name, " = ", feature.value )

# end class Feature_tests

if __name__ == '__main__':
    unittest.main()

# EOF
