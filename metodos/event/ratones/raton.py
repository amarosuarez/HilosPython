from threading import Thread, Event
import random
import time

class Raton(Thread):
    def __init__(self, nombre, event:Event):
        Thread.__init__(self, name=nombre)
        self.evento = event

    def run(self):
        # El ratón espera a que el plato esté libre
        while not self.evento.is_set():
            self.evento.wait()

        # Cogemos el plato y lo marcamos como que está siendo utilizado
        self.evento.clear() # Lo marca como False (No está libre)
        print("El ratón", self.name, "ha cogido el plato")
        time.sleep(random.randint(1, 3))
        print("El ratón", self.name, "ha terminado de comer")

        # Marcamos el plato como libre
        self.evento.set()