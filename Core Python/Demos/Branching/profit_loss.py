CP = int(input('Enter Cost Price:'))
SP = int(input('Enter Selling Price:'))

amount = SP - CP

if(amount > 0):
    print('Profit')
elif(amount == 0):
    print('No Profit No Loss')
else:
    print('Loss')