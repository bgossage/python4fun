# -*- coding: utf-8 -*-
"""
A module of DNA sequence features


"""
##
# A common base class for features
#
class  Feature:

##
## Constructor.
#
   def __init__( self ):

      self.description = str()

      self.name = str()

      self.value = 0.0

      self.tag = str()

      self.origin = str()

   # end constructor ~~~~~~~~~~~~~~~~~~~~~~~~

##
## Base class compute function - derive classes can override this
## to customize their behavior.
#
   def compute( self, sequence ):
        count = 0 #initialize a count value

        sub_len = len(self.tag)
        for z in range(len(sequence)):
        # Accesses s by index to check if a substring
        # is present within the current position in s

             if s[z:z+sub_len] == self.tag:
                 count +=1 #if a substring is found increment count

        self.value = count

    ## end compute() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# EOF




