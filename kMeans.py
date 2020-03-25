# -*- coding: utf-8 -*-
__author__ = 'Mage'

import util

def kMeans(dataSet,K,Z):
    count = 0
    print("K={},初始中心为{}".format(K,Z))
    while True:
        clusters = []
        clusteri = []
        #初始化分类list
        for z in Z:
            zs = [z]
            clusters.append(zs)
            clusteri.append([])
        #按照近邻法分配各点数据
        for i in range(len(dataSet)):
            minDist = util.distEclud(dataSet[i],Z[0])
            minInx = 0
            for inx in range(len(Z)):
                dist = util.distEclud(dataSet[i],Z[inx])
                if dist < minDist:
                    minDist = dist
                    minInx = inx
            clusters[minInx].append(dataSet[i])
            clusteri[minInx].append(i)

        isEnd = True
        Z = []
        #计算新的聚类中心，如果聚类中心有更新，则迭代继续
        for cluster in clusters:
            vecR = cluster[1]
            for i in range(2,len(cluster)):
                vecR = list(map(lambda x: x[0]+x[1], zip(vecR, cluster[i])))
            vec = [a / (len(cluster)-1) for a in vecR]
            Z.append(vec)
            if vec != cluster[0]:
                isEnd = False
        count += 1
        print("第{}轮分类，是否结束:{},聚类中心:{}".format(count,isEnd,Z))
        if isEnd:
            break
    return clusteri,clusters


if __name__ == "__main__":
    #dataSet = [[0,0],[1,0],[0,1],[1,1],[2,1],[1,2],[2,2],[3,2],[6,6],[7,6],[8,6],[6,7],[7,7],[8,7],[9,7],[7,8],[8,8],[9,8],[8,9],[9,9]]
    dataSet = util.loadDataSet("EEG_feature.txt")
    labels = util.loadDataSet("valence_arousal_label.txt")
    data = util.loadDataSet("EEG_pca_feature.txt")
    Z = [dataSet[0],dataSet[1],dataSet[2],dataSet[7]] 
    K = 4
    

    clusteri,clusters = kMeans(dataSet,K,Z)

    util.plotFeature(data,clusteri)
    # for i in range(len(clusteri)):
    #     print("分类:{:d}".format(i))
    #     for inx in clusteri[i]:
    #         print("编号:{:d},标签:{}".format(inx,labels[inx]))


        
