import os



def salida ():
        print ("El programa se ha cerrado con exito :)")
        return False    
            
def agregar_usuario(lista):
    nombre = ""
    while len(nombre) == 0:
        nombre = input("ingrese nombre\n")
    lista.append(nombre)
    telefono = "" 
    while len(telefono) < 9:
        telefono = input("ingrese telefono ej:977777777\n")
    lista.append(telefono)
    email = ""
    while not "@" in email or len(email) <= 5 :
        email = input("ingrese correo\n") 
    lista.append(email)
    print("usuario agregado con exito")
    
def mostrar_usuario (lista):
    if len (lista) == 0:
        print("No hay contactos registrados todavia")
    else:
        for contacto in lista:
            print(f"contacto: {contacto}")
        os.system("Pause")
     
def buscar_contacto(lista):
    if len(lista) == 0:
        print("No hay contactos registrados todavia")
        return
    
    nombre_buscar = input("Ingrese el nombre a buscar: ").strip().lower()
    contactos_encontrados = []
    
    for contacto in lista:
        if nombre_buscar in contacto['nombre'].lower():
            contactos_encontrados.append(contacto)
    
    if len(contactos_encontrados) == 0:
        print("No se encontraron contactos con ese nombre")
    else:
        print("\n--- CONTACTOS ENCONTRADOS ---")
        for i, contacto in (contactos_encontrados, 1):
            print(f"{i}. Nombre: {contacto['nombre']}")
            print(f"   Telefono: {contacto['telefono']}")
            print(f"   Email: {contacto['email']}")

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

