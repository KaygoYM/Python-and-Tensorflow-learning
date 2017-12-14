#import
import time 
print(time.localtime())

import time as t #简称
print(t.time())

from time import time,localtime
l_t=localtime();print(l_t)

from time import *
print(time())

import learning18
print(list(filter(learning18.fun,range(20))))


#continue & break
while True:
    b=input('try to type something')
    if b=='1':
        break
    elif b=='2':
        print('another try')
        continue
    else:
        pass
    print('still in while')

print('Finish!')

#try
try:
    file=open('eeee.txt','r+')
except Exception as error:
    print(error)
    print('There is no file named as eeee')
    response=input('Do you want to create a new file? y/n')
    if response=='y':#字符串
        file=open('eeee.txt','w')
    else:
        pass
else:
    file.write('as you can')
    file.close()


#zip lambda map
list1=[1,2,4];list2=[6,7,99]
list(zip(list1,list2))#shell 输
#[(1, 6), (2, 7), (4, 99)]
#zip 合并 迭代器
for i,j in zip(list1,list2):
    print(i/2,j*2)
#list(zip(list1,list2,list2))

#lambda 简单定义操作、函数
fun2=lambda x,y:x+y
print(fun2(2,3))

#map 函数自变量赋值
def fun(x,y):
    return(x*y)

#map(fun,[1,2],[3,5])#object
print(list(map(fun,list1,list2)))#shell 输




#copy and deep copy
import copy
a=[1,2,3];b=a
print('id(a)=',id(a),'id(b)=',id(b))#硬盘索引
a[1]=22
print(b)
c=copy.copy(a)#shallow copy
print((id(a)==id(c)))

e=[1,2,[3,4]]
d=copy.copy(e)#shallow copy
print(id(d[2])==id(e[2]))#[3,4]索引一样，会随之变，其他位不变
e[2][0]=333
print(d)

f=copy.deepcopy(e)#deep copy
print(id(f[2])==id(e[2]))



#pickle存放数据
import pickle
dict={'da':111,2:[23,1,6],'23':{1:2,'d':'happy'}}

file=open('pickle_example.pickle','wb')
pickle.dump(dict,file)#倒入
file.close()

with open('pickle_example.pickle','rb') as file:#自动关闭
    a_dict1=pickle.load(file)
print(a_dict1)


#set去除重复
char_list=['a','b','c','c','d','d','d']
print(set(char_list))
print(type(set(char_list)))
sentence='Welcome Back to This Class'
print(set(sentence))

unique_char=set(char_list)
unique_char.add('x')#单独加
unique_char.remove('b')
#unique_char.discard('y')#避免报错
print(unique_char)
unique_char.clear()#清除

set1=set(char_list)#[a,b,c,d]
set2=['1','a','e','d']
print(set1.difference(set2))#2没有1有
print(set1.intersection(set2))#1,2交集

