#2. Write a program to calculate simple interest based on Principal,Rate and Time

#Input Principal,Rate and Time
P = int(input('Enter Principal Amount:'))
R = float(input('Enter Rate:'))
T = float(input('Enter time in years:'))

#Calculating Simple Interest
SI = P * T * R / 100

#Displaying result
print('Simple Interest =',SI )