import matplotlib.pyplot as plt
import numpy as np
xs = np.linspace(0,1,100)
y = []
def func(x):
    return 1-x*pow(2.718,-2*x*x)
for x in xs:
    y.append(func(x))
print(y)
plt.plot(y)
plt.show()