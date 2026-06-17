#1.Write a program to calculate the percentage of student based on marks of any 5 
#subjects. 

#Take input from user
subject1 = int(input('Enter marks of subject 1:'))
subject2 = int(input('Enter marks of subject 2:'))
subject3 = int(input('Enter marks of subject 3:'))
subject4 = int(input('Enter marks of subject 4:'))
subject5 = int(input('Enter marks of subject 5:'))

#Calculate percentage

total = subject1 + subject2 + subject3 + subject4 + subject5
percentage = total / 5

#Display result

print('Percentage =',percentage,'%')
