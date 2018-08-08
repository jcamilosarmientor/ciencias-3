# -*- coding: utf-8 -*-
from cola import *
from colores import *


cola = Cola()

def imprimirResultado(lista):
    print("Libros: ")
    for item in lista:
        print("* {}".format(item))
    print("")

def buscar(criterio, valor_busqueda):
    cola_resultados = Cola()
    for item in cola.items:
        if valor_busqueda == item[criterio]:
            cola_resultados.encolar(item)
    imprimirResultado(cola_resultados.items)

def run():
    print("Inicio...")
    OPCIONES = bcolors.BOLD + "1) Registrar libro \n2) Consultar libros por género\n3) Consultar libros por autor\n4) Consultar libro por nombre\n5) Ver todos los libros"
    while True:
        opcion = int(raw_input("Selecciona el número de la opción para la consulta: \n{}:\n".format(OPCIONES)))
        
        if opcion == 1:
            print("\tRegistrar Libro\n")
            nombre = raw_input("Nombre: ")
            autor = raw_input("Autor: ")
            genero = raw_input("Género: ")
            libro = {
                'Nombre': nombre,
                'Autor': autor,
                'Genero': genero
            }
            cola.encolar(libro)
            
        elif opcion == 2:
            print("\tConsultar libros por genero")
            gen_buscar = raw_input("Ingrese el criterio de búsqueda: ")
            buscar('Genero',gen_buscar)
            
        elif opcion == 3:
            print("\tConsultar libros por autor")
            gen_buscar = raw_input("Ingrese el criterio de búsqueda: ")
            buscar('Autor',gen_buscar)

        elif opcion == 4:
            print("\tConsultar libro por nombre")
            gen_buscar = raw_input("Ingrese el criterio de búsqueda: ")
            buscar('Nombre',gen_buscar)
        elif opcion == 5:
            imprimirResultado(cola.items)
        else:
            print("Opcion no valida... ")
    
    
if __name__ == '__main__':
    run()
