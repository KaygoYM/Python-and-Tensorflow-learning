# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 09:39:27 2017

@author: hamch
"""
#交叉验证
#from sklearn.learning_curve import learning_curve
from sklearn.learning_curve import validation_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

digits=load_digits()
x=digits.data
y=digits.target
#train_sizes,train_loss,test_loss=learning_curve(
#       SVC(gamma=0.001),x,y,cv=10,scoring='neg_mean_squared_error',
#           train_sizes=[0.1,0.25,0.5,0.75,1])
param_range=np.logspace(-6,-3,5)
train_loss,test_loss=validation_curve(
       SVC(),x,y,param_name='gamma',param_range=param_range,
          cv=10,scoring='neg_mean_squared_error',)
train_loss_mean=-np.mean(train_loss,axis=1)
test_loss_mean=-np.mean(test_loss,axis=1)
plt.plot(param_range,train_loss_mean,'o-',color='red',label="Training")
plt.plot(param_range,test_loss_mean,'o-',color='green',label="Cross-Validation")

plt.xlabel('gamma')
plt.ylabel('Loss')
plt.legend(loc='best')
plt.show()

clf=SVC(gamma=0.0002)
clf.fit(x,y)
#保存
#import pickle

from sklearn.externals import joblib
#save
joblib.dump(clf,'save/clf.pkl')
#restore
clf2=joblib.load('save/clf.pkl')
print(clf.predict(x[0:10]))