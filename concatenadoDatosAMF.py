import serial.tools.list_ports
import pandas as pd
import datetime
import random
import time

DATA_BASE = './basedatos/blockAlex.txt'
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
        x = len(datos)
        for ind in range(x):
            #print(datos[ind])
            tem = datos[ind].split(',')[0]
            #print(tem)
            hum = datos[ind].split(',')[1]
            #print(hum)
            noS = datos[ind].split(',')[2]
            #print(noS)
            dat = datos[ind].split(',')[3]
            #print(dat)
            hou = datos[ind].split(',')[4]
            #print(hou)
            luv = datos[ind].split(',')[5]
            #print(luv)
            newData = {"S1:Temperatura":tem,"S2:Humedad":hum,"No Serie":noS,"Fecha":dat,"Hora":hou,"Lluvia":luv}
            #print(newData)
            tablaDatos = tablaDatos.append(newData,ignore_index=True)
            print(tablaDatos)
            tablaDatos.to_csv((dirDataBase).format("datos.csv",index=False))
    except:
        print("XD")

if __name__ == '__main__':
    main()
