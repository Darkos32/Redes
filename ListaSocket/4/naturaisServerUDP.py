
from socket import *
HOST  = ""
PORT = 5000
s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))
while True:
    message,_ = s.recvfrom(2048)
    message=  message.decode("utf-8")
    if message =="":
        break
    print(message)