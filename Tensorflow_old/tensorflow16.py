# -*- coding: utf-8 -*-

#Classification
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#number 0-9 手写字符

mnist=input_data.read_data_sets('MNIST_data',one_hot=True)


def add_layer(inputs,in_size,out_size,activation_function=None):
    #add one more layer and return the output of this layer
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))#矩阵大写
    biases=tf.Variable(tf.zeros([1,out_size])+0.01)#列表小写
    Wx_plus_b=tf.matmul(inputs,Weights)+biases
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

def compute_accuracy(v_images,v_label):
    global prediction
    y_pre=sess.run(prediction,feed_dict={xs:v_images})#训练样本预测值
    correct_prediction=tf.equal(tf.argmax(y_pre,1),tf.argmax(v_label,1))#最大概率
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result=sess.run(accuracy,feed_dict={xs:v_images,ys:v_label})
    return result

#define placeholder for inputs to network    
xs = tf.placeholder(tf.float32, [None, 784]) # 28x28
ys = tf.placeholder(tf.float32,[None,10])

#add output layer
prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)#最简单的只有输入输出层
#softmax 分类用

#the error between prediction and real data
cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
#交叉熵用来衡量预测值和真实值的相似程度
train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)#学习效率

sess=tf.Session()
sess.run(tf.global_variables_initializer())

#start training
for i in range(1000):
    batch_xs,batch_ys=mnist.train.next_batch(100)#100个100个学习
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})
    
    if i%50==0:
        print(compute_accuracy(mnist.test.images,mnist.test.labels))
