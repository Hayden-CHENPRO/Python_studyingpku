# !/usr/bin/env python
# -*- Coding:utf-8 -*-
# Created by Hayden at 2019/12/31

import numpy as np
from sklearn.cluster import KMeans

def loadData(filePath):
    fr = open(filePath, 'r+')
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1, len(items))])
    # for i in range(1, len(items)):
    return  retData, retCityName    # retData用来存储城市的各项消费信息；retCityName用于存储城市名称


if __name__ == '__main__':
    data, cityName = loadData(r'C:\Users\怠惰的金枪小鱼干\Desktop\city.txt')
    km = KMeans(n_clusters=3)    # 聚类数为3, 创建实例；将城市按照消费水平聚类，消费水平相近的城市聚集在一类中
    # KMeans算法默认使用欧氏距离，且没有更改为其他距离计算方法的参数，只能修改模块源代码
    label = km.fit_predict(data)    # 调用fit_predict()方法进行计算簇中心以及为簇分配序号；label指聚类后各数据所属的标签
    # print(label)
    # print(km.cluster_centers_)
    expenses = np.sum(km.cluster_centers_, axis=1)    # 聚类中心点的数值加和，即平均消费水平
    # print(expenses)
    CityCluster = [[], [], []]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    for i in range(len(CityCluster)):
        print("Expenses: %.2f"%expenses[i])
        print(CityCluster[i])

