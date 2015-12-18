import math
import random


a=16807
m=2147483
c=0
n=20
rndLst=[]
seed=random.randint(0,20)

rndLst.append(seed)
for i in range(n):
	rndLst.append((a*rndLst[-1]+c)%m)
random_numbers = []
for it in rndLst:
	random_numbers.append(round(float(it)/float(m),2))

delay1 = []
for i in random_numbers:
	delay1.append(i * 10)

delay2 = []
for i in delay1:
	delay2.append(0.88 * i)

diff = []
for i in range(len(delay1)):
	diff.append(delay1[i] - delay2[i])

avg_diff = sum(diff)/len(diff)

total = 0
for i in diff:
	total = total + ((i - avg_diff)*(i - avg_diff))
var = float(total/(n-1))
sd = math.sqrt(var)
t_table = 2.093
alpha = 0.05
print ("critical value at (",alpha/2,",",n-1,"): ",t_table)

H = t_table * sd / math.sqrt(n)
val1 = avg_diff - H
val2 = avg_diff + H

if val1>0:
	print("System1 is better")
elif val2<0:
	print("System2 is better")

