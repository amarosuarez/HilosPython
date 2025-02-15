from filosofo import Filosofo

nombres = ["Aristóteles", "Sócrates", "Platón", "Descartes", "Kant"]

if __name__ == "__main__":
    for i in range(0, 5):
        f = Filosofo(nombres[i], i)
        f.start()