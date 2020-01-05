# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2020/1/3

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

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
X = np.arange(minX, maxX).reshape(-1, 1)    # 以数据dataset_X的最大值和最小值为范围建立等差数列，方便后续画图

linear = linear_model.LinearRegression()
linear.fit(datasets_X, datasets_Y)    # 拟合输入输出数据

print('Coefficients: ', linear.coef_)    # 查看回归方程系数
print('intercept: ', linear.intercept_)    # 查看回归方程截距

plt.scatter(datasets_X, datasets_Y, color='red')
plt.plot(X, linear.predict(X), color='blue')    # plot函数用来绘制回归线
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()