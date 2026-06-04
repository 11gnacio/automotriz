# main.py
import os
from datetime import datetime

# Importamos las clases directamente
from Administracion import Administracion
from Propietario import Propietario
from Vehiculo import Vehiculo
from Operaciones import Operaciones

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

# =====================================
# MENÚ PRINCIPAL

while True:
    print("\n")
    print("====================================")
    print("    SISTEMA REGISTRO AUTOMOTRIZ")
    print("====================================")
    print("1. Listar vehículos activos")
    print("2. Registrar un nuevo vehículo")
    print("3. Listar propietarios")
    print("4. Registrar nuevo propietario")
    print("5. Listar catálogos (Marcas y Modelos)")
    print("6. Agregar configuración (Marca o Modelo)")
    print("7. Registrar venta de vehículo")
    print("8. Cargar infracción (Multa)")
    print("9. Ver historial de multas")
    print("10. Salir")
    print("====================================")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        limpiarConsola()
        print("\n===== VEHÍCULOS EN BASE DE DATOS =====")
        Vehiculo.listar_detallado()

    elif opcion == "2":
        limpiarConsola()
        print("\n===== NUEVO VEHÍCULO =====")
        patente = input("Patente: ")
        vin = input("VIN / Chasis: ")
        modelo_id = int(input("ID del Modelo (Ver opción 5): "))
        combustible_id = int(input("ID Combustible (1=Nafta, 2=Diesel...): "))
        moneda_id = input("Código Moneda (USD/ARS): ").upper()
        estado_id = int(input("ID Estado (1=Excelente, 2=Bueno...): "))
        anio = int(input("Año de Fabricación: "))
        precio = float(input("Precio de Adquisición: "))
        fecha = datetime.now().strftime('%Y-%m-%d')
        
        prop_id = input("ID Propietario (Enter si queda en Stock): ")
        prop_id = int(prop_id) if prop_id else None

        # Llamada estática directa como en tu sistema escolar
        Vehiculo.guardar(patente, vin, modelo_id, combustible_id, moneda_id, estado_id, anio, precio, fecha, prop_id)

    elif opcion == "3":
        limpiarConsola()
        print("\n===== PROPIETARIOS REGISTRADOS =====")
        Propietario.listar()

    elif opcion == "4":
        limpiarConsola()
        print("\n===== NUEVO PROPIETARIO =====")
        doc = input("Documento de Identidad: ")
        nom = input("Nombre: ")
        ape = input("Apellido: ")
        tel = input("Teléfono: ") or None
        em = input("Email: ") or None
        dir = input("Dirección: ") or None

        Propietario.guardar(doc, nom, ape, tel, em, dir)

    elif opcion == "5":
        limpiarConsola()
        print("\n===== MARCAS DISPONIBLES =====")
        Administracion.listar_marcas()
        print("\n===== MODELOS DISPONIBLES =====")
        Administracion.listar_modelos()

    elif opcion == "6":
        limpiarConsola()
        print("\n===== AGREGAR CONFIGURACIÓN =====")
        print("1. Agregar Nueva Marca")
        print("2. Agregar Nuevo Modelo")
        sub_opc = input("Seleccione (1-2): ")
        
        if sub_opc == "1":
            nombre_m = input("Nombre de la Marca: ")
            Administracion.agregar_marca(nombre_m)
        elif sub_opc == "2":
            Administracion.listar_marcas()
            id_m = int(input("\nIngrese el ID de la Marca: "))
            nombre_mod = input("Nombre del Modelo: ")
            Administracion.agregar_modelo(id_m, nombre_mod)

    elif opcion == "7":
        limpiarConsola()
        print("\n===== REGISTRAR TRANSACCIÓN DE VENTA =====")
        Vehiculo.listar_detallado()
        id_v = int(input("\nIngrese ID del vehículo vendido: "))
        Propietario.listar()
        id_comprador = int(input("\nIngrese ID del Comprador: "))
        id_vendedor = input("ID Vendedor (Enter si vende Agencia): ")
        id_vendedor = int(id_vendedor) if id_vendedor else None
        precio_v = float(input("Precio final: "))
        moneda = input("Moneda: ").upper()

        Operaciones.registrar_venta(id_v, id_comprador, precio_v, moneda, id_vendedor)

    elif opcion == "8":
        limpiarConsola()
        print("\n===== REGISTRAR NUEVA INFRACCIÓN =====")
        Vehiculo.listar_detallado()
        id_v = int(input("\nIngrese ID del vehículo infractor: "))
        desc = input("Descripción de la multa: ")
        monto = float(input("Monto penal: "))
        fecha_m = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        Operaciones.registrar_multa(id_v, fecha_m, desc, monto)

    elif opcion == "9":
        limpiarConsola()
        print("\n===== HISTORIAL GENERAL DE MULTAS =====")
        Operaciones.ver_multas()

    elif opcion == "10":
        print("\nPrograma finalizado.")
        break
    else:
        print("\nOpción inválida.")