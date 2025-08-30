#Q2.Write a Python program to create the multiplication table (from 1 to 10) of a number, using a nested loop number.
#this program counts table
y=int(input('enter the number whose table you want :'))
x=y
for x in range (1,11,1):
    print(y,*'x',x,'=',x*y)
print('end of the loop')
