import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

def plot_(x, y_real, y_hat, theta):
    plt.scatter(x, y_real, color='blue', label="Strue(pills)")
    plt.scatter(x, y_hat, color='green')
    plt.plot(x, y_hat, '--', color='green', label="Spredict(pills)")
    plt.grid(True, which='both', linestyle='-')
    plt.legend(loc="best")
    plt.xlabel("Quantity of blue pills (in micrograms)")
    plt.ylabel("Space drinving score")
    plt.show()


data = pd.read_csv("are_blue_pills_magics.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1,1)
Yscore = np.array(data["Score"]).reshape(-1,1)

linear_model1 = MyLR(np.array([[89.0], [-8]]))
linear_model2 = MyLR(np.array([[89.0], [-6]]),n_cycle=10)

linear_model1.fit_(Xpill, Yscore)
linear_model2.fit_(Xpill, Yscore)

plot_(Xpill, Yscore, linear_model1.predict_(Xpill), linear_model1.thetas)
plot_(Xpill, Yscore, linear_model2.predict_(Xpill), linear_model2.thetas)

'''
theta3 = np.arange(-23 * 2, 4 * 2)
linear_model3 = MyLR(np.array(-6, theta3[0]))
for j in range(78, 102,4):
	cost_array = np.array([])
	for i in range(-23 *2, 4 * 2):
		linear_model3.thetas = [j, i / 2]
		cost_array = np.append(cost_array, [linear_model3.cost_(Xpill, Yscore)])
	plt.plot(theta3 / 2, cost_array)
	print(np.min(cost_array), j / 2)
plt.xlim(-14,-4)
plt.ylim(10, 150)
plt.show()
'''