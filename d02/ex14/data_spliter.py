import numpy as np


def data_spliter(x, y, proportion):
    shuffler = np.random.permutation(len(x))
    x_shuffled = x[shuffler]
    y_shuffled = y[shuffler]
    x_train, x_test = np.split(x_shuffled, [int(proportion*len(x))])
    y_train, y_test = np.split(y_shuffled, [int(proportion*len(x))])
    return(x_train, x_test, y_train, y_test)
