#6. Write a Program to input two angles from user and find third angle of the 
#triangle. 

#input two angles
a1 = int(input('Enter first angle of the triangle:'))
a2 = int(input('Enter second angle of the triangle:'))

#Calculating third angle
a3 = 180 - (a1 + a2)

#Display result
print('Third angle of the triangle =',a3)