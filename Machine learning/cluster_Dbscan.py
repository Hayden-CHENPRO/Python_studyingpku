# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2020/1/1

import numpy as np
from sklearn import metrics
import sklearn.cluster as skc
import matplotlib.pyplot as plt

mac2id = dict()
onlinetimes = []
f = open(r'C:\Users\怠惰的金枪小鱼干\Desktop\TestData.txt', 'r+', encoding="utf-8")
for line in f:
    mac = line.split(",")[2]
    onlinetime = int(line.split(",")[6])
    starttime = int(line.split(",")[4].split(" ")[1].split(":")[0])
    if mac not in mac2id:
        mac2id[mac] = len(onlinetimes)
        onlinetimes.append((starttime, onlinetime))
    else:
        onlinetimes[mac2id[mac]] = [(starttime, onlinetime)]
real_X = np.array(onlinetimes).reshape((-1, 2))


# 上网时间聚类
# X = real_X[:, 0:1]
# db = skc.DBSCAN(eps=0.01, min_samples=20).fit(X)    # 调用DBSCAN方法进行训练
# labels = db.labels_    # labels为每个数据的簇标签
# print("Labels:")
# print(labels)    # 打印数据被记上的标签
# ratio = len(labels[labels[:] == -1]) / len(labels)    # 计算标签为-1（即噪声数据）的比例
# print("Noise ratio:", format(ratio, '.2%'))
#
# n_cluster_ = len(set(labels)) - (1 if -1 in labels else 0)    # 计算簇的个数并打印，评价聚类效果
#
# print("Estimated number of clusters: %d" % n_cluster_)
# print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))
#
# for i in range(n_cluster_):    # 打印各簇标号以及各簇内数据
#     print("Cluster ", i, ":")
#     print(list(X[labels == i].flatten()))
#
# plt.hist(X, 24)


# 上网时长聚类
# X = np.log(1 + real_X[:, 1:])
# db = skc.DBSCAN(eps=0.14, min_samples=10).fit(X)
# labels = db.labels_
#
# print("Labels:")
# print(labels)
# ratio = len(labels[labels[:] == -1]) / len(labels)
# print("Noise ratio: ", format(ratio, '.2%'))
#
# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#
# print("Estimated number of cluster: %d" % n_clusters_)
# print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))
#
# for i in range(n_clusters_):
#     print("Cluster ", i, ":")
#     count = len(X[labels == i])    # 统计个数、均值、标准差
#     mean = np.mean(real_X[labels == i][:, 1])
#     std = np.std(real_X[labels == i][:, 1])
#     print("\t number of sample: ", count)
#     print("\t mean of sample  : ", format(mean, '.1f'))
#     print("\t std of sample   : ", format(std, '.1f'))
