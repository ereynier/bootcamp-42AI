import numpy as np


def data_spliter(x, y, proportion):
    shuffler = np.random.permutation(len(x))
    x_shuffled = x[shuffler]
    y_shuffled = y[shuffler]
    x_train, x_test = np.split(x_shuffled, [int(proportion*len(x))])
    y_train, y_test = np.split(y_shuffled, [int(proportion*len(x))])
    return(x_train, x_test, y_train, y_test)


x1 = np.array([1, 42, 300, 10, 59])
y = np.array([0,1,0,1,0])

# Example 1:
print(data_spliter(x1, y, 0.8))

# Example 2:
print(data_spliter(x1, y, 0.5))

x2 = np.array([ [  1,  42],
                [300,  10],
                [ 59,   1],
                [300,  59],
                [ 10,  42]])
y = np.array([0,1,0,1,0])

# Example 3:
print(data_spliter(x2, y, 0.8))

# Example 4:
print(data_spliter(x2, y, 0.5))