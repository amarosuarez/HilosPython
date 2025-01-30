from threading import Lock, Thread

class Panaderia(Thread):
    numPanes = 7
    bloqueo = Lock()

    def __init__(self):
        Thread.__init__(self)
    
    def compra_pan(self):
        Panaderia.bloqueo.acquire()

        if Panaderia.numPanes > 0:
            Panaderia.numPanes -= 1
            ok = True
        else:
            print('No queda pan')
            ok = False
        
        Panaderia.bloqueo.release()
        return ok

    def run(self):
        Panaderia.compra_pan(self)
