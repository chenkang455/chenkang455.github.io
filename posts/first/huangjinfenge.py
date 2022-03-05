import matplotlib.pyplot as plt
import numpy as np

# define the function
def f(x):
    return 1-x*pow(2.718, -x*x)
# parameters define
left = 0
right = 1
gold_parameter = 0.618
# make graph
x_numbers = np.linspace(left, right, 1000)
y_numbers = [f(x) for x in x_numbers]
plt.plot(x_numbers, y_numbers)
iter = 0
# iteration 
while right - left > 0.01:
    length = right - left
    x1 = left + (1-gold_parameter)*length
    x2 = left + gold_parameter*length
    x = [x1, x2]
    y = [f(x1), f(x2)]
    plt.scatter(x, y)
    if f(x1) > f(x2):
        left = x1
    else:
        right = x2
    iter = iter + 1
print("共迭代{0}次，最终结果是{1}".format(iter, f(x1)))
plt.show()
