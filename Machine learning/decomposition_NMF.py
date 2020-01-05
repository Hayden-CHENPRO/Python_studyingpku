# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2020/1/2

from numpy.random import RandomState    # 加载RandomState用于创建随机数种子
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

n_row, n_col = 2, 3
n_components = n_row * n_col    # 设置图像展示时的排列情况
image_shape = (64, 64)    # 设置人脸数据图片的大小


###############################################################################
# Load faces data
dataset = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = dataset.data


###############################################################################
def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    plt.figure(figsize=(2. * n_col, 2.26 * n_row))    # 创建图片并指定图片大小（英寸）
    plt.suptitle(title, size=16)    # 设置标题及字号大小

    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)    # 选择画制的子图
        vmax = max(comp.max(), -comp.min())

        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray,    # 对数值归一化，并以灰度图形显示
                   interpolation='nearest', vmin=-vmax, vmax=vmax)
        plt.xticks(())
        plt.yticks(())    # 去除子图的坐标轴标签
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.94, 0.04, 0.)    # 对子图位置及间隔调整


plot_gallery("First centered Olivetti faces", faces[:n_components])
###############################################################################
# 创建特征提取的对象NMF，使用PCA作为对比，将它们存放在一个列表中
estimators = [
    ('Eigenfaces - PCA using randomized SVD',
     decomposition.PCA(n_components=6, whiten=True)),

    ('Non-negative components - NMF',
     decomposition.NMF(n_components=6, init='nndsvda', tol=5e-3))
]

###############################################################################

for name, estimator in estimators:    # 分别调用PCA和NMF
    print("Extracting the top %d %s..." % (n_components, name))
    print(faces.shape)
    estimator.fit(faces)    # 调用PCA或NMF提取特征
    components_ = estimator.components_    # 获取提取的特征
    plot_gallery(name, components_[:n_components])    # 按照固定格式进行排列

plt.show()