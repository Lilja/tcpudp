__author__ = 'Robin'
from socket import *
import time
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)

    fileStr = "res/"+bytes.decode(message)+".res"
    bytesToSend = open(fileStr, "rb").read()
    serverSocket.sendto(bytesToSend, clientAddress)


