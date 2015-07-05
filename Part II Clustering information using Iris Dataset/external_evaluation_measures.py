from readARFF import *
import numpy as np
from sklearn.metrics.cluster import normalized_mutual_info_score

def calcNMI():

	dataset = readARFF();

	subSet = dataset[['class', 'cluster']]
	#print subSet

	NMI = normalized_mutual_info_score(subSet['class'], subSet['cluster'])
	print NMI

calcNMI()