import numpy as np
from my_logistic_regression import MyLogisticRegression as MyLR
import matplotlib.pyplot as plt
X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
Y = np.array([[1], [0], [1]])
mylr = MyLR([2, 0.5, 7.1, -4.3, 2.09], 5e-3, 400000)

# Example 0:
print(mylr.predict_(X))

# Example 1:
print(mylr.cost_(X,Y))


# Example 2:
mylr.fit_(X, Y)
print(mylr.thetas)


# Example 3:
print(mylr.predict_(X))


# Example 4:
print(mylr.cost_(X,Y))

plt.scatter(X[:,0], Y)
plt.scatter(X[:,0], mylr.predict_(X))
plt.show()

plt.scatter(X[:,1], Y)
plt.scatter(X[:,1], mylr.predict_(X))
plt.show()

plt.scatter(X[:,2], Y)
plt.scatter(X[:,2], mylr.predict_(X))
plt.show()

plt.scatter(X[:,3], Y)
plt.scatter(X[:,3], mylr.predict_(X))
plt.show()