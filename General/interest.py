#Q11
#simple interest
p=int(input("enter the initial principle amount:"))
r=int(input("enter the interest rate:"))
t=int(input("enter the time period:"))
a=p*(1+r*t)
print(a)

#compund interest
p=int(input("enter the initial principle amount:"))
r=int(input("enter the interest rate:"))
t=int(input("enter the time period:"))
n=int(input("enter the number of times interest applied for time period:"))
a=p*(1+r/n)**n*t
print(a)
