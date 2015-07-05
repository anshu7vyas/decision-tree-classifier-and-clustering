from internal_evaluation_measures import *
import pandas as pd
from readARFF1 import *
import numpy as np

def getDiameter(dataFrame):

	size = len(dataFrame)
	print size
	#sizeOfclusters = df.groupby('cluster').size().to_dict()
	#print sizeOfclusters

	myList = dataFrame.values.tolist()
	#print myList
	diam = 0
	N = size
	
	for i in range(0,N):
		for j in range(0,N):
			if i is not j:
				diam = diam + calcEuclideanDist(myList[i],myList[j],4)

	return math.sqrt(diam/(N*(N-1)))
	

def averageLink(list1, list2, dimens=4):
	distSum = 0
	distLarge = 0
	N = 0

	for x in range(0, len(list1)-1):
       for y in range(0, len(list2)-1):
           distNow = calcEuclidianDist(list1[x], list2[y], dimension)
           distSum = distSum + distNow
           N = N+1
           if distNow > distLarge:
               distLarge = distNow
   
   averageDistance = distSum/N
   return averageDistance, distLarge

def main():
	df = readARFF()
	df.drop('class', axis=1, inplace=True)
	df.drop('cluster', axis=1, inplace=True)

	diam = getDiameter(df)	
	print averageLink(list1, list2, 4)
