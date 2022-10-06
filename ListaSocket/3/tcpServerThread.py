from socket import *
import threading
RECEIV_SIZE = 1024
HOST = ""
PORT = 12000
def init_socket():
    s = socket(AF_INET,SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    print("Server UP!")
    return s
def handleRequest(connect, end):
    frase = connect.recv(RECEIV_SIZE).decode("utf-8")
    frase = frase.upper()
    connect.send(str.encode(frase))
    connect.close()

def main():
    s= init_socket()
    while True:
        pedido = threading.Thread(target=handleRequest,args=s.accept())
        pedido.start()

if __name__ == "__main__":
    main()

