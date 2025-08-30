def total_sales():
    list1=[]
    total=0
    for n in range (7):
        abc=int(input("enter the total sales of the day:"))
        list1.append(abc)        
        total=total+abc
    print(list1)
    print("'The total sales of week is",total)
total_sales()





