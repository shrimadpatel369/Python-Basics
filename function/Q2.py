def total_sales():
    list1=[1,2,3,4,5,6,7]
    sum=0                     
    for n in range (7):
        list1[n]=float(input("enter the total sales of the day:"))
        sum=sum+list1[n]
        print("The total sales is $",sum)
total_sales()
    
