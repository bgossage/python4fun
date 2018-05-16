# -*- coding: utf-8 -*-
"""
Created on Sun May 13 07:30:06 2018

@author: bgossage
"""

import threading


"""
* The WorkerThread provides the means for an
* object of a given type to do work of a given type in
* parallel.  A WorkerThread is constructed using a callable
* object and a WorkPile providing the work.  The callable
* function must take a work object as its single argument.
* The requirements for the work type are those imposed by the
* WorkPile.
"""


class WorkerThread( threading.Thread ):

   ## Construct a WorkerThread.
      def __init__( self, obj, workPile, worker_id=0 ):

        self.m_obj = obj
        self.m_workPile = workPile
        self.m_worker_id = worker_id


   ## Process work from the workPile (overrides Thread.run() ).
      def run( self ):

          ## Get the first available chunk of work...
             work_itr = self.m_workPile.next()

          ## Process work until none remain...
             while work_itr != self.m_workPile.end():

             ## Have the object's member function do some work...
                self.m_obj( work_itr, self.m_worker_id )

             ## Get the next chunk of work...
                work_itr = self.m_workPile.next()

             ## end while
      # end run


## end class WorkerThread
