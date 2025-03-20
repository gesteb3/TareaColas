from cola import Cola

class Cliente:
    def __init__(self, nombre, vip=False):
        self.nombre = nombre
        self.vip = vip

    def __str__(self):
        return f"{self.nombre} - {'VIP' if self.vip else 'Regular'}"

class SistemaAtencion:
    def __init__(self):
        self.cola_vip = Cola()
        self.cola_regular = Cola()

    def agregar_cliente(self, nombre, vip=False):
        cliente = Cliente(nombre, vip)
        if vip:
            self.cola_vip.enqueue(cliente)
        else:
            self.cola_regular.enqueue(cliente)

    def atender_cliente(self):
        if not self.cola_vip.is_empty():
            return self.cola_vip.dequeue()  # Atendemos primero a los VIP
        elif not self.cola_regular.is_empty():
            return self.cola_regular.dequeue()  # Si no hay VIP, atendemos a los regulares
        else:
            return None  # Si no hay más clientes

    def mostrar_cola(self):
        print("\nClientes en la cola:")
        if not self.cola_vip.is_empty():
            print("Clientes VIP:")
            for i in range(self.cola_vip.frente, self.cola_vip.final + 1):
                print(f"  - {self.cola_vip.datos[i]}")
        if not self.cola_regular.is_empty():
            print("Clientes Regulares:")
            for i in range(self.cola_regular.frente, self.cola_regular.final + 1):
                print(f"  - {self.cola_regular.datos[i]}")
        if self.cola_vip.is_empty() and self.cola_regular.is_empty():
            print("  (No hay clientes en espera)")

sistema = SistemaAtencion()

sistema.agregar_cliente("Lucía Santos", vip=False)
sistema.agregar_cliente("Luis Martínez", vip=True)
sistema.agregar_cliente("José Maldonado", vip=False)
sistema.agregar_cliente("Andy Mazariegos", vip=True)
sistema.agregar_cliente("Oliver Meyers", vip=False)

sistema.mostrar_cola()

print("\nClientes:")
while True:
    cliente_atendido = sistema.atender_cliente()
    if cliente_atendido:
        print(f"Atendiendo a: {cliente_atendido}")
    else:
        print("No hay más clientes en la cola.")
        break
