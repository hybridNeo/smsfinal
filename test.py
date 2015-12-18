from random import *

fp = open("input.txt","r")
data = fp.read()
fp.close()
data = data.split("\n")
iatp = data[0].split(";")
stp = data[1].split(";")
iat = []
arr_prob = []
ser = []
ser_prob = []
for i in range(0,len(iatp)):
	iat.append(int(iatp[i].split(":")[0]))
	arr_prob.append(float(iatp[i].split(":")[1]))
for i in range(0,len(stp)):
	ser.append(int(stp[i].split(":")[0]))
	ser_prob.append(float(stp[i].split(":")[1]))
avg_wait_time=[]

iarr_t = []
for k in range(10):
	N = int(input("Enter no. of customers: "))
	for i in range(0,N):
		rn1 = random() * 100;
		#print rn1
		t = 0
		cum = 0
		for j in range(0,len(iat)):
			cum+=int(arr_prob[j]*100)
			#print cum
			if rn1 >= t and rn1< cum :
				iarr_t.append(iat[j])
				break
			else:
				t = cum
	
	ser_t = []
	for i in range(0,N):
		rn2 = round(random() * 100,2);
		print("rn2: ",rn2)
		t = 0
		cum = 0
		for j in range(0,len(ser)):
			cum+=int(ser_prob[j]*100)
			#print cum
			if rn2 >= t and rn2< cum :
				ser_t.append(ser[j])
				break
			else:
				t = cum
	print("t ",ser_t)
	at = list(range(N)) 
	start_1 = list(range(N))
	start_2 = list(range(N)) 
	finish_1 = list(range(N))
	finish_2 = list(range(N))
	wait_1 = list(range(N))
	wait_2 = list(range(N))
	tot_sys = list(range(N))
	idle_1 = list(range(N))
	idle_2 = list(range(N))
	nurse = int(input("Enter service time of nurse:"))
	for i in range(0,N):
		if i==0:
			at[i] = iarr_t[0]
			start_1[i] = at[i]
		else:
			#Nurse
			at[i] = at[i-1] + iarr_t[i]
			start_1[i] = max(at[i],finish_1[i-1])
		finish_1[i] = start_1[i] + nurse
		wait_1[i] = start_1[i] - at[i]

		#Doctor
		if i==0:
			start_2[i] = finish_1[i]
		else:
			start_2[i] = max(finish_1[i],finish_2[i-1])
		print(i,ser_t[i])
		finish_2[i] = start_2[i] + ser_t[i]
		wait_2[i] = start_2[i] - finish_1[i]
		tot_sys[i] = finish_2[i] - at[i]
		if i==0:
			idle_1[i] = 0
			idle_2[i] = 0
		else:
			idle_1[i] = start_1[i] - finish_1[i-1]
			idle_2[i] = start_2[i] - finish_2[i-1]

	print("Cust#\tIAT\tAT\tSt_1\tSer_1\tFT_1\tWt_1\tIdle_1\tSt_2\tSer_2\tFT_2\tWT_2\tIdle_2\tTotal")
	for i in range(0,N):
		print(i,"\t", iarr_t[i],"\t", at[i],"\t",start_1[i],"\t",nurse, "\t", finish_1[i],"\t", wait_1[i], "\t",idle_1[i], end="\t")
		print(start_2[i],"\t", ser_t[i], "\t", finish_2[i],"\t",wait_2[i], "\t",idle_2[i], "\t",tot_sys[i])

	print("Average Waiting Time of patient= ", (sum(wait_1)+sum(wait_2))/(2*N))
	avg_wait_time.append((sum(wait_1)+sum(wait_2))/(2*N))

avg_delay = sum(avg_wait_time)/len(avg_wait_time)
n=10
total = 0
for i in avg_wait_time:
	total = total + ((i - avg_delay)*(i - avg_delay))
var = float(total/(n-1))
sd = math.sqrt(var)

t_table = 2.262 # 0.025 and 9
mu0 = 4.3
#t_table = float(input("Enter table value: "))
alpha = 0.05
print ("critical value at (",alpha/2,",",n-1,"): ",t_table)
t0 = (avg_delay - mu0) / (sd/math.sqrt(n))
print("t0 value: ",t0)
if t0<t_table:
	print("Accept")
else:
	print("Reject")
