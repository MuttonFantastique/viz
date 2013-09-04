import pygame
from pygame.color import THECOLORS
from pygame import Rect

import planes
from planes import Display




class Particles:

  #Variables
  framerate_limit = 400 
  time_s = 0.0



  #init the particle
  def __init__(self):
      try:
        self.rootPlane = Display()
      except:
        print "Problem with rootPlane"

      self.widgets = []

      #clock to track time between frames
      self.myclock = pygame.time.Clock()  
     



  def erase_screen(self):
    drawing_surface = pygame.display.get_surface()
    drawing_surface.fill((0,0,0))
    pygame.display.flip()

    


  #Fix when you need time   
  def time(self):


    #VerboseComment(VC):
    #myclock.tick() computes how many milliseconds have passed since the last frame
    #followed by a conversion from millisecond into seconds
    dx_s = float(self.myclock.tick(framerate_limit) * 1e-3)

    #time since initialization
    time_s += dx_s

    return time_s


  def update_SpeedandPosition(self):


    for widget in self.widgets:
      pass    


  def collision_detection(self):


    for widget in self.widgets:
      pass
      



  #draws the particles on the screen
  def drawParticle(self):

    for widget in self.widgets:
      pass


