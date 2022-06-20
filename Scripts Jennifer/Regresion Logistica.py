import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns


dirBaseDatos="./basedatos/{}"

def main():
    diabetes = pd.read_csv("./basedatos/diabetes.csv")
    diabetes.head()

    print(diabetes.shape)
    carc_cols = ['Pregnancies','Insulin','BMI','Age','Glucose','BloodPressure','DiabetesPedigreeFunction']
    x = diabetes[carc_cols]
    y = diabetes.Outcome

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)
    logreg = LogisticRegression()
    logreg.fit(x_train,y_train)
    y_pred = logreg.predict(x_test)

    print(y_pred)

    cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
    print(cnf_matrix)

    class_names = [0,1]
    fig,ax = plt.subplots()
    tick_mark = np.arange(len(class_names))
    plt.xticks(tick_mark,class_names)
    plt.yticks(tick_mark,class_names)

    sns.heatmap(pd.DataFrame(cnf_matrix),annot=True,cmap="Blues_r",fmt="g")
    ax.xaxis.set_label_position("top")
    plt.tight_layout()
    plt.title("Matriz Confusión",y=1.1)
    plt.ylabel("Etiqueta actual")
    plt.xlabel("Etiqueta predicción")
    plt.show()

    print("Exactitud: ",metrics.accuracy_score(y_test,y_pred))

if __name__ == "__main__":
    main()





   