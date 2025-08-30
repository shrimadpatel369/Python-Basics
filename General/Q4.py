def rainfall_statistics():
    list1=[1,2,3,4,5,6,7,8,9,10,11,12]
    sum=0                     
    for n in range (12):
        list1[n]=int(input("enter the total rainfall of month:"))
        sum=sum+list1[n]
        print("The total rainfall in a year is",sum)
rainfall_statistics()    

