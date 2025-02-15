from adivinador import Adivinador, Comprobador
import random

if __name__ == '__main__':
    nombres = ['Amaro', 'Auri', 'Jenri', 'Laura', 'Marta', 'Lucía', 'Héctor', 'Raúl', 'Lorenzo', 'Marco']
    comprobador = Comprobador()
    for i in range(10):
        hilo = Adivinador(nombres[i], comprobador)
        hilo.start()