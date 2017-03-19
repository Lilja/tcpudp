__author__ = 'Robin'
import json
import os
from socket import *
import time
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while 1:
    connectionSocket, address = serverSocket.accept()

    message = connectionSocket.recv(1024)

    dataLoaded = json.loads(bytes.decode(message))


    messageSizeInBytes, secondsBetweenTransfers, nrOfTransfers = dataLoaded

    for x in range(1, nrOfTransfers+1):
        randString = os.urandom(messageSizeInBytes)
        connectionSocket.sendto(randString, address)
        time.sleep(secondsBetweenTransfers)



connectionSocket.close()
