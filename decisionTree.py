from transaction import get_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
def DT(data):
    model = DecisionTreeClassifier()
    result = []
    (x_train, y_train), (x_test, y_test) = data
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    result.append(accuracy_score(y_test, y_pred.round()))
    print('decisionTree done')
    return result