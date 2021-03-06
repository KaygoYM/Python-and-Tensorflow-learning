# -*- coding: utf-8 -*-
"""
@author: hamch
"""

#RNN循环神经网络
#LSTM RNN cell
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#this is data
mnist=input_data.read_data_sets('MNIST_data',one_hot=True)
tf.set_random_seed(1)   # set random seed

# hyperparameters
lr = 0.001                  # learning rate
training_iters = 100000     # train step 循环次数上限
batch_size = 128            # 自定义
n_inputs = 28               # MNIST data input (img shape: 28*28)
n_steps = 28                # time steps (input 28行)
n_hidden_units = 128        # neurons in hidden layer
n_classes = 10              # MNIST classes (0-9 digits)
# tf Graph input
x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_classes])

# 对 weights biases 初始值的定义
# dictionary
Weights = {
    # shape (28, 128)
    'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
    # shape (128, 10)
    'out': tf.Variable(tf.random_normal([n_hidden_units, n_classes]))
}
Biases = {
    # shape (128, )
    'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_units, ])),
    # shape (10, )
    'out': tf.Variable(tf.constant(0.1, shape=[n_classes, ]))
}

# RNN 主体
#  这个 RNN 总共有 3 个组成部分 ( input_layer, cell, output_layer). 首先我们先定义 input_layer:
def RNN(X, weights, biases):
    # 原始的 X 是 3 维数据, 我们需要把它变成 2 维数据才能使用 weights 的矩阵乘法
#=========hidden layer for input to cell============#
    # X ==> (128 batches * 28 steps, 28 inputs)
    X = tf.reshape(X, [-1, n_inputs]) #(128*28,28)
    # X_in = W*X + b
    X_in = tf.matmul(X, weights['in']) + biases['in']#(128*28,128)
    # X_in ==> (128 batches, 28 steps, 128 hidden) 换回3维
    X_in = tf.reshape(X_in, [-1, n_steps, n_hidden_units])
#======================cell=========================#
    with tf.variable_scope('lstm',reuse=True):
        lstm_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden_units, forget_bias=1.0, state_is_tuple=True)
        init_state = lstm_cell.zero_state(batch_size, dtype=tf.float32) # 初始化全零 state(元组)
        #对于 lstm 来说, state可被分为(c_state主线, h_state分线)
        outputs,final_state = tf.nn.dynamic_rnn(lstm_cell,X_in, initial_state=init_state, time_major=False)
        #outputs=每一步的output list            final_state=h_state    
#======hidden layer for output as the final result===========#
    #results = tf.matmul(final_state[1], weights['out']) + biases['out']#final_state[1]=outputs[-1] 最后一个output
    # or
    # 把 outputs 变成 列表 [(batch, outputs)..] * steps
    outputs = tf.unstack(tf.transpose(outputs, [1,0,2]))
    results = tf.matmul(outputs[-1], weights['out']) + biases['out']    #选取最后一个 output

    return results

pred = RNN(x,Weights,Biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=pred))
with tf.variable_scope('mini',reuse=None):
    train_op = tf.train.AdamOptimizer(lr).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

#============================开始训练RNN====================#
# init= tf.initialize_all_variables() # tf 马上就要废弃这种写法
# 替换成下面的写法:
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    step = 0
    while step * batch_size < training_iters:
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape([batch_size, n_steps, n_inputs])
        sess.run(train_op, feed_dict={
            x: batch_xs,
            y: batch_ys,
        })
        if step % 20 == 0:
            print(sess.run(accuracy, feed_dict={
            x: batch_xs,
            y: batch_ys,
        }))
        step += 1