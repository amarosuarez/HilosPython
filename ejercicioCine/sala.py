import random
from threading import Semaphore, Thread
import time

class Sala(Thread):
    semaforo = Semaphore(20)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.name = nombre

    def run(self):
        print("Espectador", self.name, "esperando...")
        Sala.semaforo.acquire()

        print("Espectador", self.name, "entra en la sala")
        time.sleep(5)

        Sala.semaforo.release()
        print("Espectador", self.name, "sale de la sala")

        # if (Sala.semaforo._value == 20):
        #     time.sleep(random.randint(1,10))