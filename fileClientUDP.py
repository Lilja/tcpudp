# fileClientUDP.py
__author__ = 'William'

from socket import *
import sys

# Set server ip and port
serverName = sys.argv[1]
serverPort = 12000
# Set file to request (choose from: 100, 1000, 10000, 100000, 1000000, 10000000, 100000000)
fileToRequest = sys.argv[2]

# Create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Send file request to server
clientSocket.sendto(str.encode(fileToRequest), (serverName, serverPort))
# Recieve requested file from server
recievedFile, serverAddress = clientSocket.recvfrom(int(fileToRequest))

# Print results
print(recievedFile)
print("Length (B): "+str(len(recievedFile)))

# Save file to disk
open(fileToRequest+".txt", "wb").write(recievedFile)


# Close socket
clientSocket.close()
