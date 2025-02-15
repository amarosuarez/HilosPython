from threading import Thread, Event
import time

class Empresa(Thread):
    evento = Event()
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print("LA EMPRESA", self.name, "INCIA LA VENTA")
        self.evento.set()

        time.sleep(2)
        print("LA EMPRESA", self.name, "CIERRA LA VENTA")
        self.evento.clear()

