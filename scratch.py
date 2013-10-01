
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



###########LOGGING##############

#python <2.6
#disable_existing_loggers=False














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

# interesting Snippet
# import code, traceback, signal

# def debug(sig, frame):
#     """Interrupt running process, and provide a python prompt for
#     interactive debugging."""
#     d={'_frame':frame}         # Allow access to frame object.
#     d.update(frame.f_globals)  # Unless shadowed by global
#     d.update(frame.f_locals)

#     i = code.InteractiveConsole(d)
#     message  = "Signal recieved : entering python shell.\nTraceback:\n"
#     message += ''.join(traceback.format_stack(frame))
#     i.interact(message)

# def listen():
#     signal.signal(signal.SIGUSR1, debug)  # Register handler

#run in site.py so make it execute for every python process









#use a "deck"...
#from collections import deque




 
  # try:
  #   s.setblocking(0)
  # except:
  #   print "why?!"








# try:
#   pygame.init()
#   screen = ColorChangeSquare('root_screen', Rect(200,200,1000,1000))
  
#   print pygame.event.get() 
# except:
#   print 'problem starting screen'

#   # screen.grab = True
# screen.image.fill((0,128,0))



#print "after displayflip()"

#logger.info('hey')





#print 'after event return'
# screen.sub(ColorChangeSquare("square", pygame.Rect((25, 25), (50, 50)), draggable = True))

#these 3 functions do the heavy lifting of getting objects drawn on the screen
# screen.update_SpeedandPosition()
# screen.collision_detection()
# screen.drawParticle()



#
#
#  
#EXAMPLE CODE
#
#
#



# print("creating main screen")
# screen = DropDisplay((400, 300))
# screen.grab = True
# screen.image.fill((0, 128, 0))


# print("square setup")
# screen.sub(ColorChangeSquare("square", pygame.Rect((25, 25), (50, 50)), draggable = True))

# # dropzone setup
# #
# print("drop zone setup")
# screen.sub(DropZone("dropzone", pygame.Rect((100, 100), (200, 100)), draggable = True, grab = True))
# screen.dropzone.image.fill((0, 0, 128))






#GITHUB COMMANDS

#Create a new repository on the command line

# touch README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin https://github.com/TInkeringEngr/dru.git
# git push -u origin master
# Push an existing repository from the command line

# git remote add origin https://github.com/TInkeringEngr/dru.git
# git push -u origin master



#A thing of beauty      

# foo1 = "Hello world"
# foo2 = "bar"
# foo3 = {"1":"a",
#         "2":"b"}
# foo4 = "1+1"

# for name in dir():
#     myvalue = eval(name)
#     print name, "is", type(name), "and is equal to ", myvalue


# Better:

# foo1 = "Hello world"
# foo2 = "bar"
# foo3 = {"1":"a", "2":"b"}
# foo4 = "1+1"

# import pprint
# pprint.pprint(locals())

# {'__builtins__': <module '__builtin__' (built-in)>,
#  '__doc__': None,
#  '__name__': '__main__',
#  'foo1': 'Hello world',
#  'foo2': 'bar',
#  'foo3': {'1': 'a', '2': 'b'},
#  'foo4': '1+1',
#  'pprint': <module 'pprint' from '/usr/lib/python2.5/pprint.pyc'>}