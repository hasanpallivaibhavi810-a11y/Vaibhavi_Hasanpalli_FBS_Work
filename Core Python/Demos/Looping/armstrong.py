num = int(input('Enter a number:'))
temp = num
count = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    count += 1
print('Total count=',count)