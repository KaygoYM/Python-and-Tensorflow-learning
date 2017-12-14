#matrix array numpy
import numpy as np

my_mat=np.array([[12,56,2],
                 [5,32,66],
                 [89,15,4]],dtype=np.float)

print(my_mat)
print(my_mat.dtype)
print('number of dim:',my_mat.ndim)
print('shape:',my_mat.shape)
print('size:',my_mat.size)

a=np.zeros((3,2),dtype=np.int)#ones
print('a=',a)

b=np.empty((4,5));print('b=',b)
c=np.arange(10,22,1).reshape((3,4));print('c=',c)
d=np.arange(12).reshape((3,4));print('d=',d)

e=np.linspace(1,10,4).reshape((2,2));print('e=',e,'e shape=',e.shape)

cc=d-c#逐减
print('d-c=',cc)
cc=d**2#逐平方
print('d^2=',cc)
cc=10*np.sin(d);print('10sin(d)=',cc)

print(d)
print(d<=3)

dd=d.reshape((4,3));print(dd);
cc=np.dot(c,dd);print('d\'*c=',cc)#cc=c.dot(dd)

aa=np.random.random((2,4))
#np.sum();np.min();np.max()
print(aa,np.sum(aa),np.min(aa),np.max(aa))
print(np.sum(aa,axis=1))#行求和
print(np.sum(aa,axis=0))
print(np.min(aa,axis=1))


A=np.arange(2,14).reshape((3,4))
print('A=',A)

print(np.argmin(A))#最小值索引
print(np.argmax(A))
print(np.average(A))#平均值A.mean()
print(A.mean())#np.mean(A)
print(np.median(A))#中位数

print(np.cumsum(A))#累加
print(np.diff(A))#累差，差分
[index1,index2]=np.nonzero(A)#返回非零的行列位置
print(index1);print(index2)
print(np.sort(A))#逐行排序

print(A.T)#转置
print(np.diag(A.dot(A.T)))#返回对角线元素
print(np.trace(A.dot(A.T)))#求迹

print(np.clip(A,5,9))#<5强制置5，>9强制置9






