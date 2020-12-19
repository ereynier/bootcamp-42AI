import numpy as np
import matplotlib.pyplot as plt
from prediction import predict_
from tools import add_intercept

def plot(x, y, theta):
    plt.scatter(x, y)
    h = predict_(x, theta)
    plt.plot(x, h)
    plt.show()


x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

theta1 = np.array([4.5, -0.2])
print(x)
plot(x, y, theta1)

theta2 = np.array([-1.5, 2])
plot(x, y, theta2)

theta2 = np.array([3, 0.3])
plot(x, y, theta2)