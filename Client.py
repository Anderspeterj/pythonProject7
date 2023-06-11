from socket import *
from time import sleep
import random
import json

# udp client broadcast

serverName = "255.255.255.255"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    #send data
    Id = random.randint(1, 100)
    Name = "television"
    Price = random.randint(1, 100)
    Quantity = random.randint(1, 100)

    webcam_data = {
        "Id": Id,
        "Name": Name,
        "Price": Price,
        "Quantity": Quantity
    }
    json_data = json.dumps(webcam_data)
    clientSocket.sendto(json_data.encode(), (serverName, serverPort))
    print("Sent: ", json_data)
    sleep(1)
clientSocket.close()


