from socket import *
HOST = ""
PORT = 5000
s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, end = s.accept()
while True:
    message = conn.recv(2048).decode("utf-8")
    if message == "":
        break
    print(message)