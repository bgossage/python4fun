

import WorkerThread
import WorkPile


"""
*
* This template function ProcessWorkpile executes the work
*  to be done by a given function object (functor) with  a given
* numnber of threads.  Requirements on the object are those imposed by the WorkerThread
* class.  Requirements on the work object are those
* imposed by the WorkPile class.  The generic work
* type found in "Work.py" provides a good default.
*
* @param  worker  a callable object that will do the work.
* @param  workPile a sequence of objects that decompose the work into "chunks".
* @param  numProcs  the number of processors/threads to use
*
"""

def  ProcessWorkpile( worker, workPile, numProcs ) :

## If only one processor, execute the work on the parent thread...
   if numProcs == 1 :

      work_itr = workPile.next()

      while work_itr != workPile.end() :

         worker( work_itr,  0 )

         work_itr = workPile.next()

      ## end while

      return
  ## end if

## Create the set of threads that will do the work...
   theThreads = list();

## Define worker thread type...

## Create the worker threads and start them...
   for i in range(1,numProcs) :

      work_thread = WorkerThread( worker, workPile, i )

    #  work_thread->set_affinity( i-1 );

      theThreads.append( work_thread )

      work_thread.run()
   #end for

## Wait for all the threads to complete...
   for thread in theThreads:
      thread.join()

## Delete the threads...
   del theThreads[:]

## end ProcessWorkpile ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def PApplyWork( obj, work, size, numProcs ) :

## Create the workPile...
   theWorkPile = WorkPile( size )

   ProcessWorkpile( obj, theWorkPile, numProcs );

## end PApplyWork ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



## EOF
