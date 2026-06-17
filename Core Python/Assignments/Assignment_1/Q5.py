#5. Write a program to enter P, T, R and calculate Compound Interest. 

#Input Principal, Time and Rate
p = int(input('Enter Principal Amount:'))
t = float(input('Enter time in years:'))
r = float(input('Enter rate:'))

#Calculating Compound Interest
CI = p * ((1 + r/100)**t)-p

#Displaying result
print('Compound Interest =',CI)