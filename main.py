import matplotlib.pyplot as plt
from transaction import get_data
from linearRegression import LiR
from logisticRegression import LoR
from SVM import SVM
from decisionTree import DT

if __name__ == '__main__':
    models = ['linearRegression', 'logisticRegression', 'SVM', 'decisionTree']
    colors = ['r', 'g', 'b']
    for i in range(3):
        data = get_data()
        results = [LiR(data), LoR(data), SVM(data), DT(data)]
        plt.plot(models, results, color=colors[i])
    plt.title('Supervised Learning')
    plt.xlabel('models')
    plt.ylabel('accuracy')

    plt.show()


