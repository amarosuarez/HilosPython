import random
from threading import Lock, Thread

class BloqueaLista(Thread):
    lista = [False, False, False, False, False]
    bloqueo = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print("Hilo", self.name, "ejecutándose")

        #Genero posición aleatoria de la lista a tomar
        pos = random.randint(0,4)
        print("Hilo", self.name, "quiere tomar la posición", pos)

        # Antes de acceder a la lista, bloqueo la ejecución
        BloqueaLista.bloqueo.acquire()
        if not BloqueaLista.lista[pos]:
            print("Hilo", self.name, "toma la posición", pos)
            BloqueaLista.lista[pos] = True

        # Una vez terminamos de trabajar con la lista liberamos
        BloqueaLista.bloqueo.release()