#registro de datos
clientes = {}
#datos:
def crear_cuenta():
    cc = input("cedula: ")
    nombre = input("nombre: ")
    email = input("email: ")
    edad = input("edad: ")
    tel_movil = input("telefono movil: ")
    tel_fijo = input("telefono fijo: ")
    pais = input("pais: ")
    departamento = input("departamento: ")
    ciudad = input("ciudad: ")
    direccion = input("dirección: ")

    clientes[cc] = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "telefono_movil": tel_movil,
        "telefono_fijo": tel_fijo,
        "pais": pais,
        "departamento": departamento,
        "ciudad": ciudad,
        "direccion": direccion,
        "productos": {},
        "movimientos": []
    }
    print("cuenta creada.")

#depositar informacion al menu:
    
def depositar():
    cc = input("cedula: ")
    if cc in clientes:
        valor = float(input("valor a depositar: "))
        saldo = clientes[cc]["productos"].get("cuenta_ahorros", 0)
        clientes[cc]["productos"]["cuenta_ahorros"] = saldo + valor
        clientes[cc]["movimientos"].append({"tipo": "deposito", "valor": valor})
        print("deposito realizado.")
    else:
        print("cliente no registrado.")

def solicitar_credito():
    cc = input("cedula: ")
    if cc in clientes:
        valor = float(input("Valor del crédito: "))
        clientes[cc]["productos"]["credito"] = valor
        clientes[cc]["movimientos"].append({"tipo": "credito solicitado", "valor": valor})
        print("credito solicitado.")
    else:
        print("cliente no registrado.")

def retirar():
    cc = input("cedula: ")
    if cc in clientes:
        valor = float(input("Valor a retirar: "))
        saldo = clientes[cc]["productos"].get("cuenta_ahorros", 0)
        if valor <= saldo:
            clientes[cc]["productos"]["cuenta_ahorros"] = saldo - valor
            clientes[cc]["movimientos"].append({"tipo": "retiro", "valor": valor})
            print("retiro realizado.")
        else:
            print("saldo insuficiente.")
    else:
        print("Cliente no registrado.")

def pagar_cuota_credito():
    cc = input("Cedula: ")
    if cc in clientes and "credito" in clientes[cc]["productos"]:
        cuota = float(input("Valor de la cuota: "))
        credito = clientes[cc]["productos"]["credito"]
        if cuota <= credito:
            clientes[cc]["productos"]["credito"] = credito - cuota
            clientes[cc]["movimientos"].append({"tipo": "pago credito", "valor": cuota})
            print("completaste la cuota pagada.")
        else:
            print("cuota es mayor que la deuda.")
    else:
        print("no tiene credito activo.")

def cancelar_cuenta():
    cc = input("Cedula: ")
    if cc in clientes:
        del clientes[cc]
        print("Listo, cancelaremos esta cuenta.")
    else:
        print("cuenta ya borrada.")


#MENU:
        
while True:
    print("MENU PRINCIPAL")
    print("(1) Crear cuenta")
    print("(2) Depositar dinero")
    print("(3) Solicitar credito")
    print("(4) Retirar dinero")
    print("(5) Pago cuota credito")
    print("(6) Cancelar cuenta")
    print("(7) Salir")

    opcion = input("coloque el numero de la opcion: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        depositar()
    elif opcion == "3":
        solicitar_credito()
    elif opcion == "4":
        retirar()
    elif opcion == "5":
        pagar_cuota_credito()
    elif opcion == "6":
        cancelar_cuenta()
    elif opcion == "7":
        break
    else:
        print("seleccione algo valido")
