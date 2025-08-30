#Q6
a=int(input("Enter the side of a triangle:"))
b=int(input("Enter the side of a triangle:"))
c=int(input("Enter the side of a triangle:"))
if a+b>c or b+c>a or c+a>b:
    print("It is a triangle")
else:
    print("It is not a triangle")
    
