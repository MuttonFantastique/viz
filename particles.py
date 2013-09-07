import sys


import pygame
from pygame.color import THECOLORS
from pygame import Rect
from pygame.locals import *


import planes
from planes import Display
from planes.gui import Label, OutlinedText, Container


from collections import deque
#Lets get some widgets on our gui?
#or send a text string from gui to server


class GUI(planes.Display):

  #Variables
  framerate_limit = 400 
  time_s = 0.0



    # #init the particle
    # def __init__(self):

    #       #Not the correct way      
    #       # try:
    #       #   self.rootPlane = Display()
    #       # except:
    #       #   print "Problem with rootPlane"

    #     self.widgets = []

    #     #clock to track time between frames
    #     self.myclock = pygame.time.Clock()  


    #     try:
    #       self.labelPlane = Label('labelPlane', 'Viz-2.0 -- Inspired by Rian Shelly', Rect(100,100,300,300), text_color = (0,0,0), background_color = (150,150,150))
    #       self.labelPlane.redraw()

    #       self.Visual_label = OutlinedText('node','second text string')
    #       self.Visual_label.redraw()
    #       print "created label"


    #       self.plane_container = Container('container', background_color = (150,0,0))
    #       self.plane_container.sub(self.Visual_label)
    #       self.plane_container.sub(self.labelPlane)

    #     except:
    #       print "problems with label plane"
    #       error_tuple = sys.exc_info()
    #       for i in error_tuple:
    #         print i
       



  def erase_screen(self):
    drawing_surface = pygame.display.get_surface()
    drawing_surface.fill((100,0,0))
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
    pass

      


  def collision_detection(self):
      pass
      



  #draws the particles on the screen
  def drawParticle(self):
      pass

  def showmeSomething(self):
      pass
      




class ColorChangeSquare(planes.Plane):

  def __init__(self, name, rect, draggable = False, grab = False):

    planes.Plane.__init__(self, name, rect, draggable, grab)

    # custom extensions for movement, color
    #
    self.moving = True
    self.vector = (1, 0)
    self.colors = deque([(255, 128, 0), (0, 255, 128), (0, 0, 255)])

    self.image.fill(self.colors[0])

  def clicked(self, button_name):
    self.colors.rotate(-1)
    self.image.fill(self.colors[0])

  def update(self):

    if self.rect.top > (300 - self.rect.width - 25):

      self.rect.top = 300 - self.rect.width - 25

      # turn left
      #p
      self.vector = (-1, 0)

    if self.rect.left > (400 - self.rect.width - 25):

      self.rect.left = 400 - self.rect.width - 25

      # turn down
      #
      self.vector = (0, 1)

    if self.rect.top < 25:

      self.rect.top = 25

      # turn right
      #
      self.vector = (1, 0)

    if self.rect.left < 25:

      self.rect.left = 25

      # turn up
      #
      self.vector = (0, -1)

    if self.moving:
      self.rect.move_ip(self.vector[0], self.vector[1])





#Gui_Env = GUI((0,0))




