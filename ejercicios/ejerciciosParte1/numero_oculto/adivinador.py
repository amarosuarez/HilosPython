from threading import Thread, Condition, Barrier
import random
from colorama import Fore


class Comprobador:
    encontrado = False
    cond = Condition()
    barrera = Barrier(10)

    def __init__(self):
        Thread.__init__(self)
        self.num = random.randint(0, 101)

class Adivinador(Thread):
    def __init__(self, nombre, numero):
        Thread.__init__(self, name = nombre)
        self.numero = numero

    def run(self):
        while True:
            try:
                self.numero.barrera.wait()
            except:
                pass
            with self.numero.cond:
                if self.numero.encontrado:
                    break
                else:
                    numRandom = random.randint(0, 101)
                    if self.numero.num == numRandom:
                        print(f"{Fore.GREEN}{self.name}: Numero encontrado -> {numRandom}")
                        self.numero.encontrado = True
                        self.numero.barrera.abort()
                        print(Fore.RESET)
                    else:
                        print(f"{Fore.RED}{self.name}: {numRandom} no era el numero buscado")