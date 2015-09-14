# -*- coding: utf-8 -*-
from math import log

#计算给定数据集的香农熵
##   信息定义为： l(xi) = -log2(p(xi))    p(xi)是该分类的概率
##   熵 H = 负号 - 求和from 1 至 n p(xi)log2(p(xi))   n是分类的数目
##

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    #dictionary
    labelCounts = {}
    for featVec in dataSet:
        #最后一列为分类标签
        currentLabel = featVec[-1]
        if currentLabel not in labelCount.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannonEnt = 0.0
    for key in labelCounts:
        #每种类别出现概率
        prob = float(labelCount[keys])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt
