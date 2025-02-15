import threading
import time
import random

class MiThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        time.sleep(random.randint(1,10))
        print("Soy el hilo", self.num)