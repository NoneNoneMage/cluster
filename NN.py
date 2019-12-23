# -*- coding: utf-8 -*-
__author__ = 'Mage'

import util
from numpy import *

def genMinMaxT(dataSet,begin,end,k,accuracy=4,Z1=0):
    """ Get range of T for target k clusters
    
        Input:

            dataSet (list): Input dataset
            begin (int)   : Start value of T
            end (int)     : End value of T
            k (int)       : Number of target classifications 
            accuracy (int): Accurate to the number of decimal places
            Z1 (int))     : Index of first clustering center
        Output:

            min(float),max(float)
            Minimum and maximum T of the number of target classifications
    """
    status = 0
    step = 1
    count = accuracy+1
    while True:
        if status == 0:
            #Dichotomy approach
            tmp = float((begin+end)/2)
        else:
            if status%2 == 1:
                #Approach the lower limit in steps of step, step / 10 and step / 100
                tmp = begin + step/power(10,(status-1)//2)
            if status%2 == 0:
                #Approach the upper limit in steps of step, step / 10 and step / 100
                tmp = end - step/power(10,(status-1)//2)
        zs,zsi = genClusters(dataSet,tmp,Z1)
        if len(zsi) > k:
            print("update begin {:.5f}".format(tmp))
            begin = tmp
        if len(zsi) < k:
            print("update end {:.5f}".format(tmp))
            end = tmp
        if len(zsi) == k:
            if status == 2*count:
                break
            else:
                status = status + 1

    print("begin:{:.5f},end:{:.5f}".format(begin,end))    
    return begin,end
    

def genClusters(dataSet,T,Z1=0):
    """ Get number of clusters

        Input:

            dataSet (list)  : Input dataset
            T (float)       : Distance threshold
            Z1 (int))   : Index of first clustering center
        Output:

            List of clustering center
    """
    if Z1 >= len(dataSet) or Z1 < 0:
        Z1 = 0
    zs = [dataSet[Z1]]
    zsi = [Z1]
    for i in range(len(dataSet)):
        minDist = util.distEclud(dataSet[i],zs[0])
        #print(minDist)
        for z in zs:
            dist = util.distEclud(dataSet[i],z)
            if dist < minDist:
                minDist = dist
        if minDist > T:
            zs.append(dataSet[i])
            zsi.append(i)
    return zs,zsi

def NN(dataSet,T,Z1=0):
    """ Implemention of NN classify

        Input:

            dataSet (list)  : Input dataset
            T (float)       : Distance threshold
            Z1 (int))   : Index of first clustering center
        Output:

    """
         
    zs,zsi = genClusters(dataSet,T,Z1)
    
    clusteri,clusterz = util.classify(dataSet,zs,zsi)
    return clusteri,clusterz

 #   for data in dataSet:



if __name__ == "__main__":
    dataSet = util.loadDataSet("EEG_feature.txt")
    labels = util.loadDataSet("valence_arousal_label.txt")
    Z1 = 882  #First cluster center
    beginT = 0 #Dist threshold begin val
    endT = 1000 #Dist threshold end val
    accuracy = 4 #Accurate to the number of decimal places
    k = 4 #Target number of clusters
    min,max=genMinMaxT(dataSet,beginT,endT,accuracy,k,Z1)
    print(min,max)


    # T = (min+max)/2
    # zs,zsi = genClusters(dataSet,T,Z1)
    # print(zsi)


    T = (min+max)/2
    clusteri,clusterz = NN(dataSet,T,Z1)

    for i in range(len(clusteri)):
        print("分类:{:d}".format(i))
        c1=[1.0]
        for inx in clusteri[i]:
            print("编号:{:d},标签:{}".format(inx,labels[inx]))


    # for a in util.floatrange(0.01,1,10):
    #     T = min + (max-min)*a
    #     print(T)
    #     zs,zsi = genClusters(dataSet,T,Z1)
    #     print(zsi)
    #     for i in zsi:
    #         print(labels[i])
    