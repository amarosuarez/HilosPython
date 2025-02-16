import random
from threading import Thread, Condition, Lock
import time

nombres = ["Ana",  "Juan", "Pedro", "Pepe", "Alberto", "Daniel", "Raul", "Carlos"]
Colores =["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m"]
normal = "\033[0m"




class Consumidor(Thread): 
    condicion = Condition()
    clienteEsperando = 0
    lock = Lock()
    def __init__(self):
        Thread.__init__(self)
        self.nombre = random.choice(nombres)
        self.color = random.choice(Colores)
        
        
    def run(self):
        with Consumidor.lock:
            Consumidor.clienteEsperando += 1
            
        print(f"{self.color}El consumidor {self.nombre} hace un pedido{normal}")
        print(f"{self.color}El consumidor {self.nombre} está esperando para recibir la hamburguesa{normal}")
        time.sleep(2)
        with Consumidor.condicion:
            Consumidor.condicion.wait()
        print(f"{self.color}El consumidor {self.nombre} sabe que la hamburguesa está lista y va a por ella 😋{normal}")
        print(f"{self.color}El cliente ha llegado a por su comida 🍔{normal}")
        with Consumidor.lock:
            Consumidor.clienteEsperando -= 1
        

class Cocinero(Thread):
    comidaCliente = ""
    def __init__(self):
        Thread.__init__(self)
        self.color = random.choice(Colores)
        
        
    def run(self):
        while Consumidor.clienteEsperando != 0:
            
            print(f"{self.color}El cocinero recibe el pedido y se pone manos a la obra... 👨‍🍳{normal}")

            time.sleep(5)
            print(f"El cocinero ha acabado de hacer el pedido y se la entrega al cliente")
            comidaCliente = "🍔"
            with Consumidor.condicion:
                Consumidor.condicion.notify()
        print("El cocinero ha acabao y esta hasta el nabo")
        
if __name__ == "__main__":
    lista_clientes = [Consumidor() for _ in range(5)]
    cocinerillo = Cocinero()
    
    for cliente in lista_clientes:
        cliente.start()
    cocinerillo.start() # hay uno espabilao, solo puede hacerlo fuera por que no se inicializaria uno cada vez que hay un cliente fcker
        
    for cliente in lista_clientes:
        cliente.join()
    cocinerillo.join()