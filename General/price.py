#Q2
a=int(input("Enter the number of items bought:"))
if a<10:
    price=120*a
    print("The price is",price)
elif a<99:
    price=100*a
    print("The price is",price)
elif a>=100:
    price=70*a
    print("The price is",price)
else:
    print("Enter valid input")
    
    
    
