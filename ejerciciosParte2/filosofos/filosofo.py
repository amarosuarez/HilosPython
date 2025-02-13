# import random
# from threading import Condition, Thread
# import time

# class Filosofo(Thread):
#     palillo = 0
#     palillos = [False, False, False, False, False]
#     cond = Condition()

#     def __init__(self, nombre, palillo):
#         Thread.__init__(self, name=nombre)
#         self.palillo = palillo

#     def run(self):
#         # Se pone a estudiar
#         # print("Soy", self.name, "y estoy estudiando...📕")
#         time.sleep(random.randint(0, 7))
#         # print("Soy", self.name, "y he terminado de estudiar📓")
#         # print("Soy", self.name, "y tengo el palillo", self.palillo, "a mi izquierda y el", self.palillo+1, "a mi derecha")

#         with Filosofo.cond:
#             while Filosofo.palillos[self.palillo] == True:
#                 print("Soy", self.name, "y estoy esperando al palillo de la izquierda⏳")
#                 Filosofo.cond.wait()

#             Filosofo.palillos[self.palillo] = True
#             print("Soy", self.name, "y he cogido el palillo de la izquierda")

#             while Filosofo.palillos[(self.palillo+1)%5] == True:
#                 print("Soy", self.name, "y estoy esperando al palillo de la derecha⏳")
#                 Filosofo.cond.wait()

#             Filosofo.palillos[(self.palillo+1)%5] = True
#             print("Soy", self.name, "y he cogido el palillo de la derecha")

#         print("Soy", self.name, "y estoy comiendo🥖")
#         time.sleep(random.randint(0,7))
#         print("Soy", self.name, "y terminé")

#         with Filosofo.cond:
#             Filosofo.palillos[self.palillo] = False
#             Filosofo.palillos[(self.palillo+1)%5] = False
#             Filosofo.cond.notifyAll()



import random
from threading import Condition, Thread
import time

class Filosofo(Thread):
    palillo = 0
    palillos = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre, palillo):
        Thread.__init__(self, name=nombre)
        self.palillo = palillo

    def run(self):
        # Se pone a estudiar
        # print("Soy", self.name, "y estoy estudiando...📕")
        time.sleep(random.randint(0, 7))
        # print("Soy", self.name, "y he terminado de estudiar📓")
        # print("Soy", self.name, "y tengo el palillo", self.palillo, "a mi izquierda y el", self.palillo+1, "a mi derecha")

        Filosofo.cond.acquire()
        while Filosofo.palillos[self.palillo] == True:
            print("Soy", self.name, "y estoy esperando al palillo de la izquierda⏳")
            Filosofo.cond.wait()
            
        Filosofo.palillos[self.palillo] = True
        print("Soy", self.name, "y he cogido el palillo de la izquierda")
        Filosofo.cond.release()


        Filosofo.cond.acquire()
        while Filosofo.palillos[(self.palillo+1)%5] == True:
            print("Soy", self.name, "y estoy esperando al palillo de la derecha⏳")
            Filosofo.cond.wait()

        Filosofo.palillos[(self.palillo+1)%5] = True
        print("Soy", self.name, "y he cogido el palillo de la derecha")
        Filosofo.cond.release()


        print("Soy", self.name, "y estoy comiendo🥖")
        time.sleep(random.randint(0,7))
        print("Soy", self.name, "y terminé")

        Filosofo.cond.acquire()
        Filosofo.palillos[self.palillo] = False
        Filosofo.palillos[(self.palillo+1)%5] = False
        Filosofo.cond.notifyAll()
        Filosofo.cond.release()









