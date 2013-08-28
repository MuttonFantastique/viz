#! /usr/bin/env python

import socket
import sys



#from scapy.all import Ether, IP, TCP, sr1
from scapy.all import *





#creat a tcp/ip socket to listen on
try:
  server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, msg:
  print "Socket Error number: " + msg[0] + "\nError Message: " + msg[1]


#sets some flags(?) in setsockopt
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)




#interface for incoming connections (ip,port)
server_address = ('localhost', 9879)
print 'starting up on %s port %s' % server_address




server.bind(server_address)

server.listen(5)

#connection is a socket object
connection, client_address = server.accept()
print 'connection from ', connection.getpeername()


#clientCommand = connection.recv(4096)

  # if clientCommand:
  #   #
  #   # Process client filter commands 
  #   # will need to refactor this
  #   # after coding multiprocess clients 
  #   # 
  #   pass





connection.shutdown(socket.SHUT_RD | socket.SHUT_WR)
connection.close()


server.close()

def main (*args, **kwargs):
    pass

if __name__ == "__main__":
  main()
  