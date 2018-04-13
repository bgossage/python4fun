# -*- coding: utf-8 -*-
"""
A module of DNA sequence features


"""

from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp



##
# A common base class for features
#
class  Feature:

##
## Constructor.  NOTE: 'self' is a reference to an object instance of class 'Feature'
#
   def __init__( self ):

   # Define and initialize the member variables
   # NOTE:  Initialize with valid default values.

      self.description = str()

      self.name = str()

      self.value = 0.0

      self.origin = str()

   # Define the common compute interface for all derived classes...
   def compute( self, sequence ):
       pass

   # end constructor ~~~~~~~~~~~~~~~~~~~~~~~~

#end class Feature

##
# A common base class for features computed by counting sub-strings
#
class  SubstringFeature( Feature ):

##
## Constructor.  NOTE: 'self' is a reference to an object instance of class 'Feature'
#
   def __init__( self ):
      Feature.__init__(self)  #NOTE: Call the base class init

   # Define and initialize the member variables
   # NOTE:  Initialize with valid default values.

      self.tag = str()

   # end  SubstringFeature constructor ~~~~~~~~~~~~~~~~~~~~~~~~


##
## Base class compute function - derived classes can override this
## to customize their behavior.
#
   def compute( self, sequence ):
        count = 0 #initialize a count value

        sub_str = self.tag

        sub_len = len(sub_str)
        for z in range(len(sequence)):
        # Accesses sequence by index to check if a substring
        # is present within the current position in s

             if sequence[z:z+sub_len] == sub_str:
                 count +=1 #if a substring is found increment count

        self.value = count

    ## end compute() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#end class SubStringFeature


##
# A derived class of SubstringFeature
#
class  PribnowBox( SubstringFeature ):

##
## Constructor.
#
   def __init__( self ):
      SubstringFeature.__init__( self )  # NOTE:Calls the base-class constructor

   # Overwrite the base class member variables

      self.description = "TATAAT promoter region for transcription in bacteria"
      self.name = "Pribnow Box"
      self.tag = "TATAATA"

   # end PribnowBox init ~~~~~~~~~~~~~~~~~~~~~~~~

#end class PribnowBox

#
# Derive a sub-class of Feature
#
class MeltingTemperature( Feature ):  # Derive as a sub-class of class 'Feature'

   def __init__( self ):
       Feature.__init__( self )

       self.name = "MeltingTemperature"

   # Override base class Feature compute()
   def compute( self, sequence ):

      seq = Seq( sequence )

      ans = MeltingTemp.Tm_GC( seq )

      self.value = ans

    ## end compute() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# end class MeltingTemp


# EOF




