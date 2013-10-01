#! /usr/bin/env python
#
# viz-1.0
# GNU
#
#####################

#standard
import sys
import os

#import pygame environment
import pygame


#usage time.sleep(5.5) //seconds
import time

# brother/sister modules 
from userinput import *
from gui import *

# networking
import socket



# Start debug logging with . and stop with /
# Erase log and screen with e
import logging
import logging.config


#Explicit import pycallgraph




#TODO: Whats this again?
#remove for production#
sys.dont_write_bytecode = True



#hardcoded
#TODO: setup.py
sys.path.append('/home/blackpanther/Desktop/sdlHacking/working/')









# zZz
def main():


  

  

  
  #Major Classes
  EventControl = UserEvents()


  #TODO:use gitbucket issue tracker
  #BUG:
  #single change of Dropdisplay to (0,0) and everything breaks
  #check to see how the resolution tuple is used in Planes and find what is breaking it

  screen = DropDisplay()

 

  #TODO:
  #disabled try/except block due to the masking of errors...
  #
  # Connect to server
  #
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except socket.error, msg:
    print "Socket Error number: " + msg[0] + "\nError signal: " + msg[1]
    sys.exit()



  try:
    s.connect(('localhost', 9879))
  except: 
    print "exception raised trying to connect"










  #Variables
  signal = ''

  client = True
  #Main Program Loop
  while(client):

              
        events = pygame.event.get()
        if events:

          #returns a signal and event for triggered events 
          signal, event = EventControl.pollingInput(events)
        
        if signal:
              if( signal == 'quit'):
                s.close()
                pygame.exit()
                sys.close()

              elif( signal == 'reload'):
                  
                    from gui import *
                    screen = DropDisplay()        
                

              elif signal == 'erase':
                screen.erase_screen()

                #TODO: fix hard coding...error hiding is the devil
                try:
                  os.remove('/home/blackpanther/Desktop/sdlHacking/working/log/client.log')
                except:
                  pass


              #TEMPLATE TO SEND COMMANDS TO SERVER
              #TODO:  
              elif signal == 'shutdown':
                s.send('shutdown')



              elif signal == 'sample':
                  import pycallgraph
                  pycallgraph.start_trace()
                  # TODO:
                  # import cProfile
                  # cProfile.run('foo()')


              elif signal == 'stop_sample':
                pycallgraph.make_dot_graph('images/sample.png')
                #TODO: check to see if you need to stop pycallgraph.start_trace()

              elif signal == 'mouseevent':
                screen.process(event)


              elif signal == 'turn_on_logging':
                logging.basicConfig(filename='log/client.log', filemode='w', level=logging.DEBUG)
                

              elif signal == 'turn_off_logging':
                logger.setLevel(logging.CRITICAL)


        #reset signal
        if not signal == '':
          signal == '' 
                                  



        #BUG/TODO: Their is a call to render twice....maybe because I call pygame.display.flip more than once?
        screen.update()
        screen.render()
        pygame.display.flip()





if __name__ == '__main__':
  

  #Setup __main__ logger
  logger = logging.getLogger(__name__)  
  logger.info("logging from client.py")

    
  main()


