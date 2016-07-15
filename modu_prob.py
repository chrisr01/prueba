import os
import sys
import time
def datos():
    print("ingrese un numero: ")
    global x
    x=input()
    x=int(x)
    print("ingrese otro numero: ")
    global y
    y=input()
    y=int(y)
def suma():
    os.system("clear")
    sum=x+y
    print("la suma es",sum)
    time.sleep(2)
def resta():
    os.system("clear")
    rest=x-y
    print("la resta es",rest)
    time.sleep(2)
def salir():
    os.system("clear")
    print("el programa se esta cerrando...")
    sys.exit()







