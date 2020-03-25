#coding=utf-8
import numpy as np
from sklearn.decomposition import PCA
import util

dataSet = util.loadDataSet("EEG_feature.txt")
pca = PCA(n_components=2)   #降到2维
pca.fit(dataSet)                  #训练
newX=pca.fit_transform(dataSet)   #降维后的数据
# PCA(copy=True, n_components=2, whiten=False)
# print(pca.explained_variance_ratio_)  #输出贡献率
for a in newX:
    print('{}\t{}'.format(a[0],a[1]))