# -*- coding: utf-8 -*-
"""
Created on Sun May 13 07:30:06 2018

@author: bgossage
"""

import sys

sys.path.append( ".." )

import unittest
import WorkPile
import WorkThread
import Work


//
// A chunk of work (partial sum) to compute Pi
//
class PiWork( Work ) :


    def __init__ ( self, chunks=1 ) :

       Work.__init__( self )  # NOTE:Calls the base-class constructor

       partial_sum = 0.0  ## the partial sum

       thread_id = 0      ## the id of the thread that computed it

## end class PiWork

##
## A function object to compute a partial sum
##



class MeanWork( Work ):

      def __init__( chunks=1 ) :
         Work.__init__(chunks)
         partial_sum = 0.0
         thread_id = 0


     char align[40];
     size_t start;
     size_t end;

};// end class MeanWork

class MeanSummer :

      def __init__(  data ) :

         m_data = data


      def __call__( work, id=0 ) :

         sum = 0.0
         numchunks = work.nchunks()

         total_size = len( m_data )
         length = total_size / numchunks
         start =  length * (work.chunk()-1)
         end = start + length-1

         if end >= len(m_data) :
            end = len( m_data) - 1

         for  i in range( start, end) :

            sum += m_data[i]
            sum += sin( double(i) ) * sqrt( double(i) )

         work.partial_sum = sum
         work.thread_id = id
         work.start = start
         work.end = end

      ##  end operator () //////////////


## end class MeanSummer //////////////////////////////


void PWork_test::parallel_mean()
{
  typedef sgp_threads::WorkPile<MeanWork> MeanWorkPile;

   size_t work_pile_size = 800;
   size_t size = 4000000;

   data = numpy.array( size )
   data.fill( 1.0 )

   work_pile = WorkPile( work_pile_size )
   mean_worker = MeanSummer( data )

   max_procs = 7

 ##  sgp_core::StopWatch timer;

   for  int num_procs= range(1,max_procs) :

   # Start the timer...
    #  timer.start();

   ## Run the test...
      sgp_threads::ProcessWorkpile( mean_worker, work_pile, num_procs );
      work_pile.reset();

   ## Stop the timer and show the elapsed time....
      timer.stop();
      cout << "Elapsed time= " << timer.elapsedTime();

   ## Gather up the partial sums...
      sum = 0.0
      MeanWorkPile::iterator itr= work_pile.begin();
      for(; itr!=work_pile.end(); ++itr )

         sum += (*itr).partial_sum;
##         cout << "partial sum from: " << (*itr).thread_id << "  ";
##         cout << (*itr).start << " - "  << (*itr).end << endl;

      mean = sum / double(size);

   ##   cout << "  num procs = " << num_procs << "  ";
    ##  cout << setw(16) << setprecision(16) << "mean = " << mean << endl;

   ## end for


## end parallel_mean ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



