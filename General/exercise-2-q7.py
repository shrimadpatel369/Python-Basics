#This program check whether a number is divisible by 5 and 11
x=int(input('type a number: '))
if x%5==0 and x%11==0:
    print(x,'is divisible by 5 and 11')
elif x%5==0:
    print(x,'is divisible by 5')
elif x%11==0:
     print(x,'is divisible by 11')
else:
    print(x,'is not divisible by 5 and 11')
    
    
