import random
from threading import Semaphore, Thread
import time

class Parking(Thread):
    semaforo = Semaphore(5)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.name = nombre

    def run(self):
        print("🚗 Vehículo", self.name, "está entrando al estacionamiento")
        Parking.semaforo.acquire()

        print("🚗 Vehículo", self.name, "aparcado")
        time.sleep(random.randint(1,10))
        
        Parking.semaforo.release()
        print("Vehículo", self.name, "salió del estacionamiento 🚗. Espacios disponibles:", Parking.semaforo._value)