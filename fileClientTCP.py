# fileClientTCP.py
__author__ = 'William'

from socket import *
import sys

# Set server ip and port
serverName = sys.argv[1]
serverPort = 12000
# Set file to request (choose from: 100, 1000, 10000, 100000, 1000000, 10000000, 100000000)
fileToRequest = sys.argv[2]

print("Ip: " + serverName + " port " + str(serverPort) + " file: " + fileToRequest)

# Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to socket
clientSocket.connect((serverName, serverPort))


# Send file request to server
clientSocket.send(str.encode(fileToRequest))
# Recieve requested file from server
recievedFile = clientSocket.recv(int(fileToRequest))

# Print results
print(recievedFile)
print("Length (B): "+str(len(recievedFile)))

# Save file to disk
open(fileToRequest+".txt", "wb").write(recievedFile)


# Close socket
clientSocket.close()
