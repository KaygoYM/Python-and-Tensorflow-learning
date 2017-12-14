# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
import numpy as np
#create data
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.4

#create tensorflow structure start
weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros([1]))

y=weights*x_data+biases#预测值
error=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(error)
#create tensorflow structure end

init=tf.initialize_all_variables()

sess=tf.Session()
sess.run(init)#激活Very important
#Session 会话控制
for step in range(1,201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(weights),sess.run(biases))
        
        
matrix1=tf.constant([[3,3],
                     [4,5],
                     [8,9]])
matrix2=tf.constant([[2,5,6],
                     [4,1,9]])
m1=np.array([[3,3],
             [4,5],
             [8,9]])
m2=np.array([[2,5,6],
             [4,1,9]])
product=tf.matmul(matrix1,matrix2)#matrix multiply
product_n=np.dot(m1,m2)
print("the numpy result",product_n)
print("the tf result",sess.run(product))
sess.close()

#with tf.Session() as sess:
#result2=sess.run(product)
#print(result2)
