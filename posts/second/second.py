# 阻尼牛顿法
# 必须在cd 到子文件夹里
import sys
sys.path.append("..")
import numpy as np 
from normal_function import *
import math
import matplotlib.pyplot as plt
import 数值最优化.first.Linear_search as ls
class Newton:
    def __init__(self,f) -> None:
        self.f = f
        self.func = Function(f,10**-6)
        self.distance  = 0
    def cal_direction(self,val):
        grad = self.func.cal_Gra(val)
        hessian = self.func.cal_Hessian(val)
        # 判断函数是否为正定函数
        if np.all(np.linalg.eigvals(hessian)>0.1) == False :
            # 如果不是正定函数
            direction = -grad 
            print("velocity")
        else:
        # 如果是正定函数
            direction =  -grad.dot(np.linalg.inv(hessian))
            if direction.dot(grad) > 0.1:
                direction = -grad 
                print("velocity")
            print("newton")
        return direction
    def cal_distance(self,val):
        distance = ls.Armijo(val,self.cal_direction(val),self.f)
        return distance
    def cal_gra_dis(self,val):
        grad = self.func.cal_Gra(val)
        return math.sqrt(grad[0]**2+grad[1]**2)
    def damped_newton_method(self,val):
        epsilon = 10**-3
        iter = 0
        #画图
        x = np.linspace(-4,4,100)
        y = np.linspace(-4,4,100)
        X,Y = np.meshgrid(x,y)
        Z = self.f([X,Y])
        #等高线
        plt.contour(X,Y,Z,10)
        while(self.cal_gra_dis(val) > epsilon):
            print("第{0}次迭代".format(iter))
            direction = self.cal_direction(val)
            dis = self.cal_distance(val)
            print("移动距离为{0}".format(dis))
            val_next = val + dis*direction
            # 画线段
            x = [val[0],val_next[0]]
            y = [val[1],val_next[1]]
            plt.plot(x,y)
            val = val_next
            iter += 1
        plt.show()

    def newton_steepest_method(self,val):
        epsilon = 10**-3
        iter = 0
        #画图
        x = np.linspace(-4,4,100)
        y = np.linspace(-4,4,100)
        X,Y = np.meshgrid(x,y)
        Z = self.f([X,Y])
        #等高线
        plt.contour(X,Y,Z,50)
        while(self.cal_gra_dis(val)>epsilon):
            print("第{0}次迭代".format(iter))
            print("位置坐标{0},函数值{1}".format(val,self.f(val)))
            direction  = self.cal_direction(val)
            print(direction)
            dis = 0.1
            val_next = val+ dis*direction
            # 画线段
            x = [val[0],val_next[0]]
            y = [val[1],val_next[1]]
            plt.plot(x,y)
            val = val_next
            iter = iter+1 
        plt.show()
def f1(val):
    x1 = val[0]
    x2 = val[1]
    return 4*x1**2 + x2**2 -8*x1 -4*x2
def f2(val):
    x1 = val[0]
    x2 = val[1]
    return 4*x1**2 + x2**2- (x1**2)*x2
val1 = np.array([0,0])
val2 = np.array([2,0])
# newton = Newton(f1)
# newton.damped_newton_method(val1)
newton2 = Newton(f2)
newton2.newton_steepest_method(val2)