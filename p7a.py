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

mean = 5
