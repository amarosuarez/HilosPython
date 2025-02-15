# 1️⃣ Thread → Ejecutar tareas en paralelo

# 📌 Cuándo usarlo:
# 	•	Cuando necesitas ejecutar tareas concurrentes en segundo plano.
# 	•	Para mejorar la interactividad de una aplicación sin bloquear la interfaz.

# 🔹 Ejemplo: Descargar archivos en paralelo.
from threading import Thread
import time

def descargar(archivo):
    print(f"Iniciando descarga de {archivo}")
    time.sleep(3)  # Simula el tiempo de descarga
    print(f"Descarga de {archivo} completada")

t1 = Thread(target=descargar, args=("video.mp4",))
t2 = Thread(target=descargar, args=("cancion.mp3",))

t1.start()
t2.start()

t1.join()
t2.join()