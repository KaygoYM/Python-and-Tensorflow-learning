# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:34:32 2017

@author: hamch
"""

from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris()
iris_X=iris.data
iris_Y=iris.target

#print(iris_X[:2,:])
#print(iris_Y)

X_train,X_test,Y_train,Y_test=train_test_split(
        iris_X,iris_Y,test_size=0.3)
#print(y_train)

knn=KNeighborsClassifier()#K聚类
knn.fit(X_train,Y_train)
yout=knn.predict(X_test)
print(Y_test & yout)

from sklearn.linear_model import LinearRegression

loaded_data=datasets.load_boston()
data_X=loaded_data.data
data_Y=loaded_data.data
model=LinearRegression()
model.fit(data_X,data_Y)
print('x:')
print(model.predict(data_X[:4,:]))
print('y:')
print(data_Y[:4]);print('\n')

#print(model.coef_);print(model.intercept_)斜率截距
#print(model.get_params())参数
#print(model.score(data_X,data_Y))方差为评分标准

import matplotlib.pyplot as plt
x,y=datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=5)
plt.scatter(x,y)
plt.show()