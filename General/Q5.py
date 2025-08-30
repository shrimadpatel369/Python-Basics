abc=eval(input("enter the list of numbers:"))
list1=[]
total=0
for n in abc:
    if n%2==0:
        list1.append(n)
        total=total+n
print(total)
prize=0
for n in abc:
    if n%2!=0:
        list1.append(n)
        prize=prize+n
print(prize)
print(prize-total)    
