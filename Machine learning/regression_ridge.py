# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2020/1/3
# 划分训练集和测试集那没看懂

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn import model_selection   # 加载交叉验证模块
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


df = pd.read_csv(r'C:\Users\怠惰的金枪小鱼干\Desktop\岭回归.csv')
data = np.array(df)
# plt.plot(data[:, 5])
# plt.show()
X = data[:, :5]    # 用于保存0-4维数据，即属性
y = data[:, 5]    # 用于保存第5维数据，即车流量
poly = PolynomialFeatures(6)    # 用于创建最高次数6次方的多项式特征（多次试验后确定的）
X = poly.fit_transform(X)    # X 为创建的多项式特征

# 划分训练集和测试集，test_size表示测试机的比例
train_set_X, test_set_X, train_set_y, test_set_y = model_selection.train_test_split(X, y, test_size=0.3, random_state=0)

clf = Ridge(alpha=1.0, fit_intercept=True)    # 创建岭回归实例
clf.fit(train_set_X, train_set_y)    # 调用fit函数使用训练集训练回归器
clf.score(test_set_X, test_set_y)    # 利用测试机计算回归曲线的拟合优度

# 画出拟合曲线
start, end = 200, 300    # 画一条200~300范围的拟合曲线
y_pre = clf.predict(X)    # 调用predict函数的拟合值
time = np.arange(start, end)
plt.plot(time,y[start:end],'b', label="real")    # 真实数据蓝色
plt.plot(time,y_pre[start:end],'r', label='predict')    # 拟合数据红色
plt.legend(loc='upper left')    # 设置图例的位置
plt.show()