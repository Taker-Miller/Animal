from Animal import Animal
from Dao import DAO

def registrar():
    codigo = input("Ingresa codigo del animal: ")
    raza = input("Ingresa la raza del animal: ")
    patas = input("Ingresa numero de patas del animal: ")
    peso = input("Ingresa el peso del animal: ")
    a = Animal(codigo, raza, patas, peso)
    d = DAO()
    d.registrar_animal(a)

def buscar()->Animal:
    codigo = input("Ingrese codigo del animal por buscar: ")
    d = DAO()
    a = d.buscar_animal(codigo)
    if a != None:
        print(a)
    else:
        print("El animal buscado no se encuentra")
    return a

def eliminar():
    a = buscar()
    if a != None:
        opcion = input("Desea eliminar a este animal (s/n): ")
        if opcion.lower() == "s":
            d = DAO()
            d.eliminar_animal(a.get_id()) 
        else:
            print("No se ha eliminado el animal")

def modificar():
    a = buscar()
    if a != None:
        codigo = recibir_valor("codigo", a.get_codigo())
        a.set_codigo(codigo)
        raza = recibir_valor("raza", a.get_raza())
        a.set_raza(raza)
        peso = recibir_valor("peso", a.get_peso())
        a.set_peso(float(peso))
        patas = int(recibir_valor("patas", a.get_patas()))
        a.set_patas(patas)
        d = DAO()
        d.modificar_animal(a)

def recibir_valor(nombre_atributo: str, atributo):
    opcion = input(f"Desea modificar {nombre_atributo} (s/n): ")
    if opcion.lower() == "s":
        valor = input(f"Ingrese nuevo {nombre_atributo}: ")
        return valor
    return atributo

def mostrar_todo():
    d = DAO()
    animales = d.mostrar_animales()
    for a in animales:
        print("----------")
        print(a)
        print("----------")

def menu():
    print("1- Registrar")
    print("2- Buscar")
    print("3- Eliminar")
    print("4- Modificar")
    print("5- Mostrar todo")
    print("6- Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        registrar()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        eliminar()
    elif opcion == "4":
        modificar()
    elif opcion == "5":
        mostrar_todo()
    elif opcion == "6":
        return True
    else:
        print("La opcion ingresada no es valida")

while menu() != True:
    pass