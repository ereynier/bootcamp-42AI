import numpy as np
from my_linear_regression import MyLinearRegression as MyLR

x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])

lr1 = MyLR([2, 0.7])

# Example 0.0:
print(lr1.predict_(x))

# Example 0.1:
print(lr1.cost_elem_(lr1.predict_(x),y))

# Example 0.2:
print(lr1.cost_(lr1.predict_(x),y))

# Example 1.0:
lr2 = MyLR([1, 1], 5e-8, 1500000)
print("EXEMPLE 2")

lr2.fit_(x, y)
print(lr2.thetas)

# Example 1.1:
print(lr2.predict_(x))

# Example 1.2:
print(lr2.cost_elem_(lr2.predict_(x),y))

# Example 1.3:
print(lr2.cost_(lr2.predict_(x),y))