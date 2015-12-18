import math
import random
mu0 = 4.3
a = 16807
m = 2147483
c = 0
n = 20
rndLst = []
seed = random.randint(0,20)
rndLst.append(seed)
random_numbers = []
for i in range(n):
	rndLst.append((a* rndLst[-1]+c)%m)
for i in rndLst:
	random_numbers.append(round(float(i)/float(m),2))
delay = []
for i in random_numbers:
	delay.append(round(i*10,2))
avg_delay = float(sum(delay)/len(delay))
total = 0
for i in delay:
	total = total + ((i- avg_delay)*(i-avg_delay))
var = float(total/(n-1))
sd = math.sqrt(var)
t_table = input("Enter table value")
CI_1 = avg_delay + t_table * sd / math.sqrt(n)
CI_2 = avg_delay - t_table * sd /math.sqrt(n)
we = abs(CI_1- mu0)
be = abs(CI_2- mu0)
