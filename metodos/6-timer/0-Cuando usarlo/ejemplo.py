# 7️⃣ Timer Thread → Ejecutar código tras un tiempo

# 📌 Cuándo usarlo:
# 	•	Cuando una acción debe ejecutarse después de un tiempo determinado sin bloquear el código principal.
# 	•	Para notificaciones, recordatorios o tareas retrasadas.

# 🔹 Ejemplo: Un temporizador para apagar la música después de 10 segundos.
from threading import Timer

def apagar_musica():
    print("⏰ La música se ha apagado.")

t = Timer(10, apagar_musica)  # Ejecuta la función en 10 segundos
t.start()

print("🎵 La música está sonando...")