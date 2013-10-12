import sys
import pygame
  # from pygame.color import THECOLORS
  # from pygame import Rect
  # from pygame.locals import *
import planes
  # from planes import Display
  # from planes.gui import Label, OutlinedText, Container
import logging
import logging.config
from collections import deque #pronounced deck and its a double ended que

#remove for production#
sys.dont_write_bytecode = True

logging.basicConfig(filename='log/client.log', filemode='w', level=logging.CRITICAL)

logger = logging.getLogger(__name__)
logger.info('Logging from GUI.py')



#nate made variables here
winHight = 500 #defines the hight and width in pixels
winWidth = 600
padding = 10# defines the empty space within the window to not be used
#end of nates variables 


class DropDisplay(planes.Display):

  def __init__(self):
    planes.Display.__init__(self, (winWidth,winHight))
    self.grab = True

    #to change the background of the window edit this block currently bg.png is non-essential
    #imgPos = pygame.Rect((0, 0), (0, 0))
    #bg = pygame.image.load('images/bg.png')
    #self.image.blit(bg, imgPos )

    self.sub(ColorChangeSquare("square", pygame.Rect((padding, padding), (50, 50)), draggable = True))
    #self.sub(DropZone("dropzone", pygame.Rect((100, 100), (200, 100)), draggable = True, grab = True))
    #self.dropzone.image.fill((0, 0, 128))



  def erase_screen(self):
     drawing_surface = pygame.display.get_surface()
     drawing_surface.fill((100,0,0))
     pygame.display.flip()



  def dropped_upon(self, plane, coordinates):

    if isinstance(plane, ColorChangeSquare):
      planes.Display.dropped_upon(self, plane, coordinates)
      plane.moving = True


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

#nate messed with this function. Made it so that the space between the box and the edge of the window can be modified with one change
#changed the conditions from a set value to a variable determined above, this allows for easier window resize. 
#NOTE: if the window is resized the variables stay the same and the behavior of the box stays the same. 
  def update(self):

    if self.rect.top > (winHight - self.rect.width - padding):#if the box attempts to go off of the bottom 
      self.rect.top = winHight - self.rect.width - padding
      self.vector = (-1, 0)# turn left

    if self.rect.left > (winWidth - self.rect.width - padding):#if the box attempts to go off the right
      self.rect.left = winWidth - self.rect.width - padding
      self.vector = (0, 1)# turn down

    if self.rect.top < padding:#if the box attempts to go off the top
      self.rect.top = padding
      self.vector = (1, 0) # turn right

    if self.rect.left < padding:#if the box attempts to go off the left
      self.rect.left = padding
      self.vector = (0, -1) # turn up

    if self.moving:
      self.rect.move_ip(self.vector[0], self.vector[1])

class DropZone(planes.Plane):

  def dropped_upon(self, plane, coordinates):

    planes.Plane.dropped_upon(self, plane, coordinates)

    plane.moving = True

    plane.draggable  = True



#### END OF THE FILE. THE FOLLOWING CODE WAS NOT WHAT THE ORDER DESIRES.




# class GUI(planes.Display):

#   #Variables
#   framerate_limit = 400 
#   time_s = 0.0



#      #init the particle
#      def __init__(self):

#            #Not the correct way      
#            # try:
#            #   self.rootPlane = Display()
#            # except:
#            #   print "Problem with rootPlane"

#          self.widgets = []

#          #clock to track time between frames
#          self.myclock = pygame.time.Clock()  


#          try:
#            self.labelPlane = Label('labelPlane', 'Viz-2.0 -- Inspired by Rian Shelly', Rect(100,100,300,300), text_color = (0,0,0), background_color = (150,150,150))
#            self.labelPlane.redraw()

#            self.Visual_label = OutlinedText('node','second text string')
#            self.Visual_label.redraw()
#            print "created label"


#            self.plane_container = Container('container', background_color = (150,0,0))
#            self.plane_container.sub(self.Visual_label)
#            self.plane_container.sub(self.labelPlane)

#          except:
#            print "problems with label plane"
#            error_tuple = sys.exc_info()
#            for i in error_tuple:
#              print i
       

 
#   #Fix when you need time   
#   def time(self):


#     #VerboseComment(VC):
#     #myclock.tick() computes how many milliseconds have passed since the last frame
#     #followed by a conversion from millisecond into seconds
#     dx_s = float(self.myclock.tick(framerate_limit) * 1e-3)

#     #time since initialization
#     time_s += dx_s

#     return time_s


#   def update_SpeedandPosition(self):
#     pass

      


#   def collision_detection(self):
#       pass
      



#   #draws the particles on the screen
#   def drawParticle(self):
#       pass