import socket
from _thread import *

PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("172.20.10.6", PORT))
s.listen(5)

def threaded_client(conn, clientsNumber):
    while True:
        try:
            informazioni = conn.recv(1024)
            quadratox = informazioni[0].decode("utf-8")
            quadratoy = informazioni[1].decode("utf-8")
            disegno = informazioni[2].decode("utf-8")
            
            print(quadratox, quadratoym, disegno)

            if not msg:
                print("Disconnected")
                clientsNumber -= 1
                return clientsNumber
            else:
                print(dmsg)
        except:
            print("Disconnected")
            clientsNumber -= 1
            return clientsNumber

clientsNumber = 0
while True:
    if clientsNumber <2:
        conn, addr = s.accept()
        print(f"Connection from {addr} has been estabilished!")
        clientsNumber += 1
        conn.send(bytes(f"GIOCATORE {clientsNumber}", "utf-8"))
        start_new_thread(threaded_client, (conn,clientsNumber))