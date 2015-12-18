import math
import matplotlib.pyplot as plt
print("Enter lambda value")
h = int(input())
x0=27 
a=8
c=47 
m=100
n=15
l=[]
num=n
while(n):
	n=n-1
	x1=(a*x0+c)%m
	x0=x1
	r=x0/m
	l.append(r)
print(l)

min1=5
max1=20

xi=[]
for x in l:
	xi.append(min1+x*(max1-min1))
print(xi)

plt.plot(l,xi ,'g^')
plt.axis([0,1,min1,max1 ])
plt.show()
