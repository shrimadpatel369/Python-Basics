x=int(input("Enter any Integer:"))
first=0
second=1
print(first)
print(second)
for a in range(1,x):
    third=first+second
    print(third)
    first,second=second,third
    