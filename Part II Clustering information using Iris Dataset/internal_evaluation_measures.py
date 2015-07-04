import math


def calcEuclideanDist(pt1, pt2, dimens=4):
	dist = 0
	for x in range(0, dimens):
		dist = dist + (float(pt1[x])-float(pt2[x]))**2
	
	return math.sqrt(dist)
	

