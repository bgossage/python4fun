
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

   private:
      size_t m_cols;
      size_t m_rows;

      std::vector<value_type> m_data;

};// end class FloatArray


int main ( int argc, char* argv[] )
{
   size_t N = 2048;
   FloatArray data ( N, N );
   volatile float val = 0.0f;  // Prevent the compiler from optimizing this away.

   high_resolution_clock::time_point start = high_resolution_clock::now();
// Cache-coherent nested loop
   for( size_t i=0; i<N; i++ )
      for( size_t j=0; j<N; j++ )
      {
         val = data( i, j );  // Inner loop over columns
      }
   high_resolution_clock::time_point stop = high_resolution_clock::now();
   duration<double> time_span = duration_cast<duration<double>>( stop - start );

   std::cout << "Cache-Coherent loop took " << time_span.count () << " seconds.";
   std::cout << std::endl;

   start = high_resolution_clock::now();
// Non cache-coherent nested loop...
   for( size_t i=0; i<N; i++ )
      for( size_t j=0; j<N; j++ )
      {
         val = data ( j, i );  // Inner loop over rows (down the columns)
      }
   stop = high_resolution_clock::now ();
   time_span = duration_cast<duration<double>>( stop - start );

   std::cout << "Cache Non-Coherent loop took " << time_span.count () << " seconds.";
   std::cout << std::endl;

}// end main ~~~~~~~~~~~~~~~~~~


// EOF

