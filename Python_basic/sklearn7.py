# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:18:59 2017

@author: hamch
"""

from sklearn import preprocessing
import numpy as np
a=np.array([[10,2.7,3.6],[-100,5,-2],[120,40,20]],
           dtype=np.float64)
print(a)
print(preprocessing.scale(a))#normalize

     
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt


x,y=make_classification(n_samples=300,n_features=2,n_redundant=0,
                        n_informative=2,random_state=22,n_clusters_per_class=1,
                        scale=100)
x=preprocessing.minmax_scale(x,feature_range=(-1,1))
X_train,X_test,Y_train,Y_test=train_test_split(
        x,y,test_size=0.3)
clf=SVC()
clf.fit(X_train,Y_train)
print(clf.score(X_test,Y_test))

plt.scatter(X_test[:,0],X_test[:,1],c=Y_test)
plt.show()

#交叉验证
from sklearn.cross_validation import cross_val_score
scores=cross_val_score(clf,x,y,cv=5,scoring='accuracy')#mean_squared_error
#cv 5次交叉验证
print(scores.mean())


