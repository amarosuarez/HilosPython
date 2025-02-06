import random
from threading import Barrier, Thread
import time

class Caja(Thread):
    def __init__(self, nombre, barrera: Barrier):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera

    def run(self):
        resto = self.barrera.wait()
        print("Hilo", self.name, "entra en caja y quedan", resto)
        time.sleep(random.randint(1, 3))
        print("Hilo", self.name, "sale de caja")
