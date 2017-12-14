# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:34:17 2017

@author: hamch
"""

import tensorflow as tf
#Def 添加层+Matplotlib
def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))#矩阵大写
    baises=tf.Variable(tf.zeros([1,out_size])+0.01)#列表小写
    Wx_plus_b=tf.matmul(inputs,Weights)+baises
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

import numpy as np
x_data=np.linspace(-1,1,300)[:,np.newaxis]#加维--特征
noise=np.random.normal(0,0.05,x_data.shape)#正态分布
y_data=np.square(x_data)-0.5+noise

xs=tf.placeholder(tf.float32,[None,1])#x_data size
ys=tf.placeholder(tf.float32,[None,1])#y_data size

#隐藏层
layer1=add_layer(xs,1,10,activation_function=tf.nn.relu)
#输出层
prediction=add_layer(layer1,10,1,activation_function=None)
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
                   reduction_indices=[1]))#求误差总和求平均

train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)#学习效率
#important step--initialize
init=tf.initialize_all_variables()

import matplotlib.pyplot as plt       

sess=tf.Session()
sess.run(init)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)#subplot
ax.scatter(x_data,y_data)#散点
plt.ion
#plt.show
    
for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
     #print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        
        try:
            ax.lines.remove(lines[0])#去掉第一个lines单位
        except Exception:
            pass
        prediction_value=sess.run(prediction,feed_dict={xs:x_data})
        lines=ax.plot(x_data,prediction_value,'k-',lw=5)#曲线
        plt.pause(0.1)
            #plt.ion()#防止show的暂停
sess.close