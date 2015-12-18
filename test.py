import os, sys

os.system("clear");


def fact(n):
	val = 1;
	for i in range(2, n+1):
		val = val * i;
	return val;

lamda = float(10);
mu = float(6);
n = int(10);
c = int(10);
os.system("clear");
rho = lamda / (c * mu);

p0 = 0;
for i in range(0, c):
	val1 = pow(rho, n) / fact(n);
	val2 = pow(rho, c) / fact(c);
	val3 = 1 / (1 - (rho / c));
	p0 = p0 + (val1 + val2 * val3);

pn = pow(lamda, n) * p0 / (fact(c) * pow(mu, n) * pow(c, n-c));
lq = pow(rho, c+1) * p0 / (fact(c-1) * pow(c-rho, 2));
ls = lq + rho;
ws = ls / lamda;
wq = lq / lamda;

print("P (utilization) = " + str(rho));
print("Probability that 0 people are in the system: " + str(p0));
print("Probability that " + str(n) + " people are in the queue: " + str(pn));
print("Expected number of customers in the system: " + str(ls));
print("Expected number of customers in the queue: " + str(lq));
print("Expected waiting time of customers in the system: " + str(ws*60) + " minutes" );
print("Expected waiting time of customers in the queue: " + str(wq*60) + " minutes");

print("\n");
