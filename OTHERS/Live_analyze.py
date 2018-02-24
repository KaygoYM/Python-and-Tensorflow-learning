# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:11:17 2018

@author: KAI
"""

import numpy as np
from sklearn.preprocessing import MinMaxScaler
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.mllib.clustering import KMeans
import matplotlib.pyplot as plt
import matplotlib as mlp
from itertools import combinations as comb

mlp.rcParams['font.family']='sans-serif'  
mlp.rcParams['font.sans-serif']=[u'SimHei']
mlp.rcParams['axes.labelsize']=12
mlp.rcParams['xtick.labelsize']=12
mlp.rcParams['ytick.labelsize']=12

Conf=SparkConf().setMaster("local").setAppName("Live_analyze")
sc=SparkContext(conf=Conf)
ticks=['观众数','弹幕数量','热度中值','时长','关注增长','收入']
raw_data=sc.textFile("data.txt")
data=raw_data.map(lambda x:x.strip().split('|'))
date_label=data.map(lambda x:x[-1]).collect()#日期
data_features=data.map(lambda x:x[0:-1])
data_KNN=np.array(data_features.collect()).astype(np.float)
data_KNN=MinMaxScaler().fit_transform(data_KNN)
LiveVectors=sc.parallelize(data_KNN)
Plotxx=np.array(LiveVectors.collect())
print(Plotxx)
model=KMeans.train(LiveVectors,3,initializationMode='k-means||',maxIterations=10,runs=10,epsilon=0.01)
print("Final centers: " + str(model.clusterCenters))
print("Total Cost: " + str(model.computeCost(LiveVectors)))
#pca = PCA(n_components=2)  
#xx=pca.fit_transform(data_KNN)
#print(xx)
prediction=model.predict(LiveVectors)
labels=prediction.collect()
K=15#6副画
plt.figure(figsize=(8,6))
comb_list=np.array(list(comb(range(6),2)))
#index=np.random.randint(0,len(comb_list),size=K)
#temp=[comb_list[i] for i in index]
#temp=np.array(temp)
for i in range(1,K+1):
    ax=plt.subplot(4,4,i)
    x=comb_list[i-1,0]
    y=comb_list[i-1,1]
    ax.scatter(Plotxx[:,x],Plotxx[:,y],c=labels)
    for a,b,j in zip(Plotxx[:,x],Plotxx[:,y],range(data.count())):
        ax.text(a, b+0.0005,date_label[j], ha='center', va= 'bottom',fontsize=8)
    ax.set_xlabel(ticks[x])
    ax.set_ylabel(ticks[y])
    plt.tight_layout()
plt.show()
