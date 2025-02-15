# 6️⃣ Barrier → Sincronizar múltiples hilos

# 📌 Cuándo usarlo:
# 	•	Cuando varios hilos deben esperar hasta que todos estén listos antes de continuar.
# 	•	Para fases de ejecución en paralelo.

# 🔹 Ejemplo: Un equipo de corredores espera hasta que todos estén listos antes de comenzar.
from threading import Thread, Barrier
import time
import random

barrier = Barrier(3)  # Espera a que 3 corredores estén listos

def corredor(nombre):
    time.sleep(random.randint(1, 3))  # Simula preparación
    print(f"🏃 {nombre} está listo en la línea de salida")
    barrier.wait()  # Espera a los otros corredores
    print(f"🚀 {nombre} comienza a correr!")

nombres = ["Usain", "Bolt", "Mo Farah"]
hilos = [Thread(target=corredor, args=(n,)) for n in nombres]

for h in hilos:
    h.start()

for h in hilos:
    h.join()