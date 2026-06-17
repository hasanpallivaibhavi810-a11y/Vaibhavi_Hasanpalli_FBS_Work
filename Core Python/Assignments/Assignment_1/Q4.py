#4. Write a program to enter P, T, R and calculate simple Interest. 

#Input Principal, Time and Rate
P = int(input('Enter Principal Amount:'))
T = float(input('Enter Time in years:'))
R = float(input('Enter Rate:'))

#Calculating Simple Interest
SI = P * T * R / 100

#Displaying result
print('Simple Interest =',SI)