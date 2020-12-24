import numpy as np

def iterative_l2(theta):
    l2 = 0.
    for j in range(1, theta.shape[0]):
        l2 += theta[j]**2
    return (l2)

def l2(theta):
    theta[0] = 0
    return (float(np.dot(theta, theta)))



x = np.array([2, 14, -13, 5, 12, 4, -19])

# Example 1: 
print(iterative_l2(x))

# Example 2: 
print(l2(x))

y = np.array([3,0.5,-6])
# Example 3: 
print(iterative_l2(y))

# Example 4: 
print(l2(y))