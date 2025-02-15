from supermercado import Supermercado

if __name__ == '__main__':
    
    for i in range(1,10):
        t = Supermercado(i)
        t.start()