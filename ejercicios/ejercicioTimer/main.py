from threading import Timer
import time

def funcion():
    print("hola mundo")

if __name__ == "__main__":
    temporizador = Timer(5, funcion)
    temporizador.start()
    # temporizador.cancel()
    # temporizador.join()
    print("Esperando a que se ejecute la función")