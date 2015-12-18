import os, sys

os.system("clear");


def probability(n):
	return (pow(rho, n) * p0);


lamda = 8.0
mu = 9.0#float(input("Enter service rate: "));
n = 10#int(input("Enter number of people: "));
os.system("clear");
rho = lamda / mu;
print rho
p0 = (1 - rho) / (1 - (pow(rho, n+1)));
pnq = p0 + (rho*p0);

pn = probability(n);

ls = rho * (1 + (n*pow(rho,n+1)) - (n+1)*pow(rho,n)) / ((1-rho)*(1-pow(rho, n+1)) );
lamdaEff = lamda * (1 - pn);
lq = ls - (lamdaEff / mu)
ws = ls / lamdaEff;
wq = ws - (1/mu);

print("P (utilization) = " + str(rho));
print("Effective arrival rate = " + str(lamdaEff));
print("Probability that 0 people are in the system: " + str(p0));
print("Probability that " + str(n) + " people are in the queue: " + str(pn));
print("Expected number of customers in the system: " + str(ls));
print("Expected number of customers in the queue: " + str(lq));
print("Expected waiting time of customers in the system: " + str(ws*60) + " minutes" );
print("Expected waiting time of customers in the queue: " + str(wq*60) + " minutes");

print("\n");
