import serial.tools.list_ports
import numpy as np
import pandas as pd
import datetime
import random

PORT_NAME = 'puertos.txt'
DATA_BASE = 'baseDatos.csv'

chara = {
        "mayus":("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"),
        "minus":("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),
        "numer":("1","2","3","4","5","6","7","8","9","0"),
        "espec":("!","#","$","%","&","/","(",")","=","^","+","-","*","-","_","'","¡","¿","?","~"," "),
} #Biblioteca de carácteres

def selector(exep, sim):                    #Selector de cáracter
    ind = random.randint(1,4)               #Determina la llave a seleccionar, considerando expeciones de repeticion o caracteres especiales
    if sim:
        while ind == exep:                  #Excluye tipo de caracter recientemente utilizado
            ind = random.randint(1,4)
    else:
        while ind == exep or ind == 4:      #Excluye tipo de caracter recientemente utilizado Y caracteres especiales
            ind = random.randint(1,3)
    if ind == 1:
        cate = chara.get("mayus")
    elif ind == 2:
        cate = chara.get("minus")
    elif ind == 3:
        cate = chara.get("numer")
    elif ind == 4:
        cate = chara.get("espec")
    sel = random.randint(0,len(cate)-1)
    car = cate[sel]
    return car, ind

def codeGen(size, esp):
    ale = selector(0, esp)
    passW = ale[0]
    ind = ale[1]
    for x in range(1,size):
        ale = selector(ind, esp)
        passW = passW + ale[0]
        ind = ale[1]
    return passW

def main():
	passWord = codeGen(10, False)
	print(passWord)    

if __name__ == '__main__':
    main()
