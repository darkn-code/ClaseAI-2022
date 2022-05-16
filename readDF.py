import numpy as np
import pandas as pd
from csv import writer

list=[10,5,2.5]

dirc = './{}'

with open('baseDatos.csv','a') as df:
	writerObject=writer(df)
	writerObject.writerow(list)
	df.close()

test = pd.read_csv(dirc.format('baseDatos.csv'))

print(test)

