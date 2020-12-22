import numpy as np

def simple_predict(x, theta):
    M = x.shape[0]
    N = x.shape[1]
    if (theta.reshape((theta.shape[0]), 1).shape != (N + 1, 1)):
        print("theta bad shape")
        return
    y_hat = np.array([])
    for i in range(M):
        tmp = theta[0]
        for j in range(N):
            tmp += theta[j + 1] * x[i][j]
        y_hat = np.append(y_hat, tmp)
    return(y_hat)


x = np.arange(1,13).reshape((4,3))

# Example 1:
theta1 = np.array([5, 0, 0, 0])
print(simple_predict(x, theta1))


# Example 2:
theta2 = np.array([0, 1, 0, 0])
print(simple_predict(x, theta2))


# Example 3:
theta3 = np.array([-1.5, 0.6, 2.3, 1.98])
print(simple_predict(x, theta3))



# Example 4:
theta4 = np.array([-3, 1, 2, 3.5])
print(simple_predict(x, theta4))