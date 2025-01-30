import random
from threading import Thread, Condition
import time

class Estudiante(Thread):
    libros = [False, False, False, False, False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.libro1 = random.randint(0,8)
        self.libro2 = random.randint(0,8)
        while self.libro2 == self.libro1:
            self.libro2 = random.randint(0,8)

    def run(self):
        with Estudiante.cond:
            while self.libros[self.libro1] == True or self.libros[self.libro2] == True:
                print('El estudiante', self.name , 'está esperando a almenos uno de sus libros')
                Estudiante.cond.wait()
            
            self.libros[self.libro1] = True
            self.libros[self.libro2] = True

        print('El estudiante', self.name, 'ha cogido sus dos libros', self.libro1, 'y', self.libro2)
        time.sleep(random.randint(1,5))
        print('El estudiante', self.name, 'ha terminado de usar sus libros')

        with Estudiante.cond:
            self.libros[self.libro1] = False
            self.libros[self.libro2] = False

            Estudiante.cond.notifyAll()