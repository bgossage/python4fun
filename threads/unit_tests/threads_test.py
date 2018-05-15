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
class PiSummer
{
   public:
   ## The series function.
      def f( sefl, a ) :

         return (4.0 / (1.0 + self.a * self.a) )


   ## Compute the partial sum for a given chunk of work
      def operator()( PiWork& work, int id=0 )
      {
         const size_t n = 10000000;

         const double h   = 1.0 / static_cast<double>(n);

         double sum = 0.0;
         double x = 0.0;
         size_t numchunks = work.nchunks();

         for( size_t i = work.chunk() + 1; i <= n; i += numchunks )
         {
            x = h * (static_cast<double>(i) - 0.5);
            sum += f(x);
         }
         work.partial_sum = h * sum;
         work.thread_id = id;

      ##  end operator () #################

## end class PiSummer


void PWork_test::parallel_pi()
{
   sgp_threads::Work my_work;

// Construct the workpile...
   typedef sgp_threads::WorkPile<PiWork> PiWorkPile;

   size_t work_pile_size = 32;
   double pi = 0.0;

   PiWorkPile work_pile( work_pile_size );
   PiSummer pi_worker;


   const int max_procs = NUM_CPUS;


   sgp_core::StopWatch timer;

// Run multiple cases, each case with more processors...
   for( int num_procs=1; num_procs<=max_procs; num_procs++ )
   {
      timer.start();

   // Compute the partial sums using the given number of processors and threads...
      sgp_threads::ProcessWorkpile( pi_worker, work_pile, num_procs );
      work_pile.reset();

      timer.stop();
      cout << "Elapsed time = " << timer.elapsedTime();

   // Tally up the partial sums...
      double sum = 0.0;
      PiWorkPile::iterator itr= work_pile.begin();
      for(; itr!=work_pile.end(); ++itr )
      {
         sum += (*itr).partial_sum;
 //        cout << "partial sum from: " << (*itr).thread_id << endl;;
      }

      pi = sum;

      cout << "  num procs = " << num_procs << "  ";
      cout << setw(16) << setprecision(16) << "pi = " << pi << endl;

   }// end for


} // end parallel_pi ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
namespace
{
class MeanWork :  public sgp_threads::Work
{
   public:
      MeanWork( unsigned chunks=1 )
       : sgp_threads::Work(chunks),
         partial_sum(0.0),
         thread_id(0) {;}

      double partial_sum;
      int thread_id;
     char align[40];
     size_t start;
     size_t end;

};// end class MeanWork

class MeanSummer
{
   public:
      MeanSummer( TScalarArray<double>* data )
      : m_data(data) {;}


      void operator()( MeanWork& work, int id=0 )
      {
         double sum = 0.0;
         size_t numchunks = work.nchunks();

         size_t total_size = m_data->size();
         size_t length = size_t(total_size/numchunks);
         size_t start =  length * (work.chunk()-1);
         size_t end = start + length-1;

         if( end >= m_data->size() )
            end = m_data->size() - 1;

         for( size_t i = start; i < end; i++ )
         {
            sum += (*m_data)(i);
            sum += sin( double(i) ) * sqrt( double(i) );

         }
         work.partial_sum = sum;
         work.thread_id = id;
         work.start = start;
         work.end = end;

      }//  end operator () //////////////

   private:
      TScalarArray<double>* m_data;

};// end class MeanSummer //////////////////////////////

}// end anon namespace

void PWork_test::parallel_mean()
{
  typedef sgp_threads::WorkPile<MeanWork> MeanWorkPile;

   size_t work_pile_size = 800;
   size_t size = 4000000;

   TScalarArray<double> data( size );
   data.fill( 1.0 );

   MeanWorkPile work_pile( work_pile_size );
   MeanSummer mean_worker( &data );

   cout << "array size = " << size*sizeof(double)/1.0e9 <<  "Gb" << endl;

   const int max_procs = NUM_CPUS;

   sgp_core::StopWatch timer;

   for( int num_procs=1; num_procs<=max_procs; num_procs++ )
   {
   // Start the timer...
      timer.start();

   // Run the test...
      sgp_threads::ProcessWorkpile( mean_worker, work_pile, num_procs );
      work_pile.reset();

   // Stop the timer and show the elapsed time....
      timer.stop();
      cout << "Elapsed time= " << timer.elapsedTime();

   // Gather up the partial sums...
      double sum = 0.0;
      MeanWorkPile::iterator itr= work_pile.begin();
      for(; itr!=work_pile.end(); ++itr )
      {
         sum += (*itr).partial_sum;
//         cout << "partial sum from: " << (*itr).thread_id << "  ";
//         cout << (*itr).start << " - "  << (*itr).end << endl;
      }

      double mean = sum / double(size);

      cout << "  num procs = " << num_procs << "  ";
      cout << setw(16) << setprecision(16) << "mean = " << mean << endl;

   }// end for


} // end parallel_mean ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



