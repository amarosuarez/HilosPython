import threading
from panaderia import Panaderia

class Comprador(threading.Thread):
    def __init__(self, num, panaderia):
        threading.Thread.__init__(self, name=num)
        self.num = num
        self.panaderia = panaderia

    def run(self):
        print(f"Soy el cliente {self.num}")
        if (self.panaderia.compra_pan()):
            print(f'Cliente {self.num}, ha comprado pan')