from raton import Raton
from threading import Event

if __name__ == "__main__":
    event = Event()
    # Marcamos el plato como libre
    event.set()

    for i in range(1, 4):
        r = Raton(i, event)
        r.start()
