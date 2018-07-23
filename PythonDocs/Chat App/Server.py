import socket
import sys
import time
## end of import##
##init##
s = socket.socket()
host = socket.gethostname()
print(" Server will start on host:" , host)
port=8080

s.bind((host,port))
print("")
print(" Server done binding to host and port successfully")
print("")
print("Server is waiting for connection") 
s.listen(1)
connect,addr,name=s.accept()
print(name,"From ",addr,"has connected to the server and is now online...")
print("")
while 1:
        message = "Hello ",name,", welcome to lando chatting system. How can I help you?"
        message = message.encode()
        connect.send(message)
        print("message has been sent")
        print("")
        incoming_message = connect.recv(1024)
        incoming_message = incoming_message.decode()
        print(" Client says: ",incoming_message)
        print("")



