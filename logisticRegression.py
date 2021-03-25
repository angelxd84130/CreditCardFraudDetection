from transaction import get_data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def LoR(data):
    model = LogisticRegression()
    result = []
    (x_train, y_train), (x_test, y_test) = data
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    result.append(accuracy_score(y_test, y_pred.round()))
    print('logisticRegression done')
    return result
