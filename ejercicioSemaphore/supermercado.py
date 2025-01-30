import random
from threading import Semaphore, Thread
import time

class Supermercado(Thread):
    # Creamos semáforo con un valor de 4
    # Se podrá ejecutar un código de forma simultánea por 4 hilos a la vez
    semaforo = Semaphore(4)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        # Simulamos el acceso a las cajas de un supermercado
        print("Hilo", self.name, "va a una caja")
        Supermercado.semaforo.acquire()
        print("Hilo", self.name, "está siendo atendido")
        
        # Cada cliente es atendido un tiempo distinto
        time.sleep(random.randint(1,10))
        print("Hilo", self.name, "está pagando")
        Supermercado.semaforo.release()
        print("Hilo", self.name, "abandona el supermercado")