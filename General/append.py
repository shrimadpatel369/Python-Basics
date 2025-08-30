#Q15
list=[]
f=True
while True:
    a=int(input("Enter range of numbers:"))
    list.append(a)
    if a<=0:
        f=False
        break
    print(list)
list.sort(reverse=True)
print(list)

   

