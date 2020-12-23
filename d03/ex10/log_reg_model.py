import numpy as np
from my_logistic_regression import MyLogisticRegression as MyLR
import pandas as pd
from data_spliter import data_spliter
import matplotlib.pyplot as plt
'''
def select_cat(y, cat):
    new_y = y.copy()
    other_cat = np.unique(new_y)
    # Remvoving `category` from other_cat
    other_cat = other_cat[other_cat != cat]

    # Selecting element
    to_0 = np.isin(new_y, other_cat)
    to_1 = new_y == cat

    # Changing there values
    new_y[to_0] = 0
    new_y[to_1] = 1

    return new_y


data1 = pd.read_csv("solar_system_census_planets.csv")
data2 = pd.read_csv("solar_system_census.csv", index_col=0)

y = np.array(data1[["Origin"]])
x = np.array(data2)
x = (x - np.mean(x)) / np.std(x)

x_train, x_test, y_train, y_test = data_spliter(x,y, 0.7)

y_train = select_cat(y_train, 0)
y_test = select_cat(y_test, 0)
lr0 = MyLR([[1.], [1.], [1.], [1.]], 1e-4, 50000)
plt.scatter(x_train[:,0], y_train)
plt.scatter(x_train[:,0], lr0.predict_(x_train))
plt.show()
print(lr0.cost_(x_train, y_train))
print(lr0.cost_(x_test, y_test))
y_hat, hist = lr0.fit_(x_train, y_train)
plt.scatter(x_train[:,0], y_train)
plt.scatter(x_train[:,0], lr0.predict_(x_train))
plt.show()
print(lr0.cost_(x_train, y_train))
print(lr0.cost_(x_test, y_test))
plt.plot(np.arange(50000), hist)
plt.show()


'''



def select_cat(y, cat):
    new_y = y.copy()
    other_cat = np.unique(new_y)
    # Remvoving `category` from other_cat
    other_cat = other_cat[other_cat != cat]

    # Selecting element
    to_0 = np.isin(new_y, other_cat)
    to_1 = new_y == cat

    # Changing there values
    new_y[to_0] = 0
    new_y[to_1] = 1

    return new_y

def train(x, y, cat, theta=None):
    if theta is None:
        theta = [[8.], [-0.],[-0.], [3.]]
    y_prime = select_cat(y, cat)
    lr = MyLR(theta, 1e-2, n_cycle=10000)
    plt.scatter(x[:,0], lr.predict_(x),color="blue")
    lr.fit_(x, y_prime)
    plt.scatter(x[:,0], y_prime,color="green")
    plt.scatter(x[:,0], lr.predict_(x), color="lightblue")
    plt.show()
    return lr

def predict_one_vs_all(lr_lst, cat_lst, x):
    y_hat_lst = [lr.predict_(x) for lr in lr_lst]

    idx = np.argmax(np.concatenate(y_hat_lst, axis=1), axis=1)
    return cat_lst[idx].reshape(-1, 1)

def remap(y_train, a):
    y_remap = np.array(y_train)
    for i in range(y_remap.shape[0]):
        if y_remap[i] != a:
            y_remap[i] = 0
        else:
            y_remap[i] = 1
    return(y_remap)


data1 = pd.read_csv("solar_system_census_planets.csv")
data2 = pd.read_csv("solar_system_census.csv", index_col=0)

y = np.array(data1[["Origin"]])
x = np.array(data2)
x = (x - np.mean(x)) / np.std(x)

x_train, x_test, y_train, y_test = data_spliter(x,y, 0.7)

lr0 = train(x_train, y_train, 0)
lr1 = train(x_train, y_train, 1)
lr2 = train(x_train, y_train, 2)
lr3 = train(x_train, y_train, 3)

y_hat = predict_one_vs_all([lr0, lr1, lr2, lr3], np.array([0., 1., 2., 3.]), x_test)
print(y_hat)
unique, counts = np.unique(y_hat == y_test, return_counts=True)
print(dict(zip(unique, counts)))

plt.scatter(x_test[:,0], y_test)
plt.scatter(x_test[:,0], y_hat)
plt.show()