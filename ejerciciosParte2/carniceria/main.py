from carniceria import Carniceria
import threading

if __name__ == "__main__":
    num_empleados = 4
    num_clientes = 10
    carniceria = Carniceria(num_empleados)

    clientes = []
    for i in range(num_clientes):
        cliente = threading.Thread(target=carniceria.atender_cliente, args=(f"Cliente-{i+1}",))
        clientes.append(cliente)
        cliente.start()

    for cliente in clientes:
        cliente.join()

    print("\n🏁 Todos los clientes han sido atendidos. La carnicería cierra por hoy.")