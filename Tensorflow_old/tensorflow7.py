# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:47:20 2017

@author: hamch
"""

import tensorflow as tf
#变量
state=tf.Variable(0,name='counter')
new_state=tf.add(state,1)
update=tf.assign(state,new_state)

init=tf.global_variables_initializer()
with tf.Session() as sess2:
    sess2.run(init)
    for _ in range(3):
        sess2.run(update)
        print(sess2.run(state))
        
#Placeholder
input1=tf.placeholder(tf.float32,[2,2])#形式，内容随时以dictionary填
input2=tf.placeholder(tf.float32,[2,2])
output=tf.matmul(input1,input2)
with tf.Session()as sess:
    print(sess.run(output,feed_dict={input1:[[1,2],[3,4]],
                                     input2:[[2,3],[8,9]]}))