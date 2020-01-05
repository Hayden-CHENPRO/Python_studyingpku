# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2020/1/2

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()    # 以字典形式加载鸢尾花数据集
y = data.target    # 使用y表示数据集中的标签
x = data.data    # 使用x表示数据集中的属性数据
pca = PCA(n_components=2)    # 加载PCA算法，设置降维后主成分数目为2
reduced_x = pca.fit_transform(x)    # 对原始数据进行降维，保存在reduced_x中

# 按照类别对降维后的数据进行保存
red_x, red_y = [], []    # 第一二三类数据点
blue_x, blue_y = [], []
green_x, green_y = [], []

# 按照鸢尾花的类别将降维后的数据点保存在不同的列表中
for i in range(len(reduced_x)):
    if y[i] == 0:
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])
    else:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])

# 数据可视化
plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()