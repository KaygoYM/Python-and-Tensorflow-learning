import matplotlib.pyplot as plt
import numpy as np
#图中图 plot in plot
fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# below are all percentage
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8    #相对于整个figure的百分比
ax1 = fig.add_axes([left, bottom, width, height])  # main axes
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

# different method to add axes
####################################
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')#y逆序
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

#plt.show()


#双y轴Sencondary-axis
x = np.arange(0, 10, 0.1)
y1 = 0.2 * x**2
y2 = 0.05* np.log(x)

fig,ax3 = plt.subplots()

ax4 = ax3.twinx()    # mirror the ax1
ax3.plot(x, y1, 'g-')
ax4.plot(x, y2, 'b-')

ax3.set_xlabel('X data')
ax3.set_ylabel('Y1 data', color='g')
ax4.set_ylabel('Y2 data', color='b')

plt.show()
