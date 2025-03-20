class Cola:
    def __init__(self):
        self.datos = {}
        self.frente = 0
        self.final = -1

    def enqueue(self, elemento):
        self.final += 1
        self.datos[self.final] = elemento

    def dequeue(self):
        if self.is_empty():
            return None
        elemento = self.datos[self.frente]
        del self.datos[self.frente]
        self.frente += 1
        return elemento

    def front(self):
        return None if self.is_empty() else self.datos[self.frente]

    def is_empty(self):
        return self.frente > self.final

    def size(self):
        return self.final - self.frente + 1

class GestorTareas:
    def __init__(self):
        self.cola_alta_prioridad = Cola()
        self.cola_normal = Cola()

    def agregar_tarea(self, descripcion, prioridad):
        if prioridad == 1:
            self.cola_alta_prioridad.enqueue(descripcion)
        elif prioridad == 2:
            self.cola_normal.enqueue(descripcion)
        else:
            print("Prioridad no válida.")

    def procesar_tareas(self):
        print("\n Procesando tareas...")
        while not self.cola_alta_prioridad.is_empty():
            tarea = self.cola_alta_prioridad.dequeue()
            print(f"Tarea urgente: {tarea}")

        while not self.cola_normal.is_empty():
            tarea = self.cola_normal.dequeue()
            print(f" Tarea normal procesada: {tarea}")

    def mostrar_tareas(self):
        print(" Tareas por procesar:")
        if not self.cola_alta_prioridad.is_empty():
            print("Alta prioridad:")
            for i in range(self.cola_alta_prioridad.frente, self.cola_alta_prioridad.final + 1):
                print(f"  - {self.cola_alta_prioridad.datos[i]}")
        else:
            print("  (No hay tareas de alta prioridad)")

        if not self.cola_normal.is_empty():
            print("Normal:")
            for i in range(self.cola_normal.frente, self.cola_normal.final + 1):
                print(f"  - {self.cola_normal.datos[i]}")
        else:
            print("  (No hay tareas normales)")

gestor = GestorTareas()

gestor.agregar_tarea("Realizar tarea programación", 1)
gestor.agregar_tarea("Revisar tareas de emprendedores de negocios", 2)
gestor.agregar_tarea("Leer 15 minutos", 1)
gestor.agregar_tarea("Preparar instrumentos para electronica", 2)

gestor.mostrar_tareas()

gestor.procesar_tareas()

