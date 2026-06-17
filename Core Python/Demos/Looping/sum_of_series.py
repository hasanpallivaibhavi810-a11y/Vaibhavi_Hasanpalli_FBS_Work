#Write a program to print sum of series or sum of first n numbers
n = int(input('Enter value of n: '))
i = 1
sum = 0
while(i <= n):
    sum = sum + i
    i += 1
print('Sum:',sum)