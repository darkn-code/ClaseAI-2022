import serial.tools.list_ports
import pandas as pd
import datetime
import random
import time

PORT_NAME = './Puertos/puertosAlejnadro.txt'
NO_SERIE = './Ubicacion/exterior.txt'
DATA_BASE = './basedatos/blockAlex.txt'
dirDataBase = "./basedatos/{}"

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

def revisarArchivo(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            puerto = f.readline()
#            print(puerto)
            f.close()
        return puerto
    except:
        return ''

def abrirPuerto(arduino,puerto,noserie):
    try:
        arduino.open()
        time.sleep(2)
        with open(PORT_NAME,'w',encoding='utf-8') as f:
            f.write(puerto)
            f.close()
        
        #tablaDatos = pd.read_csv(dirDataBase.format("datos.csv"))
        #if (not tablaDatos.empty):
        #    tablaDatos.drop(["Unnamed: 0"],axis=1,inplace=True)
        #tablaDatos.dropna(how="any",inplace=True)
        
        datos = arduino.readline()
        ct = datetime.datetime.now()
        ct.strftime("%d/%m/%y %H:%M:%S")
        datos = datos.decode('utf-8')
        tem = datos.split(',')[0]
        hum = datos.split(',')[1]
        dat = str(ct.date())
        #dat = dat.strftime("%d/%m/%Y")
        hou = str(ct.time())
        #hou = hoy.strftime("%H:%M:%S")
        luv = datos.split(',')[2]
        newData = tem + "," + hum + "," + noserie + "," + dat + "," + hou + "," + luv
        print(newData)
        print("lectura lista")
        with open(DATA_BASE,'a') as f:
            print("apexx")
            f.write(newData)
            print("anex")
            f.close()

        #tablaDatos = tablaDatos.append(newData,ignore_index=True)
        #print(tablaDatos)
        #tablaDatos.to_csv((dirDataBase).format("datos.csv",index=False))
        arduino.close()
    except:
        print("No se pudo conectar el Arduino")
        arduino.close()

def main():
    arduino = serial.Serial()
    arduino.baudrate = 115200

    cod = revisarArchivo(NO_SERIE)
    if cod != '':
        noserie = cod
    else:
        noserie = codeGen(10,False)
        with open(NO_SERIE,'w') as f:
            f.write(noserie)
            f.close()

    puerto = revisarArchivo(PORT_NAME)
    arduino.port=puerto

    if puerto != '':
        print(1)
        print(puerto)
        abrirPuerto(arduino,puerto,noserie)
    else:
        print(2)
        ports = serial.tools.list_ports.comports()
        portList = []
        for port in ports:
            portList.append(port)
            print(str(port))
        #arduino.port = 'COM6'
        puerto = '/dev/ttyUSB'
        puerto += input("Escoja el /dev/ttyUSB: ")
        arduino.port = puerto
        print(puerto)
        abrirPuerto(arduino,puerto,noserie)
        with open(PORT_NAME,'w', encoding='utf-8') as f:
            f.write(puerto)
            f.close()
#            f.write(puerto)
#            f.close()
if __name__ == '__main__':
    main()
