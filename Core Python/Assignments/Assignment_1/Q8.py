#8. Write a Program to convert days into years, weeks and days

#Take input
days = int(input('Enter days:'))

#Perform Operations
#1.Calculate Years
years = days // 365
days = days % 365

#2.Calculate Weeks
weeks = days // 7

#3.Calculate Days
days = days % 7

print(f'YEARS:{years}, WEEKS:{weeks}, DAYS:{days}')