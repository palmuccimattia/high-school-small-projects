import subprocess

data = subprocess.getoutput("netsh wlan show profile").split("\n")
for da in data:
    if "Tutti i profili utente" in da:
        name = da[32:-1]
        profile = subprocess.getoutput('netsh wlan show profile "' + name + '" key=clear').split("\n")
        for pro in profile:
            if "Contenuto chiave" in pro:
                password = pro[34:-1]
                print(name,":",password)
input()