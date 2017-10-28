#!usr/bin/env python

from random import *


def cluster_centr(cluster,n):
	centroid = [0]*n
	length = len(cluster)
	i = 0
	while i<n:
		j = 0
		while j<length:
			centroid[i] += cluster[j][i]
			j += 1
		centroid[i] /= length
		i += 1
	return centroid

def cleandata(DATA):
	data = []
	r = 1
	for vector in DATA:
		a = vector.split(',')
		i = 0
		if len(a) is 5:  #change vector_size-1 = 4
			while i<4: #change vector_size-1 = 4
				a[i] = float(a[i])
				i += 1
		data.append(a)
		r += 1
	return data

def initialise_clusters(data,K):
	Clusters = [[],[],[],[]] #assign this from k-value
	i = 0
	while i<len(data):
		Clusters[i%K].append(data[i])
		i += 1
	return Clusters

def centr_set(Clusters,n,K):
	Centroid = [[],[],[],[]]
	i = 0
	while i<K:
		cluster = Clusters[i]
		Centroid[i] = cluster_centr(cluster,n-1)
		i += 1
	return Centroid
def dist(vec,centr):
	length = len(centr)
	i = 0
	dist = 0
	while i<length:
		dist += (vec[i]-centr[i])**2
		i += 1
	dist = dist**0.5
	return dist

def clustering(Clusters,Centroid_set,K,vector_size):
	stopflag = 1
	i = 0
	while stopflag > 0:
		i += 1
		stopflag = 0
		t = 0
		while t<K:
			cluster = Clusters[t]
			v = 0
			while v<len(cluster):
				observation = cluster[v]
				j = 0
				flag = 0
				distance = 9999
				while j<K:
					temp_dist = dist(observation,Centroid_set[j])
					if temp_dist < distance:
						distance = temp_dist
						flag = j
					j += 1
				
				if flag != t:
					Clusters[flag].append(observation)
					del Clusters[t][v]
					stopflag += 1
				v += 1
			t += 1
		Centroid_set = centr_set(Clusters,vector_size,K)
		#print Clusters[3]
	return Clusters


if __name__ == "__main__":
	DATA = open("Iris.csv")
	data = cleandata(DATA)
	vector_size = len(data[1]) #5 in this case
	K = 4 #calculate_no_of_clusters(data)
	Clusters = initialise_clusters(data,K)
	Centroid_set = centr_set(Clusters,vector_size,K)
	Final_cluster = clustering(Clusters,Centroid_set,K,vector_size)
	#print Final_cluster[0]
	#print Final_cluster[1]
	#print Final_cluster[2]
	#print Final_cluster[3]
dtyhgrf			
				
			



		
	



