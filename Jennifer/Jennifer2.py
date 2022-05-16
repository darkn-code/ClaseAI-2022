import serial.tools.list_ports
import pandas as pd
import numpy as np
import random
import string
import datetime

dirBaseDatos="./BaseDatos/{}"
NO_SERIE= "Archivo.txt"


PORT_NAME = 'puertos.txt'

def revisarArchivo():
    try:
        with open(PORT_NAME,'r',encoding='utf-8') as f:
            puerto = f.readline()
            f.close()
    except:
        return ''
    return puerto

def abrirPuerto(arduino,puerto):
    try:
        arduino.open()
        with open(PORT_NAME,'w',encoding='utf-8') as f:
            f.write(puerto)
            f.close()
        datos = arduino.readline()
        datos1 = datos.decode("utf-8").rstrip("\r\n")
        datos2 = datos1.split(",")
        
        temperatura=datos2[0]
        humedad=datos2[1]
        lluvia=datos2[2]        
        print(datos2)

        tabla= pd.read_csv(dirBaseDatos.format("datos.csv"))
        if (not tabla.empty):
            tabla.drop(["Unnamed: 0"],axis=1,inplace=True)

        with open(NO_SERIE,'r') as f:
            password = f.readline()
            if password == "":
                with open(NO_SERIE,'w') as f:
                    caracteres=string.ascii_letters+string.digits
                    muestra=random.sample(caracteres,4)
                    password="".join(muestra)
                    f.write(password)
                    f.close()
            else:
                f.close()

        fecha=datetime.datetime.now()

        fecha1=fecha.strftime("%d/%m/%Y")

        hora=fecha.strftime("%H:%M:%S")

        nueva_fila={"S1:Temperatura":temperatura,"S2:Humedad":humedad,"No Serie":password,"Fecha":fecha1,"Hora":hora,"Lluvia":lluvia}

        tabla=tabla.append(nueva_fila,ignore_index=True)
        tabla.to_csv((dirBaseDatos).format("datos.csv",index=False))
        print("")
        print(tabla)
        arduino.close()
        
        return True
    except:
        return False

def escogerPuerto(arduino):
    ports = serial.tools.list_ports.comports()
    portList = []
    for port in ports:
        portList.append(port)
        print(str(port))
    puerto = 'COM'
    puerto += input('Escoja el COM')
    arduino.port = puerto
    Conectado = abrirPuerto(arduino,puerto)
    return Conectado

def main():
    arduino = serial.Serial()
    arduino.baudrate = 9600

    puerto = revisarArchivo()
    arduino.port = puerto
    if puerto != '':
        Conectado = abrirPuerto(arduino,puerto)
        if not Conectado:
            Conectado = escogerPuerto(arduino)
            if not Conectado:
                print("No se pudo conectar con el arduino")
    else:
        Conectado = escogerPuerto(arduino)
        if not Conectado:
            print("No se pudo conectar con el arduino")

if __name__ == "__main__":
    main()
