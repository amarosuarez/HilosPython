import random
from threading import Semaphore, Thread
import time

class Banco(Thread):
    semaforo = Semaphore(3)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
    
    def run(self):
        print("Cliente", self.name, "esperando...")
        Banco.semaforo.acquire()

        print("Cliente", self.name, "usando el cajero")
        time.sleep(random.randint(1,5))

        Banco.semaforo.release()
        print("Cliente", self.name, "abandona el cajero. Cajeros libres:", Banco.semaforo._value)