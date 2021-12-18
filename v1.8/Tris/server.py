from array import array
import socket
from _thread import *
from game import Menu

PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.2.56", PORT))
s.listen(5)

def receive(conn):
    global quadranti_server
    quadranti_server = []
    while True:
        # provo a ricevere il turno
        try:
            turno = conn.recv(1024).decode("utf-8")
        # se non sono riuscito a ricevere il turno
        except:
            pass

        # se il turno è quello delle x
        if turno == "0":
            # prova a inviare il comando di disegnare le x nel quadrante selezionato
            try:
                conn.send(bytes("disegnax", "utf-8"))
            # se non sono riuscito a inviare il comando di disegnare le x nel quadrante selezionato
            except:
                pass
        # se il turno è quello delle o
        elif turno == "1":
            # prova a inviare il comando di disegnare le o nel quadrante selezionato
            try:
                conn.send(bytes("disegnao", "utf-8"))
            # se non sono riuscito a inviare il comando di disegnare le o nel quadrante selezionato
            except:
                pass
        
        # provo a ricevere le coordinate del quadrante selezionato
        #try:
        #    coordinate_quadrato_str = conn.recv(1024).decode("utf-8")
        #    coordinate_quadrato = tuple(coordinate_quadrato_str.split(","))
        # se non sono riuscito a ricevere le coordinate del quadrante selezionato
        #except:
        #    pass

        # provo a ricevere lo stato dei quadranti
        try:
            quadranti_str = conn.recv(1024).decode("utf-8")
            quadranti = tuple(quadranti_str.split(","))
        # se non sono riuscito a ricevere le coordinate del quadrante selezionato
        except:
            pass

        for i in range(0, len(quadranti)):
            if quadranti[i] == "False":
                if i+1 not in quadranti_server:
                    quadranti_server.append(i+1)
                    #if turno == "0":
                    #    turno = 1
                    #elif turno == "1":
                    #    turno = 0
            
        if len(quadranti_server) != 0:
            print(str(quadranti_server))
            try:
                conn.send(bytes(f"{quadranti_server}", "utf-8"))
            except:
                pass
                
        #try:
        #conn.send(bytes(f"{turno}", "utf-8"))
        print(turno)
        #except:
        #    pass

clientsNumber = 0
while True:
    if clientsNumber < 2:
        conn, addr = s.accept()
        print(f"Connection from {addr} has been estabilished!")
        clientsNumber += 1
        conn.send(bytes(f"GIOCATORE {clientsNumber}", "utf-8"))

        start_new_thread(receive, (conn,))