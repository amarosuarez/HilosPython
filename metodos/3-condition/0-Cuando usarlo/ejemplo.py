# 4️⃣ Condition → Sincronización entre hilos

# 📌 Cuándo usarlo:
# 	•	Cuando un hilo debe esperar a que otro realice una acción antes de continuar.
# 	•	Para coordinar productores y consumidores en una cola de datos.

# 🔹 Ejemplo: Un chef (productor) debe cocinar antes de que un cliente (consumidor) pueda comer.
from threading import Thread, Condition
import time

condition = Condition()

def chef():
    with condition:
        print("👨‍🍳 Cocinando comida...")
        time.sleep(2)
        print("✅ Comida lista!")
        condition.notify()  # Despierta al cliente

def cliente():
    with condition:
        print("🙋 Esperando comida...")
        condition.wait()  # Espera a que el chef termine
        print("🍽️ Cliente empieza a comer")

t1 = Thread(target=chef)
t2 = Thread(target=cliente)

t2.start()
time.sleep(1)  # Asegura que el cliente espere primero
t1.start()

t1.join()
t2.join()