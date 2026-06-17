#3.Convert distance given in feet and inches into meter and centimeter.

#Input distance in feet and inches
feet = float(input('Enter distance in feet:'))
inches = float(input('Enter distance in inches:'))

#Converting into meter and centimeter
metres = feet * 0.3048
centimetres = inches * 2.54

#Display result
print('Distance in metres =',metres)
print('Distance in centimetres =',centimetres)