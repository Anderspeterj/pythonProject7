from socket import *
import requests

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
api_url = "http://localhost:5113/api/ShoppingThing"
headers = {'Content-type': 'application/json'}

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decoded_message = message.decode()
    print("Received: ", message.decode())
    # send data to api
    response = requests.post(api_url, data=message, headers=headers)
    print(response.text)




