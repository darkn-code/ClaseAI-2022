import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

pd.__version__
dirBaseDatos="./basedatos/{}"

def main():
    data=pd.read_csv('./basedatos/salarios.csv')
    print(data.head(5))
    print(data.shape)

    x = data.iloc[:,:-1].values
    y = data.iloc[:,1].values
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
    print(x_train)

    regresion = LinearRegression()
    regresion.fit(x_train,y_train)

    plt.scatter(x_train,y_train,color='blue')
    plt.plot(x_train,regresion.predict(x_train),color='black')
    plt.title('Salario vs Exp')
    plt.xlabel('Exp')
    plt.ylabel('Salario')
    plt.show()

    plt.scatter(x_test,y_test,color='red')
    plt.plot(x_test,regresion.predict(x_test),color='black')
    plt.title('Salario vs Exp')
    plt.xlabel('Exp')
    plt.ylabel('Salario')
    plt.show()

    print(regresion.score(x_test,y_test))

if __name__ == "__main__":
    main()
    
