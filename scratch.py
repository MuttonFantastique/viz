
#########profileing#######

# import cProfile
# cProfile.run('foo()')

#timer code snippet

# import timeit
# timeit.Timer('for i in xrange(10): oct(i)').timeit()

# from timeit import Timer
# t = Timer('func()','from foo import func')
# t.repeat, t.timeit()




########errors########

  # try:

  # except:
  #   (type, value, tb) = sys.exc_info()
  #    print "%s" % value.message




####pycallgraph####


# import pycallgraph
# pycallgraph.start_trace()

# pycallgraph.make_dot_graph('test.png')

####Turn off *.pyc if your untrusting 
#sys.dont_write_bytecode = True


















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

# except Exception,e:
#   print str(e)


# >>> class MyError(Exception):
# ...     def __init__(self, value):
# ...         self.value = value
# ...     def __str__(self):
# ...         return repr(self.value)
# ...
# >>> try:
# ...     raise MyError(2*2)
# ... except MyError as e:
# ...     print 'My exception occurred, value:', e.value
# ...
# My exception occurred, value: 4
# >>> raise MyError('oops!')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# __main__.MyError: 'oops!'

                  


# class Window:
#   def __init__(self):
#     surface = self.surface = pygame.display.set_mode((0,0), pygame.RESIZABLE)
#     second_surface = pygame.display.set_mode((0,0), pygame.RESIZABLE)
#     background = self.background = pygame.Surface(surface.get_size())
#     background.convert()
  

#  import pip
#   from subprocess import call

# for dist in pip.get_installed_distributions():
#   call("pip install --upgrade " + dist.project_name, shell=True)




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




# Add current and parent directory. One of them is supposed to contain the
# planes package.
#
  # sys.path.append("../")
  # sys.path.append("./")




  # assert – base assert allowing you to write your own assertions
  # assertEqual(a, b) – check a and b are equal
  # assertNotEqual(a, b) – check a and b are not equal
  # assertIn(a, b) – check that a is in the item b
  # assertNotIn(a, b) – check that a is not in the item b
  # assertFalse(a) – check that the value of a is False
  # assertTrue(a) – check the value of a is True
  # assertIsInstance(a, TYPE) – check that a is of type “TYPE”
  # assertRaises(ERROR, a, args) – check that when a is called with args that it raises ERROR

