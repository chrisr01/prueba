import os
import sys
import time
from modu_prob import *
print("programa para calcular sumas y restas")
print("")

def eleccion():
    os.system("clear")
    print("\tSUMAS Y RESTAS")
    print("\t1.-suma")
    print("\t2.-resta")
    print("\t3.-salir")
    while True:
        try:
            x=int(input("selccione la operacion q desea"))
            if (x==1):
                suma()
                eleccion()
            elif (x==2):
                resta()
                eleccion()
            elif (x==3):
                salir()
            break
        except ValueError():
            print("ingrese una opcion correcta")
datos()
eleccion()

