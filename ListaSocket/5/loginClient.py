import json
from socket import *




HOST = ""
PORT = 1254
DESTINATARIO = (HOST,PORT)

s = socket(AF_INET,SOCK_STREAM)
s.connect(DESTINATARIO)

user = input("Insira o usuário:")
senha = input("Insira ao senha:")
msg = '{ "usuario":'+'"{0}"'.format(user)+',"senha":'+'"{0}"'.format(senha)+'}'
msg= len(msg).to_bytes(2,"big") +msg.encode()
s.send(msg)
msg =s.recv(1024).decode("utf-8")
print(msg)
