import serial.tools.list_ports
#import numpy as np
#import pandas as pd
import datetime
import random
import time

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

def revisarArchivo():
    try:
        with open(PORT_NAME, 'r', encoding='utf-8') as f:
            puerto = f.readline()
            print(puerto)
            f.close()
        return puerto
    except:
        return ''

def abrirPuerto(arduino,puerto):
    try:
        arduino.open()
        with open(PORT_NAME,'w',encoding='utf-8') as f:
            f.write(puerto)
            f.close()
        datos = arduino.readline()
        cod = codeGen(10,False)
        ct = datetime.datetime.now()
        datos = datos.decode('utf-8')
        #datos = datos[:-2]+","+str(datetime.datetime.now())+","+cod+"\n"
        tem = datos.split(',')[0]
        hum = datos.split(',')[1]
        dat = str(ct.date())
        hou = str(ct.time())
        luv = datos.split(',')[2]
        newData = tem+","+hum+","+cod+","+dat+","+hou+","+luv
        with open(DATA_BASE,'a') as df:
            df.write(newData)
            df.close()
        print(newData)
        arduino.close()
    except:
        print("No se pudo conectar el Arduino")
        arduino.close()

def main():
    arduino = serial.Serial()
    arduino.baudrate = 9600

    puerto = revisarArchivo()
    arduino.port=puerto

    if puerto != '':
        print("hola")
        while True:
            abrirPuerto(arduino,puerto)
            time.sleep(60)
    else:
        ports = serial.tools.list_ports.comports()
        portList = []
        for port in ports:
            portList.append(port)
            print(str(port))
        #arduino.port = 'COM6'
        puerto = 'COM'
        puerto += input("Escoja el puerto COM: ")
        arduino.port = puerto
        for x in range(3):
            print(x)
            abrirPuerto(arduino,puerto)
            time.sleep(60)
#        with open(PORT_NAME, 'w', encoding='utf-8') as f:
#            f.write(puerto)
#            f.close()
if __name__ == '__main__':
    main()
