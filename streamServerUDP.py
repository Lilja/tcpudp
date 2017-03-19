__author__ = 'Robin'
from socket import *
import time
import json
import os

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    dataLoaded = json.loads(bytes.decode(message))
    messageSizeInBytes, secondsBetweenTransfers, nrOfTransfers = dataLoaded

    for x in range(1, nrOfTransfers+1):
        randString = os.urandom(messageSizeInBytes)
        serverSocket.sendto(randString, clientAddress)
        time.sleep(secondsBetweenTransfers)

