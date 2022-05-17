import numpy as np
import pandas as pd

dirBaseDatos="../BaseDatos/{}"

datos={"S1:Temperatura":[],
        "S2:Humedad":[],
        "No Serie":[],
        "Fecha":[],
        "Hora":[],
        "Lluvia":[]
        }
df=pd.DataFrame(datos)
print(df)

df.to_csv((dirBaseDatos).format("datos.csv"),index=False)
