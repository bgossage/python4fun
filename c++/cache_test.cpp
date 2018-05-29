
#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

/**
   Define an array type just for testing loop access.
*/
class FloatArray
{
   public:
      typedef float value_type;

   // Constructor
      FloatArray ( size_t rows, size_t cols )
      : m_cols( cols ),
        m_rows( rows ),
        m_data( rows*cols ) { ; }

   // Index operator
      inline value_type const& operator () ( size_t i, size_t j  ) const
      {
         return m_data[i*m_cols + j];

      }// end operator ( i,j ) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      
   // Index operator
      inline value_type const& operator () ( size_t i ) const
      {
         return m_data[i];

      }// end operator ( i,j ) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   private:
      size_t m_cols;
      size_t m_rows;

      std::vector<value_type> m_data;

};// end class FloatArray

/**
 * A program to demonstrate cache-coherent 2D array access.
 * 
 */
int main ( int argc, char* argv[] )
{
// Define the size of the array in both dimensions...
   const size_t N = 2048;
   
// Create the array...
   FloatArray data ( N, N );
   
   volatile float val = 0.0f;  // Prevent the compiler from optimizing this away.

//// The cache-coherent loop accesses each element without skipping memory addresses.
// Start the timer...
   high_resolution_clock::time_point start = high_resolution_clock::now();
// Cache-coherent nested loop
   for( size_t i=0; i<N; i++ )
      for( size_t j=0; j<N; j++ )
      {
         val = data( i, j );  // Inner loop over columns
      }
// Stop the timer and print results
   high_resolution_clock::time_point stop = high_resolution_clock::now();
   duration<double> time_span = duration_cast<duration<double>>( stop - start );

   std::cout << "Cache-Coherent loop took " << time_span.count () << " seconds.";
   std::cout << std::endl;

/////////////////  The non-cache-coherent loop skips rows. /////////////////
   
   start = high_resolution_clock::now();
// Non cache-coherent nested loop...
   for( size_t i=0; i<N; i++ )
      for( size_t j=0; j<N; j++ )
      {
         val = data ( j, i );  // Inner loop over rows (down the columns)
      }
   stop = high_resolution_clock::now ();
   time_span = duration_cast<duration<double>>( stop - start );
   
   std::cout << "Cache non-coherent loop took " << time_span.count () << " seconds.";
   std::cout << std::endl;
   
///////////////// Try to hand-optimize away the extra multiply ////////////////////////
   
// "Optimal" nested loop...
   size_t row = 0;
   for( size_t i=0; i<N; i++ )
   {
      row = i * N;
      for( size_t j=0; j<N; j++ )
      {
         val = data ( row + j );  // Inner loop over rows (down the columns)
         
      }
   }
   stop = high_resolution_clock::now ();
   time_span = duration_cast<duration<double>>( stop - start );

   std::cout << "Cache Optimal, non-coherent loop took " << time_span.count () << " seconds.";
   std::cout << std::endl;

}// end main ~~~~~~~~~~~~~~~~~~


// EOF

