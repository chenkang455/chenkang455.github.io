import matplotlib.pyplot as plt
import numpy as np
# calculate the result
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
def f(x):
    x1 = x[0]
    x2 = x[1]
    return 100*(x2-x1*x1)*(x2-x1*x1)+(1-x1)*(1-x1)

# 3d-plot
def plot_function(f):
    fig = plt.figure()
    x1 = np.outer(np.linspace(-2, 2, 30), np.ones(30))
    x2 = x1.copy().T
    ax = fig.add_subplot(111, projection='3d')
    z1 = 100*(x2-x1*x1)*(x2-x1*x1)+(1-x1)*(1-x1)
    ax.plot_surface(x1, x2, z1, cmap='viridis', edgecolor='none')
    plt.show()
# calculate the gradient

def cal_gra(f, x):
    x1 = x[0]
    x2 = x[1]
    delta = 0.0001
    dx1 = (f([x1+delta, x2])-f([x1, x2])) / delta
    dx2 = (f([x1, x2+delta])-f([x1, x2]))/delta
    return np.array([dx1, dx2])
def Armijo(x,direction,f):
    '''
    x: position
    direction: moving direction
    f: function
    '''    
    # define parameters
    rou = 0.6  
    dis = 1  # define the moving distance
    beta = 0.5  # define the constant moving distance
    iter = 1 # define iter times
    iter_max = 20
    print("原位置为({0},{1}),函数值为{2}".format(x[0],x[1],f(x)))
    if f(x + direction * dis) <= f(x) + rou * dis * cal_gra(f, x).dot( direction):
        dis = 1
    else:
        dis = beta 
        while iter < iter_max:
            if f(x + direction * dis) <= f(x) + rou * dis * cal_gra(f, x).dot( direction):
                break
            dis = dis * rou   #! update formula
            iter = iter + 1
    x = x + dis * direction
    print("现位置为({0},{1}),函数值为{2}".format(x[0],x[1],f(x)))
    
    return dis
if __name__ == "__main__":
    x = np.array([1, -1])  # position
    direction = np.array([0, 1])
    print("搜索步长为{}".format(Armijo(x,direction,f)))
    plot_function(f)

