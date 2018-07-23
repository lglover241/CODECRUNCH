import socket
import time
import sys
s=socket.socket()
name = input(str("Enter your name: "))
host = input(str("Enter hostname of the server: "))
port = 8080
s.connect((host,port))
print(" Connected to server")
s.send(name)

while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print(incoming_message)
        print("")
        message = input(str(">>"))
        message = message.encode()
        s.send(message)
        print("message has been sent")
        print("")

