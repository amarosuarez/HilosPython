# 5 hilos escriben cada uno una vocal en un archivo de texto.
# Se usa un Lock para evitar que los hilos escriban simultáneamente y corrompan el archivo.


from threading import Thread, Lock
import time

class Escritor(Thread):
    def __init__(self, vocal, lock):
        Thread.__init__(self)
        self.vocal = vocal
        self.lock = lock

    def run(self):
        for _ in range(5):
            with self.lock:  # Bloquea el acceso al archivo para un solo hilo a la vez
                with open("vocales.txt", "a") as f:
                    f.write(self.vocal + "\n")
            time.sleep(0.1)  # Simula un pequeño retraso

if __name__ == "__main__":
    vocales = ["A", "E", "I", "O", "U"]
    lock = Lock()
    hilos = [Escritor(vocal, lock) for vocal in vocales]

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("Escritura finalizada. Revisa vocales.txt")