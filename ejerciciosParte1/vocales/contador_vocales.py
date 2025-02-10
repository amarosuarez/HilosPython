import threading

class ContadorVocales(threading.Thread):
    def __init__(self, vocal, archivo):
        super().__init__()
        self.vocal = vocal
        self.archivo = archivo
        self.cantidad = 0

    def run(self):
        with open(self.archivo, 'r', encoding='utf-8') as f:
            texto = f.read().lower()
            self.cantidad = texto.count(self.vocal)
        print(f"Vocal '{self.vocal}': {self.cantidad} veces")