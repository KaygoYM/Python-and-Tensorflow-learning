# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:47:33 2017

@author: hamch
"""
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y=x**2
t=2*x+1

plt.figure(1)
#figsize=(8,5)
l1,=plt.plot(x,y,label='square')
l2,=plt.plot(x,t,color='red',linewidth=2.0,linestyle='-',
         label='linear')
#l1,l2与handle配合使用
#移动坐标轴位置
ax=plt.gca()#get current axis
ax.spines['right'].set_color('none')#去轴
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('outward',-1))#data,outward,axes
ax.spines['left'].set_position(('data',-0.25))

plt.legend(handles=[l1,l2],labels=('square_up','linear_up'),loc='best')#loc='upper right'

#ticks能见度
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='pink',edgecolor='None',
                        alpha=0.9))
    
#*******************************************************#

plt.figure(2)
plt.plot(x,t)
plt.xlim((-1,2))#取值范围
plt.ylim((-2,3))
plt.xlabel('X')
plt.ylabel('Y')
#单位
new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3]
            ,[r'$really\ bad$',r'$\alpha$',r'$normal$',r'$good$',r'$very\ good$'])

# $Times New Roman字体 r正则

#添加标注
#method1
x0=0.5;y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,-1],linestyle='--',color='k')
plt.annotate(r'$2x+1=%s$' %y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),
             textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

#method2
plt.text(-0.25,2,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \beta_t$',
         fontdict={'size':16,'color':'green'})
#i,t下标
plt.show()
