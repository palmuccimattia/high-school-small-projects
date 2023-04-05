import subprocess

uscita = subprocess.getoutput("ipconfig").split("\n")

for riga in uscita:
    if "Stato supporto" in riga:
        if "Supporto disconnesso" not in riga:
            print("Connessione ad Internet attiva!")
            break
else:
    print("Il PC non è connesso alla rete!")
        
