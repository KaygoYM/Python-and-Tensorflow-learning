# -*- coding: utf-8 -*-
"""
@author: hamch
"""

#CNN卷积神经网络
#结构如下
#IMAGE-CONVOLUTION-MAX.POOLING-CONVOLUTION-MAX.POOLING-FULLY.CONNECTED-FULLY.CONNECTED-CLASSIFIER
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#number 0-9
mnist=input_data.read_data_sets('MNIST_data',one_hot=True)
#准备工作
def compute_accuracy(v_images,v_label):
    global prediction
    y_pre=sess.run(prediction,feed_dict={xs:v_images,keep_prob:1})#训练样本预测值
    correct_prediction=tf.equal(tf.argmax(y_pre,1),tf.argmax(v_label,1))#最大概率
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result=sess.run(accuracy,feed_dict={xs:v_images,ys:v_label,keep_prob:1})
    return result

def weight_variable(shape): 
	initial=tf.truncated_normal(shape,stddev=0.1)#定义Weight变量，输入shape，返回变量的参数
    #随机变量正态分布初始化
    #normal_distribution
	return tf.Variable(initial)
def bias_variable(shape): 
	initial=tf.constant(0.1,shape=shape) 
	return tf.Variable(initial)
def conv2d(x,W):
    #strides=[1,x_movement,y_movement,1]
	return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
#定义卷积，tf.nn.conv2d函数是tensoflow里面的二维的卷积函数，
#x是图片的所有参数，W是此卷积层的权重，
#然后定义步长strides=[1,1,1,1]值，strides[0]和strides[3]的两个1是默认值，中间两个1代表padding时在x方向运动一步，y方向运动一步，
#padding采用的方式是SAME。
def max_pool_2x2(x): 
	return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
#padding时我们选的是一次一步
#池化的核函数大小为2x2，因此ksize=[1,2,2,1]
xs=tf.placeholder(tf.float32,[None,784])#28*28
ys=tf.placeholder(tf.float32,[None,10])
keep_prob=tf.placeholder(tf.float32)
x_image=tf.reshape(xs,[-1,28,28,1])
#-1代表先不考虑输入的图片例子多少这个维度，后面的1是channel的数量,黑白的=1，RGB图像=3。

#convolutional layer1 + max pooling;
W_conv1=weight_variable([5,5,1,32])
b_conv1=bias_variable([32])
#卷积核patch5x5，黑白channel=1，输出是32个featuremap
h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)#output size 28*28*32
h_pool1=max_pool_2x2(h_conv1)#层输出 output size 14*14*32

#convolutional layer2 + max pooling;
W_conv2=weight_variable([5,5,32,64])
#卷积核patch5x5，输入size=32，输出是64个featuremap
b_conv2=bias_variable([64])
#接着我们就可以定义卷积神经网络的第二个卷积层，这时的输出的大小就是14x14x64
h_conv2=tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)#output size 14*14*64
h_pool2=max_pool_2x2(h_conv2)#output size 7*7*64

#fully connected layer1 + dropout;
W_fc1=weight_variable([7*7*64,1024]) #输入size=h_pool2.shape
b_fc1=bias_variable([1024])#更高
h_pool2_flat=tf.reshape(h_pool2,[-1,7*7*64]) #展平

h_fc1=tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)#output size 1*1024
h_fc1_drop=tf.nn.dropout(h_fc1,keep_prob)
#fully connected layer2 to prediction.
W_fc2=weight_variable([1024,10])
b_fc2=bias_variable([10])
#预测输出
prediction=tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)

#loss
cross_entropy=tf.reduce_mean(
    -tf.reduce_sum(ys*tf.log(prediction),
    reduction_indices=[1]))
train_step=tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
#开始训练
sess=tf.Session()
sess.run(tf.global_variables_initializer())
saver=tf.train.Saver()

for i in range(100):
    batch_xs,batch_ys=mnist.train.next_batch(100)#100个100个学习
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys,keep_prob:0.5})
    if i%50==0:
        print(compute_accuracy(mnist.test.images,mnist.test.labels))#测试准确率

#Saver 保存模型
#save to files
save_path=saver.save(sess,"my_CNN/save_CNN.ckpt")        
print("Save to path: ", save_path)


# 先建立 W, b 的容器
#W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
#b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="biases")

# 这里不需要初始化步骤 init= tf.initialize_all_variables()

#saver = tf.train.Saver()
#with tf.Session() as sess:
    # 提取变量
 #   saver.restore(sess, "my_net/save_net.ckpt")
  #  print("weights:", sess.run(W))
   # print("biases:", sess.run(b))