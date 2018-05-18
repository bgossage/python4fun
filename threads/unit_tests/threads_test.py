# -*- coding: utf-8 -*-
"""
Created on Sun May 13 07:30:06 2018

@author: bgossage
"""

import sys

sys.path.append( ".." )

import unittest
import math
import numpy

import WorkPile
import WorkThread
import Work


##
## A function object to compute a partial sum
##



class MeanWork( Work ):

      def __init__( self, chunks=1 ) :
         super().__init__(chunks)
         m_partial_sum = 0.0
         m_thread_id = 0



## end class MeanWork

class MeanSummer( Work ):

      def __init__( self, data ) :

         self.m_data = data


      def __call__( self, work, id=0 ) :

         sum = 0.0
         numchunks = work.nchunks()

         total_size = len( self.m_data )
         length = total_size / numchunks
         start =  length * (work.chunk()-1)
         end = start + length-1

         if end >= len(self.m_data) :
            end = len( self.m_data) - 1

         for  i in range( start, end) :

            sum += self.m_data[i]
            sum += math.sin( float(i) ) * math.sqrt( float(i) )

         work.partial_sum = sum
         work.thread_id = id
         work.start = start
         work.end = end

      ##  end operator () //////////////


## end class MeanSummer //////////////////////////////


class PWork_test( unittest.TestCase ):

    def parallel_mean( self ) :

       work_pile_size = 800
       size = 4000000

       data = numpy.zeros( size )
      
       work_pile = WorkPile( work_pile_size )
       mean_worker = MeanSummer( data )

       max_procs = 7

     ##  sgp_core::StopWatch timer;

       for  num_procs in range(1,max_procs) :

       # Start the timer...
        #  timer.start();

       ## Run the test...
          ProcessWorkpile( mean_worker, work_pile, num_procs )

          work_pile.reset()

       ## Stop the timer and show the elapsed time....
         ##timer.stop();
         ## cout << "Elapsed time= " << timer.elapsedTime();

       ## Gather up the partial sums...
          sum = 0.0
          for work in work_pile :

             sum += work.partial_sum
          print( "partial sum from: " << work.thread_id, "  " )
          print( work.start, " - ", work.end )

          mean = sum / float(size)

          print( "  num procs = ", num_procs )
          print( "mean = ", mean )

       ## end for


    ## end parallel_mean ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



