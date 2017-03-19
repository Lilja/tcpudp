# streamClientTCP.py
__author__ = 'William'

import json
from socket import *
import sys

# Set server ip and port
serverName = sys.argv[1]
serverPort = 12000
# Set request message to send
messageSizeInBytes = int(sys.argv[2])

# Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to socket
clientSocket.connect((serverName, serverPort))

secondsBetweenTransfers = 0.01
nrOfTransfers = 10000
sendInfo = (messageSizeInBytes, secondsBetweenTransfers, nrOfTransfers)
dataString = json.dumps(sendInfo)

# Print request message
print(dataString)

# Encode message
clientSocket.send(str.encode(dataString))

# Recieve set amount of transfers
for x in range(1, nrOfTransfers+1):
   print("Transfer nr: "+str(x))

   # Recieve transfer
   recievedData = clientSocket.recv(messageSizeInBytes)
   # Print length of transferred data
   print("Length (B): "+str(len(recievedData))+"\n")


# Close socket
clientSocket.close()
