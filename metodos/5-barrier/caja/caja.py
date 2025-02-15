from threading import Thread, Barrier
import time, random

class Caja(Thread):
    def __init__(self, nombre, barrera:Barrier):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera

    def run(self):
        self.barrera.wait()
        print("Hilo", self.name, "entra en la caja")
        time.sleep(random.randint(1,3))
        print("Hilo", self.name, "sale de la caja")