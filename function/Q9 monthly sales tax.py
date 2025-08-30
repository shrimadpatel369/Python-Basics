#monthly sales tax
total_sales=float(input("enter the total sales of the month:"))

def total_sales_tax():
    country_sales_tax=total_sales*0.025
    state_sales_tax=total_sales*0.05
    print("The amount of country sales tax is $",country_sales_tax)
    print("The amount of state sales tax is $",state_sales_tax)
    print("The amount of total sales tax is $",country_sales_tax+state_sales_tax)

total_sales_tax()
    
    

