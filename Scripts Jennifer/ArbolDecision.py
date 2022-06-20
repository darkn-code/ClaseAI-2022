import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import re
from sklearn import tree
from sklearn.model_selection import train_test_split
sns.set()
from sklearn import preprocessing

dirBaseDatos="./basedatos/{}"
def main():
    train_df = pd.read_csv('./basedatos/titanic-train.csv')
    test_df = pd.read_csv('./basedatos/titanic-test.csv')

    print(train_df.head())
    print(train_df.shape)

    train_df.Sex.value_counts().plot(kind='bar',color=['b','r'])
    plt.title('Distribucion de sobrevivientes')
    plt.show()

    label_encoder = preprocessing.LabelEncoder()

    encoder_sex = label_encoder.fit_transform(train_df['Sex'])

    train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
    train_df['Embarked'] = train_df['Embarked'].fillna('S')

    train_predictors = train_df.drop(['PassengerId','Survived','Name','Ticket','Cabin'],axis=1)
    categorical_cols = [cname for cname in train_predictors.columns if train_predictors[cname].nunique() < 10 and train_predictors[cname].dtype == 'object']
    numerical_cols = [cname for cname in train_predictors.columns if train_predictors[cname].dtype in ['int64','float64']]

    my_cols = categorical_cols + numerical_cols
    train_predictors = train_predictors[my_cols]

    dummy_encoded_train_predictors = pd.get_dummies(train_predictors)

    y_target = train_df['Survived'].values
    x = dummy_encoded_train_predictors

    x_train, x_val, y_train, y_val = train_test_split(x,y_target, test_size=.25,random_state=0)

    arbol = tree.DecisionTreeClassifier()
    arbol = arbol.fit(x,y_target)

    arbol_exactitud= round(arbol.score(x,y_target),4)
    print('Accuracy: %0.4f' % (arbol_exactitud))

if __name__ == "__main__":
    main()
