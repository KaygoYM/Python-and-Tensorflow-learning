#numpy
import numpy as np

A=np.arange(3,15).reshape((3,4));print('A=',A)
print(A[2])#行
print(A[2][3])
index=np.argmax(A);print(index)
print(A[1,1:3])
i=1
for column in A.T:#以行迭代
    print('column'+str(i)+'=',column)
    i+=1
i=1
for row in A:
    print('row'+str(i)+'=',row)
    i+=1

print(A.flatten())#变成序列
for item in A.flat:
    print(item)

ONE=np.array([1,1,1])
TWO=np.array([2,2,2])

CC=np.vstack((ONE,TWO));print('ONE,TWO S\'shape=',ONE.shape);print('CC\'s shape=',CC.shape)
print(CC)#上下合并
DD=np.hstack((ONE,TWO));print(DD)#左右合并

print(ONE[np.newaxis,:].T)


A=np.array([1,2,3])[:,np.newaxis]
B=np.array([4,5,6])[:,np.newaxis]
print(np.hstack((A,B,B)))
print(np.vstack((A,A,B)))

C=np.concatenate((A,B,B,A),axis=1)#axis=0.上下合并,axis=1.左右合并
print(C)

cc=np.split(C,2,axis=1);print(cc[0])
ccc=np.split(C,3,axis=0);print(ccc[1])
print(np.array_split(C,3,axis=1))#不等分割
print(np.vsplit(C,3))#上下分割
print(np.hsplit(C,2))#左右分割



#array's copy
a=np.arange(4)
b=a;c=a;d=b#a 就是 b c d，改变a，bcd一起改
a[0]=11
if b is a:
    print('b is connected with a')
    print('a and b=',a)
    d[1:3]=[22,33]
else:
    print('b is not connected with a')
    print('b=',b,'a=',a)
b=a.copy() #deep copy a改变,b不变
a[3]=44
if b is a:
    print('b is connected with a')
    print('a and b=',a)
else:
    print('b is not connected with a')
    print('b=',b,'a=',a)
