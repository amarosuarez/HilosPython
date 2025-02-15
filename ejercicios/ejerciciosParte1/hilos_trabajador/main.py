from trabajador import Trabajador
nombres = ["Amaro", "Rubén", "Jenri", "Marta", "Lucía"]

if __name__ == "__main__":
    for i in range(5):
        t = Trabajador(nombres[i])
        t.start()
