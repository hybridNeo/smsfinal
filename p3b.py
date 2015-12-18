def fact(n):
	if n == 0 or n == 1:
		return 1
	return n*fact(n-1)
l = 10.0
m = 6.0
n = 10
c = 10
rho = (l/m*c)
p0 = 0
for i in range(0,c):
	val1 = pow(rho,n)/fact(n)
	val2 = pow(rho,c)/fact(c)
	val3 = 1/(1 - rho/c)
	p0+= val1 + val2 * val3
pn = l**n *p0 / fact(c) * m**n * c**(n-c)
print pn
