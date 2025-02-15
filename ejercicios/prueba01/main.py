from mithread import MiThread
from lock import BloqueaLista

if __name__ == '__main__':
    print("Soy el hilo principal")

    # for i in range(25):
    #     t = MiThread("Hilo " + str(i))
    #     t.start()
    
    for i in range(10):
        t = BloqueaLista(i)
        t.start()