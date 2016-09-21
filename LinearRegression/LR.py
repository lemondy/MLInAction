#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description: implements the linear regression model
# Author: YunZhang
# Created on 2016/9/20
#

from numpy import *

'''
  load data from fie

'''
def loadData(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1   # get the dimension of feature
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(lineArr[-1])      # the last column represent label
    return dataMat, labelMat

'''
 calculate the wights. w = (x.T * x).inverse * x.T * y
'''
def standRegres(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse."
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws



# Locally weighted linear regression (LWLR)

def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j, j] = math.exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.dat(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse."
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat

