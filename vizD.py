#! /usr/bin/env python

import os
import socket
import sys

#from scapy.all import Ether, IP, TCP, sr1
from scapy.all import *








class Child_Fork():

        # if fork == 0 //child
        # encrypt the connection and data
        # get string command from client that specifies filter
        # create socket and filter for client
        # pre-process data 
        # ship to client

  CONST_msg_length = 50











  def __init__(self, connection, peername):
    self.connection = connection
    self.peername = peername
    self.sendDataToClient()





  def listenForData(self):
    print "called listen for data!"
    message = self.connection.recvfrom(4096)
    if message == 'shutdown':
      closeConnection()
    else:
      return


  def ProcessData(self):
    pass


  def sniffNetwork(self):

      smellyLoad = sniff(iface='eth0', count=10, prn=lambda x: x.show())

      return smellyLoad



  #fixed length implementation
    #TODO: indicator of packet length 
    # This yields two recv's
    # one to get the length of data and a second recv for the full load
  def sendDataToClient(self, msg):

    sent_Data = 0
    while sent_Data < CONST_msg_legth:
      sent = self.connection.send(msg[sent_Data:])

      if sent == o:
        raise RunTimeError("socket connection broken")

      sent_Data = sent_Data + sent 


      # sending = True
      # while(sending):
      #   smellyLoad = self.sniffNetwork()
      #   try:
      #     self.connection.send("Hello Client")
      #   except:
      #     sending = False
      #     print "Client: "+ str(self.peername[0])  + " exited."

      #   #self.listenForData()




  #Fixed length implementation
  def recieveData(self):
    msg = ''
    while len(msg) < CONST_msg_length:
      chunk = self.connection.recv(CONST_msg_length - len(msg))

      if chunk == ""
        raise RunTimeError('socket connection broken')

      msg = msg + chunk 
    return msg


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
    #use this for production & >1000: server.bind((socket.gethostname(), 9879))
    server_address = ('localhost', 9879)
    server.bind(server_address)
    server.listen(3)
    print 'Listening on %s port %s' % server_address



    on = True
    while on:
      try:
        #connection is a socket object
        connection, client_address = server.accept()
        peername =  connection.getpeername()

        print 'connection from ' + str(peername[0])
        if connection:
          process = os.fork()

          if process == 0:
            Child_Fork(connection,peername)
                 
      except KeyboardInterrupt, e:
        print "Shuting Down"
        break

    server.close()


if __name__ == "__main__":
  main()
  