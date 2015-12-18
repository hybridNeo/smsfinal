import math
file = open('te.txt','r')
def pdf(x):
	return (1.0/mean)*math.exp(-x/mean)
arr = sorted(map( lambda x:float(x),file.read().split(',')))
min_ = arr[0]
max_ = arr[-1]
r = (max_ - min_)/10.0
buckets = [0 for i in range(10)]
for i in arr:
	buckets[int(i)]+=1
graph = [i*'*' for i in buckets]
print 'Graph:'
for i in graph:
	print i
freq = []
print "r is ",r
for it in range(1,11):
	freq.append([min_+(it-1)*r,min_ + it*r,0])
for i in arr:
	for j in range(len(freq)):
		if i >= freq[j][0] and i <= freq[j][1]:
			freq[j][2] += 1
mean = 5
chisquare = 0
for i in range(len(freq)):
	ex = pdf(min_ + (i+1)*r )
	chisquare += (freq[i][2]/len(arr) -ex)**2/ex
print "chisquare : ", chisquare
print "chi- alpha :" ,16.92
