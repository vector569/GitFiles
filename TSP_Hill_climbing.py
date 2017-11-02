#!/usr/bin/env python
import numpy as np
import math
import random
def distance(route):
	length = len(route)
	dist = 0
	i = 0
	while i<length-1:
		dist += ((route[i][1]-route[i+1][1])**2 + (route[i][2]-route[i+1][2])**2)**0.5
		i += 1
	return dist
def centroid(route):
	length = len(route)
	i = 0
	centroidx = 0
	centroidy = 0
	while i<length:
		centroidx += route[i][1]
		centroidy += route[i][2]
		i += 1
	centroidx /= length
	centroidy /= length
	i = 0
	while i <length:
		route[i][1] -= centroidx
		route[i][2] -= centroidy
		i += 1
	return route
def mutate(route,a1,a2):
	route1 = route[:]
	temp = route1[a1]
	route1[a1] = route1[a2]
	route1[a2] = temp
	return route1

DATA = open('china.csv')
data = []
for line in DATA:
	a = line.split(' ')
	data.append([int(a[0]),float(a[1]),float(a[2].replace('\n',''))])
T = 10**4
deltaT = 1
num_nodes = len(data)
data = centroid(data)
route = data
while T>0:
	existing_dist = distance(route)
	temperory_routes = []
	a1 = int(random.random()*num_nodes)
	a2 = int(random.random()*num_nodes)
	mutation = mutate(route,a1,a2)
	mutating_dist = distance(mutation)
	if mutating_dist<existing_dist:
		route = mutation
	print existing_dist,T
	T = T - deltaT
print route

	

	

