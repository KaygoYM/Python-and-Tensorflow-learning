#Tensorboard
import tensorflow as tf
import numpy as np
#Optimiazer


def add_layer(inputs,in_size,out_size,n_layer,activation_function=None):
    layer_name='layer%s'% n_layer
    #add one more layer and return the output of this layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights=tf.Variable(tf.random_normal([in_size,out_size]))#矩阵大写
            tf.summary.histogram(layer_name+'/weights',Weights)
        with tf.name_scope('biases'):
            biases=tf.Variable(tf.zeros([1,out_size])+0.01)#列表小写
            tf.summary.histogram(layer_name+'/biases',biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b=tf.matmul(inputs,Weights)+biases
        if activation_function is None:
            outputs=Wx_plus_b
        else:
            outputs=activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name+'/outputs',outputs)
        return outputs
    
#make some real data
x_data=np.linspace(-1,1,300,dtype=np.float32)[:,np.newaxis]
noise=np.random.normal(0,0.05,x_data.shape).astype(np.float32)
y_data=np.square(x_data)-0.5+noise

#define placeholder for inputs to network
with tf.name_scope('Inputs'):
    xs=tf.placeholder(tf.float32,[None,1],name='x_input')#x_data size
    ys=tf.placeholder(tf.float32,[None,1],name='y_input')#y_data size

#add hidden layer
layer1=add_layer(xs,1,10,n_layer=1,activation_function=tf.nn.relu)
#add output layer
prediction=add_layer(layer1,10,1,n_layer=2,activation_function=None)
#the error between prediction and real data
with tf.name_scope('Loss'):
    loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
                       reduction_indices=[1]))#求误差总和求平均
    tf.summary.scalar('loss',loss)
with tf.name_scope('Train'):
    train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)#学习效率

sess=tf.Session()
merged=tf.summary.merge_all()
writer=tf.summary.FileWriter("D:\Workspace\save",sess.graph)#tensorboard 观看框架(graph)
#important step
sess.run(tf.global_variables_initializer())

#start training
for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
        rs=sess.run(merged,feed_dict={xs:x_data,ys:y_data})
        writer.add_summary(rs,i)
writer.close
sess.close
