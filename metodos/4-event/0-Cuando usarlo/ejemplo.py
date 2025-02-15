# 5️⃣ Event → Señalización entre hilos

# 📌 Cuándo usarlo:
# 	•	Cuando un hilo debe esperar hasta que otro le envíe una señal.
# 	•	Para iniciar o detener tareas cuando se active una condición.

# 🔹 Ejemplo: Un semáforo que indica cuándo los coches pueden avanzar.
from threading import Thread, Event
import time

event = Event()

def coche(nombre):
    print(f"🚗 {nombre} esperando luz verde...")
    event.wait()  # Espera hasta que el semáforo se active
    print(f"🚦 {nombre} arranca!")

def semaforo():
    time.sleep(3)
    print("🟢 Semáforo en verde!")
    event.set()  # Los coches pueden avanzar

t1 = Thread(target=coche, args=("Toyota",))
t2 = Thread(target=coche, args=("Ford",))
t3 = Thread(target=semaforo)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()