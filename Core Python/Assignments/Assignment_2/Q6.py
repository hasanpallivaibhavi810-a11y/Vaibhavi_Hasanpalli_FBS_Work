#6. WAP to calculate total salary of employee based on basic, da=10% of basic, 
#ta=12% of basic, hra=15% of basic. 

#Input basic salary
basic_salary = int(input('Enter basic salary of employee: '))

#Calculate da
da = basic_salary * 10 / 100

#Calculate ta
ta = basic_salary * 12 / 100

#Calculate hra
hra = basic_salary * 15 / 100

#Calculate Total Salary
tot_salary = basic_salary + da + ta + hra

#Display result
print('Total salary of employee= ',tot_salary)