
from socket import *
import time
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while 1:
    connectionSocket, address = serverSocket.accept()

    message = connectionSocket.recv(1024)
    fileStr = bytes.decode(message)+".txt"
    bytesToSend = open(fileStr, "rb").read()
    connectionSocket.send(bytesToSend)



connectionSocket.close()
