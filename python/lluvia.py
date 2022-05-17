import pandas as pd
import numpy as np
import random
import string
import datetime

dirBaseDatos="./BaseDatos/{}"

def main():
    tabla= pd.read_csv(dirBaseDatos.format("tarea.csv"))
    if (not tabla.empty):
        tabla.drop(["Unnamed: 0"],axis=1,inplace=True)
    temp=int(input("Introduzca la temperatura:  "))
    print("")

    humedad=int(input("Introduzca la humedad existente: "))
    print("")
   
    caracteres=string.ascii_letters+string.digits
    muestra=random.sample(caracteres,4)
    password="".join(muestra)
   
    fecha=datetime.datetime.now()

    fecha1=fecha.strftime("%d/%m/%Y")
   
    hora=fecha.strftime("%H:%M:%S")
   
    lluvia=random.choice(["Sí","No"])
   
    nueva_fila={"S1:Temperatura":temp,"S2:Humedad":humedad,"No Serie":password,"Fecha":fecha1,"Hora":hora,"Lluvia":lluvia}
   
    tabla=tabla.append(nueva_fila,ignore_index=True)
    tabla.to_csv((dirBaseDatos).format("tarea.csv",index=False))
    print("")
    print(tabla)

if __name__=="__main__":
    main()
