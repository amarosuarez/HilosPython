# 3️⃣ Semaphore → Controlar acceso a recursos limitados

# 📌 Cuándo usarlo:
# 	•	Cuando un recurso tiene un número limitado de accesos simultáneos.
# 	•	Para limitar la cantidad de hilos que pueden ejecutar una tarea a la vez.

# 🔹 Ejemplo: Solo 3 cajeros disponibles en un banco, pero más clientes esperando.
from threading import Thread, Semaphore
import time

semaforo = Semaphore(3)  # Máximo 3 hilos a la vez

def usar_cajero(nombre):
    with semaforo:
        print(f"{nombre} está usando el cajero...")
        time.sleep(2)  # Simula el uso del cajero
        print(f"{nombre} ha terminado.")

clientes = ["Ana", "Luis", "Carlos", "Eva", "Pedro"]
hilos = [Thread(target=usar_cajero, args=(c,)) for c in clientes]

for h in hilos:
    h.start()

for h in hilos:
    h.join()