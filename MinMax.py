# -*- coding: utf-8 -*-
__author__ = 'Mage'

import util

def genClusters(dataSet,thita=1/2,Z1=0):
    
    if Z1 >= len(dataSet) or Z1 < 0:
        Z1 = 0
    zs = [dataSet[Z1]]
    zsi = [Z1]
    maxDist = 0
    maxInx  = 0
    #选取距离Z1最远的点作为Z2
    for inx in range(len(dataSet)):
        dist = util.distEclud(dataSet[inx],zs[0])
        if dist > maxDist:
            maxInx = inx
            maxDist = dist
    zs.append(dataSet[maxInx])
    zsi.append(maxInx)
    print(zsi)

    while True:
        Dist = []
        #每个点距离各中心最小距离存入Dist
        for inx in range(len(dataSet)):
            d = util.distEclud(dataSet[inx],zs[0])
            for z in zs:
                dist = util.distEclud(dataSet[inx],z)
                if dist < d:
                    d = dist
            Dist.append(d)
        #Dist中最大值大于Z1和Z2距离的thita倍，则成为新聚类中心
        if max(Dist) > util.distEclud(zs[0],zs[1]) * thita:
            print("maxDist:{:.5f} > ||z0-z1|| * thita({:.5f} * {:.3f} = {:.5f})".format(max(Dist),util.distEclud(zs[0],zs[1]),thita,util.distEclud(zs[0],zs[1])*thita))
            index = Dist.index(max(Dist))
            zs.append(dataSet[index])
            zsi.append(index)
            print("update clusters :{}".format(zsi))
        else:
            break
    return zs,zsi

def MinMax(dataSet,thita=1/2,Z1=0):
    zs,zsi = genClusters(dataSet,thita,Z1)
    clusteri,clusterz = util.classify(dataSet,zs,zsi)
    return clusteri,clusterz

if __name__ == "__main__":
    dataSet = util.loadDataSet("EEG_feature.txt")
    data = util.loadDataSet("EEG_pca_feature.txt")
    labels = util.loadDataSet("valence_arousal_label.txt")
    
    thita = 0.77
    Z1    = 500
    clusteri,clusterz = MinMax(dataSet,thita,Z1)

    util.plotFeature(data,clusteri)

    # for i in range(len(clusteri)):
    #     print("分类:{:d}".format(i))
    #     for inx in clusteri[i]:
    #         print("编号:{:d},标签:{}".format(inx,labels[inx]))
    




