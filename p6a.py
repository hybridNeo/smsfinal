import math
ld = input("Enter lambda value")
x0 = 27.0
a = 8.0
c = 47.0
m = 100
n = 15
l = []
for i in range(n):
	n-=1
	x0 = (a*x0+c)%m
	l.append(x0/m)
print 'the generated numbers are ',l
print "The variates are :"
for r in l:
	x = -(math.log(1-r))/ld
	print x