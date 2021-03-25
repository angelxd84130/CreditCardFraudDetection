# data preprocessing
import pandas as pd
import numpy as np

df = pd.read_csv("creditcard.csv")
X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

def get_data():
    # split training and testing data
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1000)
    return (x_train, y_train), (x_test, y_test)