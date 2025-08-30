#number pattern
#1  
#2 4
#3 5 6
n=int(input("enter the number of rows:"))
for row in range(n):
    val=row+1
    dec=n-1
    for col in range(row+1):
        print(format(val,""),end="  ")
        val=val+dec
        dec=dec-1
    print()
