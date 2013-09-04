import pygame
from pygame.color import THECOLORS

global Surface





class Window:
  def __init__(self):
    surface = self.surface = pygame.display.set_mode((0,0), pygame.RESIZABLE)
    background = self.background = pygame.Surface(surface.get_size())
    background.convert()
    



class Particles:

  #init the particle
  def __init__(self):
      self.widgets = []
      self.particlesCount = 0


      # xPos = 0
      # yPos = 0

      #need to get the pointer to the surface
      drawing_surface = pygame.display.get_surface()

      drawing_surface.fill((0,0,150))


     
      pygame.display.flip()


      # for widget in range(100):
      #   xPos += 10
      #   yPos += 10
      #   pygame.draw.circle(Surface.surface, [0,0,100], (xPos,yPos), 50) 




  def erase_screen(self):
    drawing_surface = pygame.display.get_surface()
    drawing_surface.fill((0,0,0))
    pygame.display.flip()

     



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



Surface = Window()