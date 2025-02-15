import random
from threading import Thread, Condition
import time

class Estudiante(Thread):
    libros = [False, False, False, False, False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        # Generamos los libros de forma aleatoria
        self.libro1 = random.randint(0,8)
        self.libro2 = random.randint(0,8)

        # Comprobamos que no sea el mismo libro
        while self.libro2 == self.libro1:
            self.libro2 = random.randint(0,8)

    def run(self):
        # with reemplaza a acquire() y release()
        with Estudiante.cond:
            # comprueba que ambos libros estén libres, sino se queda esperando
            while self.libros[self.libro1] == True or self.libros[self.libro2] == True:
                print('El estudiante', self.name , 'está esperando a almenos uno de sus libros')
                Estudiante.cond.wait()
            
            # Una vez estén libres, los coge
            self.libros[self.libro1] = True
            self.libros[self.libro2] = True

        # Usa los libros
        print('El estudiante', self.name, 'ha cogido sus dos libros', self.libro1, 'y', self.libro2)
        time.sleep(random.randint(1,5))
        print('El estudiante', self.name, 'ha terminado de usar sus libros')

        # Suelta los libros y notifica a todos
        with Estudiante.cond:
            self.libros[self.libro1] = False
            self.libros[self.libro2] = False

            Estudiante.cond.notifyAll()