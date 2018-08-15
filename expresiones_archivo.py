# -*- coding: utf-8 -*-
from arbol_expresiones import convertir, evaluar
from pila import *

EXPRESIONS_FILE = "expresiones.in"
RESULT_FILE = "expresiones.out"

pila = Pila()

def readFile():
    file = open(EXPRESIONS_FILE, "r")
    filas = (file.read().splitlines())
    clearFile(RESULT_FILE)
    print("Expresiones: ")
    for exp in filas:
        convertir(exp.split(" "), pila)
        result = evaluar(pila.desapilar())
        print("{} : {}".format(exp,result))
        writeFile(str(result)+"\n")
    
    file.close()

def writeFile(result):
    file = open(RESULT_FILE, "a")
    file.write(result)
    file.close()

def clearFile(file):
    file = open(file, "w").close()

def run():
    readFile()

if __name__ == "__main__":
    run()

