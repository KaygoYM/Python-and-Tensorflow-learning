# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:14:07 2017

@author: hamch
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=Axes3D(fig)
x=np.arange(-4,4,0.25)
y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(x,y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
#rstride跨度
ax.contourf(X,Y,Z,zdir='z',offset=-1,cmap='rainbow')
#plt.show()

#Subplot
#可以纠结的subplot
plt.figure()
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])
plt.subplot(235)
plt.plot([0,1],[0,4])
plt.subplot(236)
plt.plot([0,1],[2,4])
plt.show()
