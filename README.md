# TareaColas
# Proyecto 1: Gestor de tareas

## Descripción
Este proyecto implementa un **Gestor de Tareas** utilizando una estructura de **Cola (FIFO - First In, First Out)**. Se administran tareas con dos niveles de prioridad: **alta** y **normal**. Las tareas urgentes se procesan antes que las normales.

## Estructura del Código
### **Clase Cola**
Maneja una estructura FIFO para el almacenamiento y gestión de tareas.

### **Clase GestorTareas**
- `agregar_tarea(descripcion, prioridad)`: Agrega tareas con prioridad **1 (Alta)** o **2 (Normal)**.
- `procesar_tareas()`: Procesa primero las tareas urgentes y luego las normales.
- `mostrar_tareas()`: Muestra las tareas pendientes por prioridad.

## Uso
```python
from gestor_tareas import GestorTareas

gestor = GestorTareas()

gestor.agregar_tarea("Realizar tarea programación", 1)
gestor.agregar_tarea("Revisar tareas de emprendedores", 2)
gestor.agregar_tarea("Leer 15 minutos", 1)

gestor.mostrar_tareas()
gestor.procesar_tareas()
```

---

# Proyecto 2: Sistema de atención al cliente

## Descripción
Este proyecto implementa un **Sistema de Atención al Cliente** con dos colas de prioridad:
- **Clientes VIP** (se atienden primero).
- **Clientes Regulares** (se atienden después de los VIPs).

## Estructura del Código
### **Clase cliente**
Representa a un cliente con su nombre y tipo (VIP o Regular).

### **Clase SistemaAtencion**
- `agregar_cliente(nombre, vip)`: Agrega clientes a la cola correspondiente.
- `atender_cliente()`: Atiende clientes en orden de prioridad.
- `mostrar_cola()`: Muestra los clientes en espera.

## Uso
```python
from sistema_atencion import SistemaAtencion

sistema = SistemaAtencion()

sistema.agregar_cliente("Lucía Santos", vip=False)
sistema.agregar_cliente("Luis Martínez", vip=True)
sistema.agregar_cliente("José Maldonado", vip=False)

sistema.mostrar_cola()

while True:
    cliente_atendido = sistema.atender_cliente()
    if cliente_atendido:
        print(f"Atendiendo a: {cliente_atendido}")
    else:
        print("No hay más clientes en la cola.")
        break
```
