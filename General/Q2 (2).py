#Q2. Sum of the series (Using for Loop)
x=float(input('enter the value of x :'))

n=int(input('enter a value for n(for x**n):'))
s=0
for a in range(n+1):
    s+=x**a
print('sum of first',n,'terms :',s)
