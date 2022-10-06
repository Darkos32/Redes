from socket import *
HOST = ""
PORT = 5000

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
n =int( input("Valor de N: "))
for i in range(1, n+1):
    s.send((str(i) + "\n").encode())