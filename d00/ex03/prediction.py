import numpy as np

def simple_predict(x, theta):
    if (x.ndim != 1 or theta.ndim != 1 or theta.size != 2):
        print("x or theta haven't the good format")
        return
    y = np.ndarray((0,1))
    for i in range(x.size):
        y = np.append(y, theta[0] + theta[1] * x[i])
    return(y)

x = np.arange(1,6)
theta1 = np.array([5, 0])
y = simple_predict(x, theta1)
print(y)

theta2 = np.array([0, 1])
y = simple_predict(x, theta2)
print(y)

theta3 = np.array([5, 3])
y = simple_predict(x, theta3)
print(y)

theta4 = np.array([-3, 1])
y = simple_predict(x, theta4)
print(y)