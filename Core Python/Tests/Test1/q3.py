#Q3. Write a program to accept distance in km and conert it into meters and centimeters both

#Input distance
distance = int(input('Enter distance in km:'))

#Converting distance into meters and centimeters
meters = distance * 1000
centimeters = meters * 100

#Displaying result
print('Distance in meters =',meters)
print('Distance in centimeters =',centimeters)