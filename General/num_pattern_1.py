#Q14
a=int(input("Enter anyone number n>20:"))
for a in range(11,a+1):
    if a%3==0 and a%7==0:
        print("TipsyTopsy")
    elif a%7==0:
        print("Topsy")
    elif a%3==0:
        print("Tipsy")
    else:
        print(a)
   
