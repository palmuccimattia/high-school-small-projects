# Client

import socket
import sys

def inviacomandi(s):
    while True:
        comando = input("%>")
        if comando.lower() == "quit":
            print("Sto chiudendo la connessione al Server")
            s.close()
            sys.exit()
        else:
            s.send(comando.encode())
            data = str(s.recv(4096),"utf-8")
            print(data)

            
def conn_server(indirizzo_server):
    try:
        s = socket.socket()
        s.connect(indirizzo_server)
        print(f"Connessione Server {indirizzo_server} stabilita")
    except socket.error as errore:
        print(f"Qualcosa è andato storto, sto uscendo\n{errore}")
        sys.exit()
    inviacomandi(s)

if __name__ == "__main__":
    conn_server(("192.168.1.132",80))
