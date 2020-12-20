import numpy as np
import matplotlib.pyplot as plt
from prediction import predict_
from vec_cost import cost_, cost_elem_

def plot_with_cost(x, y, theta):
    plt.scatter(x, y)
    y_hat = predict_(x, theta)
    J = cost_(y, y_hat)
    J_elem = cost_elem_(y, y_hat)
    plt.plot(x, y_hat, color='orange')
    plt.plot((x,x),(y,y_hat), 'r--')
    plt.title("Cost : %f" %J)
    plt.show()
    return

x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])

# Example 1:
theta1= np.array([18,-1])
plot_with_cost(x, y, theta1)

# Example 2:
theta2 = np.array([14, 0])
plot_with_cost(x, y, theta2)

# Example 3:
theta3 = np.array([12, 0.8])
plot_with_cost(x, y, theta3)