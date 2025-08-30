#This program check whether it is alphabet,digit or special character
x=input('Enter a character : ')
if x>='A' and x<='Z':
    print('You entered a alphabet')
elif x>='a' and x<='z':
          print('You entered a alphabet')
elif x>='0' and x<='9':
    print('You entered a digit')
else:
    print('You entered a special character')
