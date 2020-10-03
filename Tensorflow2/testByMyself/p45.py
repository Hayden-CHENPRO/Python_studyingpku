#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 10:40
# @Author  : chenlitao
# @File    : p45.py

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

# prepare data
x_data = datasets.load_iris().data
y_data = datasets.load_iris().target

np.random.seed(486)
np.random.shuffle(x_data)
np.random.seed(486)
np.random.shuffle(y_data)
tf.random.set_seed(486)

x_train = x_data[:-30]
y_train = y_data[:-30]
x_test = x_data[-30:]
y_test = y_data[-30:]

x_train = tf.cast(x_train, tf.float32)
x_test = tf.cast(x_test, tf.float32)

train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)


# model
w1 = tf.Variable(tf.random.truncated_normal([4,3], stddev=0.1, seed=1))
b1 = tf.Variable(tf.random.truncated_normal([3], stddev=0.1, seed=1))


# optimization algorithm
epoch = 500
lr = 0.1
loss_all = 0
train_loss_result = []
test_acc = []

for epoch in range(epoch):
    for step, (x_train, y_train) in enumerate(train_db):
        with tf.GradientTape() as tape:
            y = tf.matmul(x_train, w1) + b1
            y = tf.nn.softmax(y)
            y_ = tf.one_hot(y_train, depth=3)
            loss = tf.reduce_mean(tf.square(y_ - y))
            loss_all += loss.numpy()
        grads = tape.gradient(loss, [w1, b1])

        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])

    print("Epoch {}, loss {}". format(epoch, loss_all / 4))
    train_loss_result.append(loss_all / 4)
    loss_all = 0


    # test
    total_correct, total_number = 0, 0
    for x_test, y_test in test_db:
        y = tf.matmul(x_test, w1) + b1
        y = tf.nn.softmax(y)
        pred = tf.argmax(y, axis=1)
        pred = tf.cast(pred, dtype=y_test.dtype)
        correct = tf.cast(tf.equal(pred, y_test), dtype=tf.int32)
        correct = tf.reduce_sum(correct)
        total_correct += int(correct)
        total_number += x_test.shape[0]

    acc = total_correct / total_number
    test_acc.append(acc)
    print("--------------------------------------")


# plot graph
plt.title('Loss Function Curve')  # 图片标题
plt.xlabel('Epoch')  # x轴变量名称
plt.ylabel('Loss')  # y轴变量名称
plt.plot(train_loss_result, label="Loss")  # 逐点画出trian_loss_results值并连线，连线图标是Loss
plt.legend()  # 画出曲线图标
plt.show()  # 画出图像

# 绘制 Accuracy 曲线
plt.title('Acc Curve')  # 图片标题
plt.xlabel('Epoch')  # x轴变量名称
plt.ylabel('Acc')  # y轴变量名称
plt.plot(test_acc, label="$Accuracy$")  # 逐点画出test_acc值并连线，连线图标是Accuracy
plt.legend()
plt.show()













