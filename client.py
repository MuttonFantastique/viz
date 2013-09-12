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

#implicit import pycallgraph

#use a "deck"...
#from collections import deque




#remove for production#
sys.dont_write_bytecode = True



#Still necessary?
#TODO: setup.py
sys.path.append('/home/blackpanther/Desktop/sdlHacking/working/')

















# zZz
def main():

  

  
  #Major Classes
  EventControl = UserEvents()




  #single change dropdisplay to (0,0) and everything breaks
  #check to see how the resolution tuple is used and what its breaking

  screen = DropDisplay()
  screen.image.fill((0,128,0))








                                                # try:
                                                #   pygame.init()
                                                #   screen = ColorChangeSquare('root_screen', Rect(200,200,1000,1000))
                                                  
                                                #   print pygame.event.get() 
                                                # except:
                                                #   print 'problem starting screen'

                                                #   # screen.grab = True
                                               # screen.image.fill((0,128,0))



 

#TODO
#disabled try/except block due to the masking of unrelated exceptions...need to modify except to print all exceptions
  #
  # Connect to server
  #
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except socket.error, msg:
    print "Socket Error number: " + msg[0] + "\nError Message: " + msg[1]
    sys.exit()



  try:
    s.connect(('localhost', 9879))
  except: 
    print "exception raised trying to connect"

  # try:
  #   s.setblocking(0)
  # except:
  #   print "why?!"


  #Variables
  message = ''

  client = True
  #Main Program Loop
  while(client):
        #print "got into the loop"


        #gets user input which returns a string signal for triggered events 
        
        events = pygame.event.get()
        #print "after pygame.event.get()"

        #print events


        if events:
          message, event = EventControl.pollingInput(events)
        
       
    
        if( message == 'quit'):
          s.close()
          pygame.exit()
          sys.close()

        elif( message == 'reload'):
            
              from gui import *
              screen = DropDisplay()        
          

        elif message == 'erase':
          screen.erase_screen() 


        #TEMPLATE TO SEND COMMANDS TO SERVER
        #TODO:  
        elif message == 'shutdown':
          s.send('shutdown')



        elif message == 'sample':
            import pycallgraph
            pycallgraph.start_trace()
                  #TODO: stop_trace()?


                # TODO:
                # import cProfile
                # cProfile.run('foo()')


        elif message == 'stopsample':
          pycallgraph.make_dot_graph('images/sample.png')

        elif message == 'mouseevent':
          screen.process(event)






        #print 'after event return'
          # screen.sub(ColorChangeSquare("square", pygame.Rect((25, 25), (50, 50)), draggable = True))
         

        #print "before screen update and render"
        screen.update()
        screen.render()
        pygame.display.flip()
        #print "after displayflip()"
      
  

        #these 3 functions do the heavy lifting of getting objects drawn on the screen
          # screen.update_SpeedandPosition()
          # screen.collision_detection()
          # screen.drawParticle()



        


  


if __name__ == '__main__':
  main()


