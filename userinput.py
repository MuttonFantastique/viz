import pygame
from pygame.locals import *
import particles





class UserEvents:

  #useful for event keys: http://www.pygame.org/docs/ref/key.html
  def pollingInput(self):
    for event in pygame.event.get():
      print event

      if(event.type == pygame.QUIT):
        return 'quit'

      elif(event.type == pygame.KEYDOWN):

        if(event.key == K_ESCAPE):
          pygame.exit(); sys.exit()

        if(event.key == K_i):
          try:
            reload(particles)
            print "Success! reloaded particles!"
            return "reload"
          except Exception,e:
            print str(e)
            print "Unable to reload Particles" 

        elif(event.key == K_e):
          return 'erase'



      elif(event.type == pygame.KEYUP):
        pass

      elif(event.type == pygame.MOUSEBUTTONDOWN):
        pass

      elif(event.type == pygame.MOUSEBUTTONUP):
        pass


