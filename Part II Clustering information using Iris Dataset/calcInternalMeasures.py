__author__ = 'NANSH'

from internal_evaluation_measures import calcEuclideanDist
import pandas as pd
from readARFF1 import *
import numpy as np
import math

"""@return the diameter of a particular cluster"""
def getDiameter(dataFrame):
	size = len(dataFrame)
	print size

	myList = dataFrame.values.tolist()
	#print myList
	diam = 0
	N = size
	for i in range(0,N):
		for j in range(0,N):
			if i is not j:
				diam = diam + (calcEuclideanDist(myList[i],myList[j])**2)

	return math.sqrt(diam/(N*(N-1)))

"""@return average link betwee two clusters"""
def averageLink(list1, list2, dimens=4):
	distSum = 0
	N = 0

	for x in range(0, len(list1)):
		for y in range(0, len(list2)):
			distNow = calcEuclideanDist(list1[x], list2[y], 4)
			distSum = distSum + distNow
			N = N + 1
			
	averageLink = distSum/N
	return averageLink

"""@return complete link between two clusters"""
def completeLink(list1, list2, dimens=4):
	distLarge = 0

	for x in range(0, len(list1)):
		for y in range(0, len(list2)):
			distNow = calcEuclideanDist(list1[x], list2[y], 4)
			if distNow > distLarge:
				distLarge = distNow

	return distLarge


def main():
	df0, df1 = readARFF()
	df0.drop('class', axis=1, inplace=True)
	df0.drop('cluster', axis=1, inplace=True)

	df1.drop('class', axis=1, inplace=True)
	df1.drop('cluster', axis=1, inplace=True)
	'''
	df2.drop('class', axis=1, inplace=True)
	df2.drop('cluster', axis=1, inplace=True)
	'''
	myList0 = df0.values.tolist()
	myList1 = df1.values.tolist()
	#myList2 = df2.values.tolist()

	print getDiameter(df0)
	print "#####################################################################"
	print getDiameter(df1)
	print "#####################################################################"
	#print getDiameter(df2)
	print "#####################################################################"
	print "#####################################################################"
	print "Average Link and Complete Link between cluster 0 and cluster 1:"
	print averageLink(myList0, myList1, 4)
	print "#####################################################################"
	#print "Average Link and Complete Link between cluster 0 and cluster 2:"
	#print averageLink(myList0, myList2, 4)
	#print "#####################################################################"
	#print "Average Link and Complete Link between cluster 1 and cluster 2:"
	#print averageLink(myList1, myList2, 4)


main()
