#Q4.Calculate the cost of painting the buildin's walls

#Input cost of interior,exterior and input area too
interior = int(input('Enter interior cost:'))
exterior = int(input('Enter exterior cost:'))
area = float(input('Enter area:'))

#Calculating  cost of painting
inte_cost = 4 * interior
exte_cost = 3 * exterior
tot_cost = inte_cost + exte_cost

print('Interior painting cost =',inte_cost)
print('Exterior painting cost =',exte_cost)
print('Cost of painting the buildings walls =',tot_cost)