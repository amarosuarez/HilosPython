import threading
import time
import random

class Carniceria:
    def __init__(self, num_empleados):
        # El semáforo permite que solo 4 clientes sean atendidos a la vez
        self.semaforo = threading.Semaphore(num_empleados)

    def atender_cliente(self, nombre_cliente):
        with self.semaforo:  # Solo permite que 4 clientes sean atendidos simultáneamente
            print(f"🛒 El cliente {nombre_cliente} está siendo atendido.")
            tiempo_espera = random.randint(1, 10)
            time.sleep(tiempo_espera)  # Simula el tiempo de atención
            print(f"✅ El cliente {nombre_cliente} ha terminado en la carnicería (atendido en {tiempo_espera} segundos).")
