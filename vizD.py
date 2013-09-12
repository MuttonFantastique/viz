#! /usr/bin/env python

import os
import socket
import sys

#from scapy.all import Ether, IP, TCP, sr1
from scapy.all import *


#remove for production#
sys.dont_write_bytecode = True




    #TODO:
        # if fork == 0 //child
        # encrypt the connection and data
        # get string command from client that specifies filter
        # create socket and filter for client
        # pre-process data 
        # ship to client
class Child_Fork():
  MSG_LENGTH = 50


  def __init__(self, connection, peername):
    self.connection = connection
    self.peername = peername




    #Soon...
    #self.sendDataToClient()






  #TODO: indicator of packet length 
  # This mandates connection.recv x2
  # one to get the length and the second recv for the full payload

  #fixed length implementation
  def sendDataToClient(self, msg):

    sent_Data = 0
    while sent_Data < CONST_msg_legth:
      sent = self.connection.send(msg[sent_Data:])

      if sent == o:
        raise RunTimeError("socket connection broken")

      sent_Data = sent_Data + sent 



  #Fixed length implementation
  def recieveData(self):
    msg = ''
    while len(msg) < MSG_LENGTH:
      chunk = self.connection.recv(MSG_LENGTH - len(msg))

      if chunk == "":
        raise RunTimeError('socket connection broken')

      msg = msg + chunk 
    return msg





  def listenForData(self):
    print "called listen for data!"
    message = self.connection.recvfrom(4096)
    if message == 'shutdown':
      closeConnection()
    else:
      return


  def sniffNetwork(self, filter):

      smellyLoad = sniff(iface='eth0', count=10, prn=lambda x: x.show())

      return smellyLoad

  
  
  def ProcessData(self):
    pass

  def closeConnection(self):
    self.connection.shutdown(socket.SHUT_RD | socket.SHUT_WR)
    self.connection.close()
   






def main (*args, **kwargs):


    #creat a tcp/ip socket to listen on
    try:
      server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
      print "Socket Error number: " + msg[0] + "\nError Message: " + msg[1]


    #sets address re-use flag in setsockopt
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


 
    #interface for incoming connections (ip,port)
    server_address = ('localhost', 9879)
    server.bind(server_address)

    #hardcoded to listen for 5 clients
    server.listen(5)
    print 'Listening on %s port %s' % server_address



    on = True
    while on:
      try:
        #connection is a socket object
        connection, client_address = server.accept()
        peername =  connection.getpeername()

        print 'connection from ' + str(peername[0])
        if connection:

          #process == 0 is child, else is parent process
          process = os.fork()

          if process == 0: 
            Child_Fork(connection,peername)
                 
      except KeyboardInterrupt, e:
        print "Shuting Down"
        break

    server.close()


if __name__ == "__main__":
  main()
  