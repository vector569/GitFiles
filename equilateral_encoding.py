#!/usr/bin/env python


#Equilateral encoding
#Done via recursion with a seed point in 2 dimensions
def encode(arr,n):
	k = arr[0]
	if k is n:
		return arr
	if(k<n):
		i = 0;
		newp = [];
		while (i<k-1):
			newp.append(0)
			i += 1
		newp.append(1)
		i = 0
		sumsq = 0
		while(i<k-1):
			sumsq += arr[1][i]*arr[1][i]
			i += 1	
		r = 1-(1-sumsq)**(0.5)
		i = 1
		while(i<=k):
			arr[i].append(r)
			i += 1
		arr[0] += 1
		k += 1
		arr.insert(1,newp)
		centroid = 0
		i = 1
		while(i<=k):
			centroid += arr[i][k-2]
			i += 1
		centroid /= k
		i = 1
		while(i<=k):
			arr[i][k-2] -= centroid
			i += 1
		return encode(arr,n)		

# The encoding is of the form
# [n,[a,b,c....(n-1)th element],... n points]]
# Total array size is n+1 
if __name__ == '__main__':
	n = input("Enter n(>=2)")
	seed = [2,[-0.5],[0.5]]
	encoding = encode(seed,n)
	print encoding
	e = encoding[1]
	f = encoding[2]
	sum = 0
	i = 0
	while(i<n-1):
		sum += (e[i]-f[i])**2
		i += 1
	print sum

	



