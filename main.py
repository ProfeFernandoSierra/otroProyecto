import os
os.system("cls")
from functions import *

lista = []
on = True
while on:
    print("\t\tMENU AGENDA DE CONTACTOS\n")
    print("1) Agregar un contacto: nombre, teléfono, email.")
    print("2) Listar contactos: mostrar todos los contactos guardados.")
    print("3) Buscar un contacto por nombre.")
    print("4) Eliminar un contacto.")
    print("5) Salir del programa.\n")
    try:
        opcion = int(input("Seleccione una opcion\n"))
        if opcion == 1:
            print("Agregar contacto")
            agregar_usuario(lista)
        elif opcion == 2:
            mostrar_usuario(lista)
        elif opcion == 3:
            print("a")
        elif opcion == 4:
            print("a")
        elif opcion == 5:
            on = salida()
    except:
        print("Ingrese carecteres numericos")