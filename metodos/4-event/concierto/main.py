from comprador import Comprador
from empresa import Empresa
import time, random

nombres = [
    "Amaro", "Fred", "Marta", "Auri", "Jenri", "Lucas", "Sofía", "Daniel", "Elena", "Hugo",
    "Valeria", "Mateo", "Camila", "Alejandro", "Isabella", "Gabriel", "Natalia", "Diego", "Emma", "Javier"
]

if __name__ == "__main__":
    empresa = Empresa("APPLE")
    empresa.start()

    for i in range(20):
        c = Comprador(nombres[i], empresa)
        # Simulamos lo que tarda en entrar a la web
        time.sleep(random.uniform(0.1, 0.25))
        c.start()