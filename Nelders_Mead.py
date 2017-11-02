import numpy as np
import math
import random
# have to generalise nearly everything to N-Dimensions
# there is a bug whereby the best, good and worst get
#  out of order once before converging in a wrong way
def ackley(x):
	return -20*np.exp(-0.2*(0.5*(x[0]**2+x[1]**2)**0.5))-np.exp(0.5*(np.cos(2*np.pi*x[0])+np.cos(2*np.pi*x[1])))+np.e+20
def beale(x):
	return (1.5-x[0]+x[0]*x[1])**2+(2.25-x[0]+x[0]*x[1]*x[1])**2+(2.625-x[0]+x[0]*x[1]*x[1]*x[1])**2
def levis(x):
	return (np.sin(3*np.pi*x[0]))**2 + ((x[0]-1)**2)*(1+(np.sin(3*np.pi*x[1]))**2)+((x[1]-1)**2)*(1+(np.sin(2*np.pi*x[1]))**2)
def cross_in_tray(x):
	return -0.0001*((np.abs(np.sin(x[0])*np.sin(x[1])*np.exp(np.abs(100-((x[0]*x[0]+x[1]*x[1])**0.5)/np.pi)))+1)**0.1) + 2.06261187082
def egg_holder(x):
	return -1*(x[1]+47)*np.sin((np.abs(x[0]/2+x[1]+47))**0.5)-x[0]*np.sin((np.abs(x[0]-(x[1]+47)))**0.5) + 959.640662711
def init_generate(max1): 
	a = random.random()*max1
	b = random.random()*max1
	if b is a:
		b += 1
	c = random.random()*max1
	if  c is b or c is a:
		c += 3
	return a,b,c
def testfucn(n,x):
	if n is 1:
		return ackley(x)
	if n is 2:
		return beale(x)
	if n is 3:
		return levis(x)
	if n is 4:
		return cross_in_tray(x)
	if n is 5:
		return egg_holder(x)
def organise(a,b,c,n):
	B = G = W = [None,None]
	P1 = testfucn(n,a)
	P2 = testfucn(n,b)
	P3 = testfucn(n,c)
	P4 = max([P1,P2,P3])
	if P4 is P1:
		W = a
		P5 = max(P2,P3)
		if P5 is P2:
			G = b
			B = c
		if P5 is P3:
			G = c
			B = b 
	if P4 is P2:
		W = b
		P5 = max(P1,P3)
		if P5 is P1:
			G = a
			B = c
		if P5 is P3:
			G = c
			B = a 
	if P4 is P3:
		W = c
		P5 = max(P2,P1)
		if P5 is P2:
			G = b
			B = a
		if P5 is P1:
			G = a
			B = c
	return B,G,W
def dist(x,y):
	return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5
def convergence(x,y,z):
	a = dist(x,y)
	b = dist(y,z)
	c = dist(x,z)
	s = (a+b+c)/2
	ar = (s*(s-a)*(s-b)*(s-c))**0.5
	if ar<0.0000000000000001:
		return 0
	return 1
#print ackley([0,0])
#print beale([3,0.5])
#print levis([1,1])
#print cross_in_tray([1.34941,1.34941])
#print egg_holder([12,404.2319])
Test_case = 4
a,b,c = init_generate(2)
p,q,r = init_generate(2)
B = G = W = [None, None]
B, G, W = organise([a, p], [b, q], [c, r],Test_case)
R = [None, None]
M = [None, None]
E = [None, None]
C = [None, None]
C1 = [None, None]
C2 = [None, None]
i = 0
while convergence(B,G,W):
	B, G, W = organise(B, G, W,Test_case)
	M[0] = (B[0] + G[0])/2
	M[1] = (B[1] + G[1])/2
	R[0] = 2*M[0] - W[0]
	R[1] = 2*M[1] - W[1]
	if testfucn(Test_case,G) > testfucn(Test_case,R) and testfucn(Test_case,R) > testfucn(Test_case,B):
		W = list(R)
	elif testfucn(Test_case,B) > testfucn(Test_case,R):
		E[0] = 2*R[0] - M[0]
		E[1] = 2*R[1] - M[1]
		if testfucn(Test_case,R) > testfucn(Test_case,E):
			W = list(E)
		else:
			W = list(R)
	else:
		C1[0] = 0.25*W[0]+0.75*M[0]
		C1[1] = 0.25*W[1]+0.75*M[1]
		C2[0] = 0.75*W[0]+0.25*M[0]
		C2[1] = 0.75*W[1]+0.25*M[1]
		if testfucn(Test_case,C1)<testfucn(Test_case,C2):
			C = list(C1)
		else:
			C = list(C2)
		if testfucn(Test_case,C)<testfucn(Test_case,G):
				W = list(C)
		else:
			G = list(M)
			W[0] = (B[0] + W[0]) / 2
			W[1] = (B[1] + W[1]) / 2
	i += 1
print B,G,W
print testfucn(Test_case,B),testfucn(Test_case,G),testfucn(Test_case,W)