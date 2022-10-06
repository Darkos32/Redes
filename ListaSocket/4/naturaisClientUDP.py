from socket import *
HOST = ""
PORT = 5000
DESTINATARIO = (HOST,PORT)
s = socket(AF_INET, SOCK_DGRAM)

n = int(input("Valor de N: "))
for i in range(1, n+1):
    s.sendto((str(i) +"\n").encode(),DESTINATARIO)
