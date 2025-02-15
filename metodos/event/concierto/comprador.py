from threading import Thread
import time, random

class Comprador(Thread):
    def __init__(self, nombre, empresa):
        Thread.__init__(self, name=nombre)
        self.empresa = empresa
    
    def run(self):
        print(self.name, "entra a la web")

        if self.empresa.evento.is_set():
            print("¡La venta está abierta!", self.name, "está comprando...")
            time.sleep(random.randint(1, 5))
            print(self.name, "ha terminado de comprar")
        else:
            print("La venta está cerrada...")