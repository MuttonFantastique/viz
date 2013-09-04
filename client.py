#! /usr/bin/env python
#
# viz-1.0
# GNU
#
#####################


#useful 
import sys
import os


#import pygame environment
import pygame
from pygame.locals import *
from pygame.color import THECOLORS


#usage time.sleep(5.5) //seconds
import time


# program modules #
from userinput import *
from particles import *


# networking
import socket



#How does this python program obtain the path to the other programmed modules? I must explicitily hard code the path?
sys.path.append('/home/blackpanther/Desktop/sdlHacking/working/')











# zZz
def main():

  #give me a few global classes to play with...guess I don't need them
  #global Surface, EventControl, Particle_Container, Window


  #intialize pygame module's
  pygame.init()


  #initate global classes
  EventControl = UserEvents()
  Particle_Container = Particles()

  #a clock to track time between frames
  myclock = pygame.time.Clock()

  #Variables
  framerate_limit = 400 
  time_s = 0.0





#
# Connect to server and get data about network
#
  try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except socket.error, msg:
    print "Socket Error number: " + msg[0] + "\nError Message: " + msg[1]
    sys.exit()



  # ex: s.send('string')

  try:
    s.connect(('localhost', 9879))

    client = True
    #Main Program Loop
    while(client):

        data = s.recv(16) #2^16 or 0xFF bits

        if data:
          print data
          data = 0


        #VerboseComment(VC): myclock.tick() computes how many milliseconds have passed since the last frame
        #followed by a conversion from millisecond into seconds
        dx_s = float(myclock.tick(framerate_limit) * 1e-3)



        #gets user input which returns a string signal if an event is triggered 
        eventReturn = EventControl.pollingInput()
    

        #conditionals for eventReturn sig
        if( eventReturn == 'quit'):
          s.close()
          pygame.exit()
          sys.close()

        elif( eventReturn == 'reload'):
          from particles import *
          Particle_Container = Particles()

        elif eventReturn == 'erase':
          Particle_Container.erase_screen() 

        elif eventReturn == 'shutdown':
          s.send('shutdown')

        

        #these 3 functions do the heavy lifting of getting objects drawn on the screen
        Particle_Container.update_SpeedandPosition()
        Particle_Container.collision_detection()
        Particle_Container.drawParticle()


        #time since initialization
        time_s += dx_s


        #update the screen
        pygame.display.flip()
     


  except: #exits if no connection made
    "exception raised..."


if __name__ == '__main__':
  main()


