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
from particles import *

# networking
import socket

#implicit import pycallgraph

#Still necessary?
#TODO: setup.py
sys.path.append('/home/blackpanther/Desktop/sdlHacking/working/')


# zZz
def main():


  #Major Classes
  EventControl = UserEvents()
  #Gui_Env = GUI((400,400), fullscreen = False)
  Gui_Env = GUI((0,0))
  Gui_Env.grab = True
  Gui_Env.image.fill((0,128,0))



  #Variables


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

      # try:
      #   s.setblocking(0)
      # except:
      #   print "why?!"



    client = True
    #Main Program Loop
    while(client):

        #gets user input which returns a string signal for triggered events 
        eventReturn = EventControl.pollingInput()
        
    
        if( eventReturn == 'quit'):
          s.close()
          pygame.exit()
          sys.close()

        elif( eventReturn == 'reload'):
            
            from particles import *
            Gui_Env = GUI((0,0))
            Gui_Env.grab = True
            Gui_Env.image.fill((0, 128, 0))
          
          

        elif eventReturn == 'erase':
          Gui_Env.erase_screen() 



        #TEMPLATE TO SEND COMMANDS TO SERVER
        #TODO:  
        elif eventReturn == 'shutdown':
          s.send('shutdown')



        elif eventReturn == 'sample':
            import pycallgraph
            pycallgraph.start_trace()

              # TODO:
              # import cProfile
              # cProfile.run('foo()')


        elif eventReturn == 'stopsample':
          pycallgraph.make_dot_graph('images/sample.png')


        Gui_Env.sub(ColorChangeSquare("square", pygame.Rect((25, 25), (50, 50)), draggable = True))
        Gui_Env.update()
        Gui_Env.render()

        pygame.display.flip()

  

        #these 3 functions do the heavy lifting of getting objects drawn on the screen
        Gui_Env.update_SpeedandPosition()
        Gui_Env.collision_detection()
        Gui_Env.drawParticle()



        


  except: #exits if no connection made
    "exception raised trying to connect"


if __name__ == '__main__':
  main()


