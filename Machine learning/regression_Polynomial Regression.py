# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2020/1/3

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures    # 导入多项式特征构造模块

datasets_X = []
datasets_Y =[]
fr = open(r'C:\Users\怠惰的金枪小鱼干\Desktop\prices.txt', 'r')
lines = fr.readlines()
for line in lines:
    items = line.strip().split(',')
    datasets_X.append(int(items[0]))
    datasets_Y.append(int(items[1]))
length = len(datasets_X)
datasets_X = np.array(datasets_X).reshape([length, 1])    # 变成二维，以符合现行回归拟合函数输入参数的要求
datasets_Y = np.array(datasets_Y)

minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX, maxX).reshape(-1, 1)    # 以数据 dataset_X 的最大值和最小值为范围建立等差数列，方便后续画图

poly_reg = PolynomialFeatures(degree=2)    # degree=2 表示建立 datasets_X 的二次多项式特征 X_poly
X_ploy = poly_reg.fit_transform(datasets_X)
lin_reg_2 = linear_model.LinearRegression()    # 然后创建线性回归
lin_reg_2.fit(X_ploy, datasets_Y)    # 使用线性模型学习 x_poly 和 datasets_Y 之间的映射关系

plt.scatter(datasets_X, datasets_Y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')    # plot函数用来绘制回归线，此处建立了 X 的二次多项式特征
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
