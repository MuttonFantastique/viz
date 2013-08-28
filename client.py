#!/usr/bin/env python
#
# viz-1.0
# GNU
#
#####################

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



import socket


sys.path.append('/home/blackpanther/Desktop/sdlHacking/working/')




# zZz
def main():

  #give me a few global classes to play with
  global Surface, EventControl, Particle_Container, Window

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


  print "about to connect"
  try:
    s.connect(('localhost', 9879))
  except socket.error, msg:
  print "Socket Error number: " + msg[0] + "\nError Message: " + msg[1]

  #s.send('string')

  
  

  on = True
  
  #Program Loop
  while(True):
    print "Entering program loop"

    print "pulling data"
    data = s.recv(6500)

    #myclock.tick() computes how many milliseconds have passed the last frame
    #converted into seconds
    dx_s = float(myclock.tick(framerate_limit) * 1e-3)

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

    

    #these 3 functions do the heavy lifting
    Particle_Container.update_SpeedandPosition()
    Particle_Container.collision_detection()
    Particle_Container.drawParticle()


    #time since initialization
    time_s += dx_s


    #update the screen
    pygame.display.flip()



main()


