import numpy as np
from mylinearregression import MyLinearRegression as MyLR
X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
Y = np.array([[23.], [48.], [218.]])
mylr = MyLR([[1.], [1.], [1.], [1.], [1]])

# Example 0:
print(mylr.predict_(X))

# Example 1:
print(mylr.cost_elem_(X,Y))

# Example 2:
print(mylr.cost_(X,Y))

# Example 3:
mylr.fit_(X, Y)
print(mylr.thetas)

# Example 4:
print(mylr.predict_(X))

# Example 5:
print(mylr.cost_elem_(X,Y))

# Example 6:
print(mylr.cost_(X,Y))