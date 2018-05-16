


import threading
import Work


"""
* The template class WorkPile provides a thread-safe means of controlling
* work done by multiple threads.  A WorkerThread will process
* work from a WorkPile until it reaches the end of that WorkPile.
* The template argument class must provide the following:
*
*		(1)  A constructor accepting an unsigned integer giving
*			  the number of separate work "chunks."
*		(2)  A prefix decrement operator.
*		(3)  A copy constructor.
*
"""

class WorkPile:



   ## Default constructor
      def __init__ ( self ):

           self.m_lock = threading.Lock()
           self.m_pile = list()
           self.m_current_work = iter( self.m_pile )

           self.reset()

      ## end constructor ###############

   ## Construct a WorkPile of a given size.
      def __init__ ( self, size ) :

         self.resize( size )

      ## end constructor #####################

      def size( self ):
      # Assure serial access here...
         with self.m_lock :

            return self.m_pile.size();

      ## end size #############################

   ## Resize
      def resize( self, size ):

      ## Use a Guard to assure serial access here...
         with self.m_lock:

            self.m_pile.resize( size )

            start = Work( size )

            for i in range(0, len(self.m_pile)) :

               self.m_pile[i] = start;
               start.decrement();

         ## end with scope

         self.reset()

      ## end resize #############################

  ### Add work.
      def add( self,  work ):

      ## Use a Guard to assure serial access here...
         with self.m_lock :

            self.m_pile.append( work )
            self.reset()

      # end add() ##################

      def begin( self ) :

          return iter( self.m_pile )

      ## end begin() ####################

   ## Return the next chunk of work.
      def next( self ) :

      ## Use a Guard to assure serial access here...
         with self.m_lock :

            ans = self.m_current_work

            if next(ans,None) is None :
                return ans

            next( self.m_current_work );

            return ans;

      ## end next ###############################

      def reset( self ):

      ## Use a locked scope to assure serial access here...
         with self.m_lock :

            self.m_current_work = iter( self.m_pile )

      ## end reset ///////////////////////////////////////

   ### Return an iterator to indicate the end.
      def end( self ):

      ## Use a Guard to assure serial access here...
         with self.m_lock :

            return self.m_pile.end()

      ## end end() #########################



## end  class WorkPile


## EOF
