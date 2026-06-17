#5. WAP to calculate selling price of book based on cost price and discount. 

#Input cost price and discount 
cost_price = float(input('Enter cost price of book: '))
discount = float(input('Enter discount percentage: '))

#calculate discount amount
dis_amount = (cost_price * discount) / 100

#Calculate selling price
selling_price = cost_price - dis_amount

#Display result
print('Selling price of book= ',selling_price)