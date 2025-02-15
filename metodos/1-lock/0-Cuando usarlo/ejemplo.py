# 2️⃣ Lock → Evitar condiciones de carrera

# 📌 Cuándo usarlo:
# 	•	Cuando varios hilos acceden y modifican una misma variable o recurso compartido.
# 	•	Para evitar corrupción de datos.

# 🔹 Ejemplo: Simular una cuenta bancaria con varios hilos accediendo.
from threading import Thread, Lock

saldo = 100
lock = Lock()

def retirar_dinero(monto):
    global saldo
    with lock:  # Bloquea la sección crítica
        if saldo >= monto:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {saldo}")
        else:
            print("Fondos insuficientes")

t1 = Thread(target=retirar_dinero, args=(50,))
t2 = Thread(target=retirar_dinero, args=(70,))

t1.start()
t2.start()
t1.join()
t2.join()