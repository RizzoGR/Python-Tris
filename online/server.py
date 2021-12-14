import socket
import threading   

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNESSIONE = 'Disconnesso!'
HEADER = 64

server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def gestione_client(conn, addr):
  print(f"Nuova connessione, {addr} connesso.")

  connesso = True
  while connesso:
    msg_lunghezza = conn.recv(HEADER).decode(FORMAT) 
    if msg_lunghezza:   
      msg_lunghezza = int(msg_lunghezza)
      msg = conn.recv(msg_lunghezza).decode(FORMAT)
      print(f"[{addr}] {msg}")
      if msg == DISCONNESSIONE:
        connected = False 
  conn.close()

    
def start():
  server.listen()
  print(f"[ASCOLTANDO] Il server sta attendendo su {SERVER}")
  while True: 
    conn, addr = server.accept()
    thread = threading.Thread(target=gestione_client, args=(conn, addr))
    thread.start()
    print(f"Thread attivi {threading.activeCount() - 1}")

print("Avvio Server ...")
start()

