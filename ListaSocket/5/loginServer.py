import json
from socket import *
import threading
HOST = ""
PORT = 1254
DESTINATARIO = (HOST, PORT)

base = {"darkos": "12345"}


def init_socket():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(DESTINATARIO)
    s.listen(1)
    return s


def handleRequest(conn, end):
    msg = conn.recv(2)
    tam = int.from_bytes(msg[0:2],"big")
    msg = conn.recv(tam)
    msg =json.loads(msg)
    if msg["usuario"] in base and msg["senha"]==base[msg["usuario"]]:
        msg = "Sucesso"
    else:
        msg = "fracasso"
    conn.send(msg.encode())


def main():
    s= init_socket()
    while True:
        pedido = threading.Thread(target=handleRequest, args=s.accept())
        pedido.start()


if __name__ == "__main__":
    main()
