import serial.tools.list_ports
import pandas as pd
import datetime
import random
import time

DATA_BASE = './basedatos/datos.csv'
dirDataBase = "./basedatos/{}"

def revisarArchivo(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            puerto = f.readline()
#            print(puerto)
            f.close()
        return puerto
    except:
        return ''

def main():
    try:
        tablaDatos = pd.read_csv(dirDataBase.format("datos.csv"))
        if (not tablaDatos.empty):
            tablaDatos.drop(["Unnamed: 0"],axis=1,inplace=True)
        with open(DATA_BASE,'r',encoding='utf-8') as f:
            datos = f.readlines()
            print("tamaño datos")
            print(numpy.shape(datos))
            print("fin")
    except:
        print("XD")

if __name__ == '__main__':
    main()
