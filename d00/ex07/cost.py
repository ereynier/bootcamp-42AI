import numpy as np
from prediction import predict_

def cost_elem_(y, y_hat):
    y = y.reshape(y.shape[0], 1)
    y_hat = y_hat.reshape(y_hat.shape[0], 1)
    M = y.shape[0]
    J_elem = np.zeros((M, 1))
    for i in range(M):
        J_elem[i][0] = (1. / (2. * M)) * (y_hat[i][0] - y[i][0])**2
    return J_elem
    
def cost_(y, y_hat):
    y = y.reshape(y.shape[0], 1)
    y_hat = y_hat.reshape(y_hat.shape[0], 1)
    J_value = 0
    for i in range(y.shape[0]):
        J_value += (y_hat[i][0] - y[i][0])**2
    J_value = J_value / (2 * y.shape[0])
    return J_value

x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])

# Example 1:
out = cost_elem_(y1, y_hat1)
print(out)

# Example 2:
out = cost_(y1, y_hat1)
print(out)


x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
y_hat2 = predict_(x2, theta2)
y2 = np.array([[19.], [42.], [67.], [93.]])

# Example 3:
out = cost_elem_(y2, y_hat2)
print(out)

# Example 4:
out = cost_(y2, y_hat2)
print(out)

x3 = np.array([0, 15, -9, 7, 12, 3, -21])
theta3 = np.array([[0.], [1.]])
y_hat3 = predict_(x3, theta3)
y3 = np.array([2, 14, -13, 5, 12, 4, -19])


# Example 5:
out = cost_(y3, y_hat3)
print(out)

# Example 6:
out = cost_(y3, y3)
print(out)