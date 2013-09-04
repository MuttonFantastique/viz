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
from pygame.locals import *
from pygame.color import THECOLORS

#usage time.sleep(5.5) //seconds
import time

# brother/sister modules 
from userinput import *
from particles import *

# networking
import socket


#Still necessary?
#TODO: setup.py
sys.path.append('/home/blackpanther/Desktop/sdlHacking/working/')


# zZz
def main():


  #Major Classes
  EventControl = UserEvents()
  Particle_Container = Particles()



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
          Particle_Container = Particles()

        elif eventReturn == 'erase':
          Particle_Container.erase_screen() 



        #TEMPLATE TO SEND COMMANDS TO SERVER
        #TODO:  
        elif eventReturn == 'shutdown':
          s.send('shutdown')

        

        #these 3 functions do the heavy lifting of getting objects drawn on the screen
        Particle_Container.update_SpeedandPosition()
        Particle_Container.collision_detection()
        Particle_Container.drawParticle()


        


  except: #exits if no connection made
    "exception raised trying to connect"


if __name__ == '__main__':
  main()


