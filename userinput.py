import pygame
from pygame.locals import *
import gui

import logging
import sys

#remove for production#
sys.dont_write_bytecode = True

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')





import logging
import logging.config
logging.basicConfig(filename='log/client.log', filemode='w', level=logging.CRITICAL)

logger = logging.getLogger(__name__)
logger.info('logging from userinput.py')



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

                          elif(event.key == K_r):
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
                            message = 'stop_sample'
                            event = ''
                            return message , event

                          elif(event.key == K_PERIOD):
                            message = 'turn_on_logging'
                            event = ''
                            return message, event

                          elif(event.key == K_SLASH):
                            message = 'turn_off_logging'
                            event = ''
                            return message, event

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


            #        Did I fix this when I hacked Planes so that process was only called on the particular event instead of 
            #        iterating over the entire event twice...yes it appears


            #        What was my design decision for creating a seperate module and class for iterating over events?
            #        The module makes litte difference and the class was setup because I thought I would be decorating events
            #        I might want to merge with main and only keep the function

    




