# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:29:29 2017

@author: hamch
"""

import matplotlib.pyplot as plt
import numpy as np
#Scatter
n=1024
x=np.random.normal(0,1,n)#正态分布
y=np.random.normal(0,1,n)
T=np.arctan2(y,x)#颜色--能量
plt.figure(1)
plt.title('Scatter')
plt.scatter(x,y,edgecolors='red',s=75,c=T,alpha=0.4)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(());plt.yticks(())
#Bar
m=12
X=np.arange(m)
Y1=(1-X/float(m))*np.random.uniform(0.5,1.0,m)
Y2=(1-X/float(m))*np.random.uniform(0.5,1.0,m)
plt.figure(2)
plt.title('Bar')
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='yellow')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='yellow')

for x,y in zip(X,Y1):
    plt.text(x+0.1,y+0.05,'%.2f' %y,
             ha='center',va='bottom')#对齐方式
for x,y in zip(X,Y2):
    plt.text(x+0.1,-y-0.05,'%.2f' %y,
             ha='center',va='top')#对齐方式


plt.xlim((-.5,m))
#plt.ylim((-1.25,1.25))
plt.xticks(());plt.yticks(())

#contours
def c(x,y):
    return(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
#height function
nn=256
xn=np.linspace(-3,3,n)
yn=np.linspace(-3,3,n)
Xn,Yn=np.meshgrid(xn,yn)
plt.figure(3);plt.title('Contours')
plt.contourf(Xn,Yn,c(Xn,Yn),8,alpha=0.75,
             cmap=plt.cm.hot)#10个分版 alpha透明度 cmap热源图
C=plt.contour(Xn,Yn,c(Xn,Yn),8,colors='black'
              ,linewidth='0.5')#等高线
plt.xticks(());plt.yticks(())
#adding label
plt.clabel(C,inline=True,fontsize=10)

#image
a=np.array([0.313666457689,0.423456009677,0.453215499009,
            0.984711177794,0.666666666666,0.124543895133,
            0.000155320097,0.888888312123,0.222222333333]).reshape(3,3)

plt.figure(4);plt.title('Image')
plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar()
plt.xticks(());plt.yticks(())


plt.show()