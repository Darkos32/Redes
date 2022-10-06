
from socket import *
import threading
HOST =""
PORT = 12000
RECV_SIZE = 2048
s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))
def handleRequest(message, end):
    message = message.decode("utf-8").upper()
    s.sendto(message.encode(),end)
def main():
    print("Server UP")
    while True:
        pedido = threading.Thread(target=handleRequest,args=s.recvfrom(RECV_SIZE))
        pedido.start()
if __name__ == "__main__":
    main()

