import numpy as np
class Function:
    def __init__(self,f,delta) -> None:
        self.delta = delta 
        self.f = f
    def cal_val(self,val):
        return self.f(val)
    #求偏导
    def part_1(self,index,val):
        #! 不改变原值
        val = list(val)
        # 原函数值
        f1 = self.f(val)
        val [index] += self.delta
        # 自变量改变delta后的函数值
        f2 = self.f(val)
        return (f2 - f1)/self.delta
    #求二阶导
    def part_2(self,index1,index2,val):
        #! 不改变原值
        val = list(val)
        f1 = self.part_1(index1,val)
        val [index2] += self.delta
        f2 = self.part_1(index1,val)
        return (f2-f1)/self.delta
    #求梯度
    def cal_Gra(self,val):
        if len(list(val)) == 1 :
            return self.part_1(0,val)
        elif len(list(val)) == 2:
            return np.array([self.part_1(0,val),self.part_1(1,val)])
    def cal_Hessian(self,val):
        dim = len(val)
        mat = np.zeros((dim,dim))
        for i in range(dim):
            for j in range(dim):
                mat[i,j] = self.part_2(i,j,val)
        return mat
def test_f(val):
    x1 = val[0]
    x2 = val[1]
    return x1**2 + x2**2 + 2*x1*x2
if __name__ =="__main__":
    delta = 10**-6
    val =  [3,1]
    func = Function(test_f,delta)
    print(func.cal_val(val))

