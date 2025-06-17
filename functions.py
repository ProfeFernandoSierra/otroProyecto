lista = []

def salida ():
        print ("El programa se ha cerrado con exito :)")
        return False

def menu():
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
                print("a")
            elif opcion == 3:
                print("a")
            elif opcion == 4:
                print("a")
            elif opcion == 5:
               on = salida()
        except:
            print("Ingrese carecteres numericos")
            
def agregar_usuario(lista):
    nombre = ""
    while len(nombre) == 0:
        nombre = input("ingrese nombre\n")
    telefono = "" 
    while len(telefono) < 9:
        telefono = input("ingrese telefono ej:977777777\n")
    email = ""
    while not "@" in email and len(email) <= 5 :
        email = input("ingrese correo\n") 
    lista.append(nombre, telefono, email)
    print("usuario agregado con exito")      
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa.

