import os
import time

def create_file():
    file = open("./Week 3/file.txt", "a")
    file.write("Dit is geschreven d.m.v de os write functie")
    file.close()

    countdown = 15
    while countdown > 0:
        print("Het bestand wordt over  {} seconden verwijderd.".format(countdown))
        time.sleep(1)
        countdown -= 1

    os.remove("./Week 3/file.txt")
    print("Bestand verwijderd.")

create_file()
