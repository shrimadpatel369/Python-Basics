#automobile cost
a=int(input("enter the loan payment of you automobile:"))
b=int(input("enter the insurance of you automobile:"))
c=int(input("enter the gas payment of you automobile:"))
d=int(input("enter the oil payment of you automobile:"))
e=int(input("enter the tiers payment of you automobile:"))
f=int(input("enter the maintenance payment of you automobile:"))
def monthly_cost():
    monthly_cost=a+b+c+d+e+f
    print(monthly_cost)
monthly_cost()
