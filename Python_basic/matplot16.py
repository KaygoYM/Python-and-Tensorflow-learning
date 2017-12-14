import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

x=np.linspace(1,10,100)

#method 1:subplot2grid
plt.figure()
ax1=plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
#3行3列单元小格,从左上角(0,0)开始,跨1行3列
ax1.plot(x,np.log(x))
ax1.set_title('Ax_figure1')#plt.title()

ax2=plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
ax2.plot(x,2*x+1)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax3.plot([0,1],[2,4],'r+')
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
ax5 = plt.subplot2grid((3, 3), (2, 1))
ax5.plot(x,2*x**2+2)
#method 2:gridspec
plt.figure()
gs=gridspec.GridSpec(3,3)#分格
ax6 = plt.subplot(gs[0, :])#占满第0行
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

#method 3:easy to define structure
f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=False)
ax11.plot(x,x**2,'m')

plt.tight_layout()
plt.show()
