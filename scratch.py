
# except:
#   print "global exception"
#   e = sys.exc_info()
#   print e[0]
#   print e[1]

# except:
#    print "local exception"
#    e = sys.exc_info()
#    print e[0]
#    print e[1]
                  


# class Window:
#   def __init__(self):
#     surface = self.surface = pygame.display.set_mode((0,0), pygame.RESIZABLE)
#     second_surface = pygame.display.set_mode((0,0), pygame.RESIZABLE)
#     background = self.background = pygame.Surface(surface.get_size())
#     background.convert()
  

     import pip
      from subprocess import call

    for dist in pip.get_installed_distributions():
      call("pip install --upgrade " + dist.project_name, shell=True)




#   # #need to get the pointer to the surface
#  drawing_surface = pygame.display.get_surface()
#  drawing_surface.fill((0,0,150))


# for widget in range(100):
#   xPos += 10
#   yPos += 10
#   pygame.draw.circle(Surface.surface, [0,0,100], (xPos,yPos), 50) 


#pygame.display.flip()



# try:
#    data = s.recv(16) #2^16 or 0xFF bits
# except:
#    print "moving on"

# if data:
#    print data
#    data = 0

# ex: s.send('string')




# sending = True
# while(sending):
#   smellyLoad = self.sniffNetwork()
#   try:
#     self.connection.send("Hello Client")
#   except:
#     sending = False
#     print "Client: "+ str(self.peername[0])  + " exited."

#   #self.listenForData()


#use for remote server.bind((socket.gethostname(), 9879))


# try:
#   s.setblocking(0)
# except:
#   print "why?!"


##### Check user input example
#if not isinstance( <instance>, <instance>):
# raise ValueError() //use raise to throw exception