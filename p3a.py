
# M|M|1|N
l = 8.0 #float(input("Enter arrival rate "))
m = 9.0 # float(input("Enter service rate"))
n = 10 #int(input("Enter number of people")) 
r = l/m #server utilization
p0 = (1-r)/(1 - pow(r,n+1))
pnq = p0 + (r*p0) #probability of no queue
pn = pow(r,n)*p0
ls = r * (1 + n*(r**(n+1)) - (n+1)* (r**n)) / ((1 - r) * (1 - (r**(n+1))))
l_eff = l * (1-pn)
lq = ls - (l_eff/m)
ws = ls/l_eff 
wq = ws - (1/m)
print ls,lq,ws*60,wq*60