import pygame
from pygame.locals import *
import gui


import sys

#remove for production#
sys.dont_write_bytecode = True

class UserEvents:

  printEvent = True

  #useful for event keys: http://www.pygame.org/docs/ref/key.html
  def pollingInput(self, events):


          for event in events:
              #print "got into pollingInput" 
        
              if (self.printEvent == True):
                print event
         
              #should kill here instead of send message...quick fix..zZ
              if(event.type == pygame.QUIT):
                message = 'quit'
                event = ''
                return message , event

              elif(event.type == pygame.KEYDOWN):


                          if(event.key == K_ESCAPE):
                            pygame.exit(); sys.exit()

                          elif(event.key == K_i):
                            try:
                              reload(gui)
                              print "Success! reloaded particles!"
                              message = "reload"
                              event = ''
                              return message , event
                              
                            except Exception,e:
                              print str(e)
                              print "Unable to reload Particles" 

                          elif(event.key == K_e):
                            message = 'erase'
                            event = ''
                            return message , event


                          elif(event.key == K_p):
                            if self.printEvent == True:
                              self.printEvent = False
                            else:
                              self.printEvent = True

                          elif(event.key == K_s):
                            message = 'shutdown'
                            event = ''
                            return message , event

                          elif(event.key == K_z):

                            message = 'sample'
                            event = ''
                            return message , event

                          elif(event.key == K_x):
                            message = 'stopsample'
                            event = ''
                            return message , event

                          elif(event.type == pygame.KEYUP):
                            pass

              elif (event.type == pygame.MOUSEBUTTONDOWN ) or (event.type == pygame.MOUSEBUTTONUP):
                message = 'mouseevent'
                return message , event


          return '',''
          


            

                        
          

   


            ##########################
            #Problem:
            #        Looping over events should only be done once -- I imagine it will be intensive. 
            #        If there is already a looping of events in Display.process()...
            #        ...then all event logic needs to be programmed into the Display.process() 

            #        display.process() accepts an eventlist...Sweet!....we tried passing this
            #        to the Display instance, but it wasn't globally recognized between modules...

    




