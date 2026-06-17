name = 'Ram'
pasword = '1234'

username = input('Enter username:')
password = input('Enter password:')

if username == name and password == pasword:
    print('Login Successful')

else:
    print('Invalid Login Credentials')