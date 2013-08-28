import pygame
import time
import sys
import os

from pygame.locals import *
from pygame.color import THECOLORS




class UserEvents:

  #useful for event keys: http://www.pygame.org/docs/ref/key.html
  def pollingInput(self):
    for event in pygame.event.get():
      print event

      if(event.type == pygame.QUIT):
        return 'quit'

      elif(event.type == pygame.KEYDOWN):

        if(event.key == K_ESCAPE):
          return 'quit'

      elif(event.type == pygame.KEYUP):
        pass

      elif(event.type == pygame.MOUSEBUTTONDOWN):
        pass

      elif(event.type == pygame.MOUSEBUTTONUP):
        pass



      
class drawingWindow:
  def __init__(self):
    self.surface = pygame.display.set_mode((0,0), pygame.RESIZABLE)


  def erase_screen(self):
    self.surface.fill(THECOLORS['black'])
    pygame.display.flip()







# zZz
def main():

  #give me a few global classes to play with
  global Surface, EventControl


  

  #intialize pygame module's
  pygame.init()

  #initate classes
  Surface = drawingWindow()
  EventControl = UserEvents()


  #a clock to track time between frames
  myclock = pygame.time.Clock()

  #Variables
  framerate_limit = 400 


  time_s = 0.0

  
  #Program Loop
  on = True
  while(on):

    #myclock.tick() computes how many milliseconds have passed since the previous call in the last frame
    #converted into seconds
    delta_time_s = float(myclock.tick(framerate_limit) * 1e-3)

    eventReturn = EventControl.pollingInput()

    if( eventReturn == 'quit'):
      on = False

    #time since initialization
    time_s += delta_time_s

    print time_s



main()


