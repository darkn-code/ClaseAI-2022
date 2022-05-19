import serial.tools.list_ports
import pandas as pd
import numpy as np
import random
import string
import datetime

dirBaseDatos="./BaseDatos/{}"

PORT_NAME = './Puertos/puerto.txt'
NO_SERIE = './Ubicacion/invernadero.txt'

def revisarArchivo():
    try:
        with open(Port_NAME, 'r', encoding='utf-8') as f:
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

                data = arduino.readline()
                data2 = data.decode(utf-8).rstrip("\r\n")
                data3 = data2.split(",")

                temp=data3[0]
                hum=data3[1]
                lluv=data3[2]

            tabla= pd.read_csv(dirBaseDatos.format("datos.csv"))
            if (not tabla.empty):
                tabla.drop(["Unnamed: 0"],axis=1,inplace=True)

            with open(NO_SERIE,'r') as f:
                password = f.readline()
                if password == "":
                    with open(NO_SERIE,'w') as f:
                        caracters=string.ascii_letters+string.digits
                        muestra=ramdom.sample(caracters,4)
                        password="".join(muestra)
                        f.write(password)
                        f.close()
                    else:
                        f.close()

                fecha=datetime.datetime.now()
                fecha2=fecha.strftime("%d,%m,%Y")
                hora=fecha.strftime("%H:%M:%S")

                filacreada=("S1:Temperatura":temp,"S2:Humedad":hum,"No serie",password,"Fecha",fecha2,"Hora",hora,"lluv":lluvia)
                tabla=tabla.append(filacreada,ignore_index=True)
                tabla.to_csv((dirBaseDatos).format("datos.csv",index+False))
                print("")
                print(tabla)
                arduino.close()

                return True
            except:
                return False



    def main():
        arduino = serial.Serial()
        arduino.baudrate = 9600

        puerto = revisarArchivo()
        arduino.port = puerto
        if puerto !='':
            abrirPuerto(arduino,puerto)
        else:
            ports = serial.tools.list_ports.comports()
            portList = []
            for port in ports:
                portList.append(port)
                print(str(port))
            puerto = 'COM'
            puerto += input('Escoja el COM')
            arduino.port = puerto
            abrirPuerto(arduino,puerto)

if __name__ == '__main__':
    main()

