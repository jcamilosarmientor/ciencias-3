# -*- coding: utf-8 -*-
from cola import *

def run():
    print("inicio....")
    cola = Cola()
    cupo = 3
    continuar = True
    while continuar:
        print(cola.items)
        if cupo > len(cola.items):
            placa = raw_input("Placa: ")
            color = raw_input("Color: ")
            vehiculo = {'Placa': placa, 'Color': color}
            cola.encolar(vehiculo)
        else:
            resp = raw_input("Cupo lleno. ¿Despachar Vehículo? S/N\n")
            if resp == 'S':
                desencolado = cola.desencolar()
                print('El carro {} fue despachado'.format(desencolado))
            else:
                cont = raw_input("¿Continuar? S/N\n")
                if resp == 'N':
                    continuar = False

        

if __name__ == '__main__':
    run()
