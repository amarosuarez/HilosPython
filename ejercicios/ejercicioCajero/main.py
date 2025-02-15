from banco import Banco

if __name__ == '__main__':
    for i in range(1,10):
        t = Banco(i)
        t.start()