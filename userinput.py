import pygame
from pygame.locals import *
import particles


import sys



class UserEvents:

  printEvent = True

  #useful for event keys: http://www.pygame.org/docs/ref/key.html
  def pollingInput(self):
  
    
    for event in pygame.event.get(): 
        if (self.printEvent == True):
          print event
   
        if(event.type == pygame.QUIT):
          return 'quit'

        elif(event.type == pygame.KEYDOWN):


          if(event.key == K_ESCAPE):
            pygame.exit(); sys.exit()

          elif(event.key == K_i):
            try:
              reload(particles)
              print "Success! reloaded particles!"
              return "reload"
            except Exception,e:
              print str(e)
              print "Unable to reload Particles" 

          elif(event.key == K_e):
            return 'erase'

          elif(event.key == K_p):
            if self.printEvent == True:
              self.printEvent = False
            else:
              self.printEvent = True

          elif(event.key == K_s):
            return 'shutdown'

          elif(event.key == K_z):
            return 'sample'

          elif(event.key == K_x):
            return 'stopsample'



        elif(event.type == pygame.KEYUP):
          pass

        elif(event.type == pygame.MOUSEBUTTONDOWN):
          pass

        elif(event.type == pygame.MOUSEBUTTONUP):
          pass

        
        return




