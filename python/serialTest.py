import serial.tools.list_ports

PORT_NAME = 'puertos.txt'

def revisarArchivo():
    try:
        with open(PORT_NAME, 'r', encoding='utf-8') as f:
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
        print(datos.decode('utf-8').rstrip('\n'))
        arduino.close()
    except:
        print("No se pudo conectar el Arduino")


def main():
    arduino = serial.Serial()
    arduino.baudrate = 9600

    puerto = revisarArchivo()
    arduino.port=puerto
    if puerto != '':
        abrirPuerto(arduino,puerto)
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
        abrirPuerto(arduino,puerto)
    
if __name__ == '__main__':
    main()
