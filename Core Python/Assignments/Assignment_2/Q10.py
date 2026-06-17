#10. Write a program to reverse three-digit number.

#Input a three digit number
num = int(input('Enter a three digit number: '))

#Perform operation
digit1 = num % 10
num = num // 10

digit2 = num % 10
num = num // 10

digit3 = num % 10
num = num // 10

reversed_num = (digit1 * 100) + (digit2 * 10) + (digit3)

#Display result
print('Reverses Number is ',reversed_num)
