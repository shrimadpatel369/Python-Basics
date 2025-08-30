#number pattern
#1
#2 3
#4 5 6
x=int(input("enter the number of rows:"))
num=1
for row in range(1,x+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print()
    

