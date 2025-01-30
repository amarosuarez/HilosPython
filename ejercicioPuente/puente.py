import random
from threading import Semaphore, Thread
import time

class Puente(Thread):
    semaforoN = Semaphore(1)
    semaforoS = Semaphore(1)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        pass