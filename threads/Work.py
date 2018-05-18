
"""
* The class Work provides a generic work type for constructing
* a WorkPile.  It provides the constructor and decrement
* operator required by the WorkPile class. It also provides
* the less-than operator required by the WorkerThread class.
* Work is divided into a given number of "chunks".  An instance of
* the class Work maintains the total number of chunks and the id of
* the current chunk.  Thread safety is provided by the WorkPile.
"""

class Work :

   ## The constructor.
      def __init__( self, chunks=1 ) :
          self.m_chunk = chunks
          self.m_numChunks = chunks

   ## The prefix decrement operator.
      def decrement ( self ) :
         if  self.m_chunk > 0  :
            self.m_chunk = self.m_chunk - 1
            return self

   ## The less than operator.
      def __lt__ ( self, work ) :
         return self.m_chunk < work.m_chunk

   ## The greater than operator.
      def __gt__ ( self, work ) :
         return self.m_chunk > work.m_chunk

   ## Return the current chunk of work.
      def chunk( self ) :
          return self.m_chunk

   ## Return the total number of work chunks.
      def nchunks( self ) :
          return self.m_numChunks

## end class Work


## EOF
