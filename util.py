# -*- coding: utf-8 -*-
__author__ = 'Mage'

from numpy import *
import matplotlib.pyplot as plt

def plotFeature(pcadata, clusteri):
    data=array(pcadata)
    fig = plt.figure()
    scatterColors = ['blue', 'green', 'yellow', 'brown','red','black']
    ax = fig.add_subplot(111)
    for i in range(len(clusteri)):
            print("分类:{:d}".format(i))
            for inx in clusteri[i]:
                ax.scatter(data[:,0][inx], data[:,1][inx], c=scatterColors[i], s=30)
    plt.show()

def loadDataSet(fileName, splitChar='\t'):
    """ Load vectors from file
    
        Input:

            fileName (str)  : Local file of dataset
            splitChar (str) : Separator between data in each row

        Output:

            List of vectors
    """
    dataSet = []
    with open(fileName) as fr:
        for line in fr.readlines():
            curline = line.strip().split(splitChar)
            fltline = list(map(float, curline))
            dataSet.append(fltline)
    return dataSet

def distEclud(vecA, vecB):
    """ Computes euclidean distance of two vectors

        Input:

            vecA (list) : vector A
            vecB (list) : vector B

        Output:
            Euclidean distance of two vectors
    """
    vecC = list(map(lambda x: x[0]-x[1], zip(vecA, vecB)))
    return sqrt(sum(power(vecC, 2)))

def floatrange(start,stop,steps):
    ''' Computes a range of floating value.
       
        Input:

           start (float)  : Start value.
           end   (float)  : End value
           steps (int): Number of values
       
        Output:

           A list of floats
       
       Example:
          >>> print floatrange(0.25, 1.3, 5)
           [0.25, 0.51249999999999996, 0.77500000000000002, 1.0375000000000001, 1.3]
    '''
    return [start+float(i)*(stop-start)/(float(steps)-1) for i in range(steps)]

def classify(dataSet,zs,zsi):
    if len(zs) < 2 or len(zs) != len(zsi):
        return dataSet
    clusteri = []
    clusterz = []
    for index in zsi:
        ci = []
        ci.append(index)
        clusteri.append(ci)
        cz = []
        cz.append(dataSet[index])
        clusterz.append(cz)

    for inx in range(len(dataSet)):
        minzsi = 0
        mindist = distEclud(dataSet[inx],zs[0])
        for i in range(len(zs)):
            dist = distEclud(dataSet[inx],zs[i])
            if dist < mindist:
                minzsi = i
                mindist = dist
        clusteri[minzsi].append(inx)
        clusterz[minzsi].append(dataSet[inx])
    return clusteri,clusterz


if __name__ == "__main__":
    data = loadDataSet("EEG_pca_feature.txt")
    labels = loadDataSet("valence_arousal_label.txt")
    clusteri = [[],[],[],[]]
    for lb in range(len(labels)):
        if labels[lb] == [1,1]:
            clusteri[0].append(lb)
        if labels[lb] == [1,2]:
            clusteri[1].append(lb)
        if labels[lb] == [2,1]:
            clusteri[2].append(lb)
        if labels[lb] == [2,2]:
            clusteri[3].append(lb)
    plotFeature(data,clusteri)

    