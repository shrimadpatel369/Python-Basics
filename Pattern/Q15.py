for row in range(7):
    for col in range(7):
        if row==0 or row==6: 
            print("#",end="")
        elif row==col:
            print("#",end="")
        else:
            print(end=" ")
    print("")
        
        
        
