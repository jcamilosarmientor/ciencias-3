from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/=":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol, variables):
    if arbol.valor in variables.keys():
        return variables[arbol.valor]
    if arbol.valor == "+":
        return evaluar(arbol.izq, variables) + evaluar(arbol.der, variables)
    if arbol.valor == "-":
        return evaluar(arbol.izq, variables) - evaluar(arbol.der, variables)
    if arbol.valor == "/":
        return evaluar(arbol.izq, variables) / evaluar(arbol.der, variables)
    if arbol.valor == "*":
        return evaluar(arbol.izq, variables) * evaluar(arbol.der, variables)
    if arbol.valor == "=":
        return { arbol.der.valor: evaluar(arbol.izq, variables) }
        # return "{} = {}".format(arbol.der.valor, evaluar(arbol.izq, variables))
    
    return int(arbol.valor)
    
# exp = raw_input("ingrese l expresion en posfija: ").split(" ")

# pila = Pila()

# convertir(exp, pila)

# print evaluar(pila.desapilar())

