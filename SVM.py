from transaction import get_data
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
def SVM(data):
    model = LinearSVC()
    result = []
    (x_train, y_train), (x_test, y_test) = data
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    result.append(accuracy_score(y_test, y_pred.round()))
    print('SVM done')
    return result