#7.Program to Find the Roots of a Quadratic Equation  

#Take input from user
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

#Perform operation
d = b * b - (4 * a * c)

r1 = (-b + d ** 0.5)/(2*a)

r2 = (-b - d ** 0.5)/(2*a)

#Displaying result
print('Root 1 is:', r1)
print('Root 2 is:', r2) 

