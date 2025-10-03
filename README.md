# Sistema de Gestión de Cuentas - Banco Virtual

## 🚀 Descripción del Proyecto

Este proyecto es un sistema básico para gestionar cuentas bancarias de clientes. Permite crear cuentas, hacer depósitos, solicitar créditos, retirar dinero, pagar cuotas de crédito, y cancelar cuentas. Todos los datos se almacenan de manera persistente en un archivo `JSON` para simular un banco virtual.

---

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje de programación utilizado para el desarrollo del sistema.
- **JSON**: Almacenamiento de los datos en un archivo `base_datos.json` para mantener la persistencia.
- **Funciones y Estructuras**: Uso de funciones para realizar operaciones bancarias y diccionarios para gestionar los datos de los clientes.

---

## ⚙️ Funcionamiento del Sistema

El sistema tiene las siguientes funcionalidades clave:

1. **Crear Cuenta**: Permite crear una nueva cuenta bancaria ingresando datos como cédula, nombre, correo, etc.
2. **Depositar Dinero**: Los clientes pueden depositar dinero en su cuenta de ahorros.
3. **Solicitar Crédito**: Los clientes pueden solicitar un crédito que se agrega a su cuenta.
4. **Retirar Dinero**: Los clientes pueden retirar dinero de su cuenta de ahorros, si tienen suficiente saldo.
5. **Pagar Cuota de Crédito**: Los clientes pueden pagar las cuotas de su crédito.
6. **Cancelar Cuenta**: Los clientes pueden cancelar su cuenta, eliminando todos sus datos del sistema.

---

## 💻 Estructura del Proyecto

El sistema se ejecuta desde el archivo `main.py`, que interactúa con un archivo `base_datos.json` para almacenar la información de las cuentas de los clientes. Cada operación sobre las cuentas se guarda automáticamente después de su ejecución.

### Archivos principales:
- `main.py`: Contiene el código principal que gestiona las operaciones y el menú interactivo.
- `data.py`: Define las funciones de guardado (`guardado`) y carga de datos (`cargar_datos`).
- `base_datos.json`: Archivo donde se almacenan los datos de los clientes.

---

## 📝 Instrucciones de Uso
- se inicia desde main.py
