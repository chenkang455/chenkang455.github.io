# 粒子群算法
# 模拟鸟类的捕食行为 位置，速度
import random
import matplotlib.pyplot as plt
# 超参数设置
c1 = 1.5
c2 = 1.5
num = 100
w = 1
best_results = []  # 统计不同迭代次数最优结果
iter_num = 100
# 限制条件
max_px = 1
min_px = -1
max_py = 200
min_py = -200

# 计算 x^2 + y^2 的最小值

part_best_x = [1 for i in range(num)]
part_best_y = [1 for i in range(num)]
part_best_result = [1 for i in range(num)]


def gen_num(number, p_min, p_max, v_min, v_max):
    x = []
    y = []
    results = []
    vx = []
    vy = []
    for i in range(number):
        x.append(p_min+random.random()*(p_max-p_min))
        y.append(p_min+random.random()*(p_max-p_min))
        results.append(1-x[i]*pow(2.718,-x[i]*x[i]))
        vx.append(v_min+random.random()*(v_max-v_min))
        vy.append(v_min+random.random()*(v_max-v_min))
    return x, y, results, vx, vy


# 初始随机操作
x, y, results, vx, vy = gen_num(num, -200, 200, -5, 5)

for iter in range(iter_num):
    w = 0.99*w
    # 位置更新
    for i in range(num):
        x[i] += vx[i]
        y[i] += vy[i]
        results[i] = pow(x[i], 2)+pow(y[i], 2) + 2*x[i]
    # 全局分析
    best_result = min(results)
    glo_best_x = x[results.index(min(results))]
    glo_best_y = y[results.index(min(results))]
    best_results.append(best_result)
    # 局部分析
    for i in range(num):
        if(part_best_result[i] > results[i]):
            part_best_x[i] = x[i]
            part_best_y[i] = y[i]
            part_best_result[i] = results[i]
    # 更新
    for i in range(num):
        vx[i] = vx[i]*w + c1*(glo_best_x - x[i]) + c2*(part_best_x[i] - x[i])
        vy[i] = vy[i]*w + c1*(glo_best_y - y[i]) + c2*(part_best_y[i] - y[i])

    # 限制
    for i in range(num):
        x[i] = max_px if x[i] > max_px else x[i]
        x[i] = min_px if x[i] < min_px else x[i]

        y[i] = max_py if y[i] > max_py else y[i]
        y[i] = min_py if y[i] < min_py else y[i]
print(best_results)
plt.plot(best_results)
plt.show()
