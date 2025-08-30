#number pattern
#8  
#8 6
#8 6 4

for row in range(8,0,-1):
    for col in range(8,row,-1):
        print(col,end="  ")
    print()
