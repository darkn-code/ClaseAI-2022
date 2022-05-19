import serial.tools.list_ports
import time

PORT_NAME = './Puertos/puertos.txt'

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
        time.sleep(1)
        with open(PORT_NAME,'w',encoding='utf-8') as f:
            f.write(puerto)
            f.close()
        datos = arduino.readline()
        print(datos.decode('utf-8').rstrip('\n'))
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
    puerto = '/dev/ttyACM'
    puerto += str(input('Escoga el /dev/ttyACM'))
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

    

if __name__ == '__main__':
    main()
