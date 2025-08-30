#Q12
a=int(input("Enter one side of the triangel:"))
b=int(input("Enter one side of the triangel:"))
c=int(input("Enter one side of the triangel:"))
if a==b==c:
    print("It is a equilateral triangle")
elif a==b!=c or a==c!=b or b==c!=a:
    print("It is a isosceleus triangle")
else:
    print("It is a scalene triangle")
    
    
