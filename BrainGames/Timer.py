import pygame as pg
import time,sys
import pydoc
import typing


pg.init()

class Timer:
    '''a class that starts,ends, and grabs the current time '''


    def __init__(self,time:int = 30):
      '''this is a contructor for the Timer class 

      parameters: 
      time (int):default seconds for the timer.
      '''
      #self.font = pg.font.SysFont(None, 100)
      self._count = time #seconds
      self._timestarted = None
      self._finished = False
  
    (__init__.__doc__)



    def startTimer(self):
      self._timestarted = pg.time.get_ticks()
      
    

    def isFinished(self):
      '''checks if the timer is finished and returns the result

      :return: boolean

      '''
 
      return self._finished
           

    def getTime(self) -> float:
      if self._timestarted is None: 
        return self._count
      elapsed_time = self._count - (pg.time.get_ticks() - self._timestarted)/1000

      if  elapsed_time <= 0: 
       self._finished = True
      
      if self._finished :
        return 0.0
      return  elapsed_time

      
      


