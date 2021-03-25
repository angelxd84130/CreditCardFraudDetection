from transaction import get_data
from keras import Sequential
from keras.layers.core import Dense, Dropout
from keras.layers import Embedding
from keras.layers.recurrent import SimpleRNN
from sklearn.metrics import accuracy_score
def RNN():
    model = Sequential()
    result = []
    (x_train, y_train), (x_test, y_test) = get_data()
    model.add(Embedding(output_dim=32, input_dim=x_train.shape[0], input_length=x_train.shape[1]))
    model.add(Dropout(0.25))
    model.add(SimpleRNN(units=32))
    model.add(Dense(units=256, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=30, epochs=1, verbose=2, validation_split=0.2)
    y_pred = model.predict_classes(x_test)
    result.append(accuracy_score(y_test, y_pred))

    print('RNN done')
    return result

#print(RNN())
