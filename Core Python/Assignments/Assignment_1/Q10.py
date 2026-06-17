#10.Write a program to calculate area of an equilateral triangle.

#Input length of ane side of the triangle

a = float(input('Enter length of one side of triangle:'))

#Calculate area
area = ((3 ** 0.5)/ 4) * a * a   

#Display Area
print('Area of equilateral triangle =',area)