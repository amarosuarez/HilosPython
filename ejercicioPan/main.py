from comprador import Comprador
from panaderia import Panaderia

if __name__ == '__main__':
    p = Panaderia()
    for i in range(10):
        t = Comprador(i, p)
        t.start()