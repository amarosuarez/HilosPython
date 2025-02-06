import random
from threading import Semaphore, Thread
import time

class Trabajador(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            print(f"Soy {self.name} y estoy trabajando")
            time.sleep(random.randint(1, 3))
            print(f"Soy {self.name} y he terminado de trabajar")