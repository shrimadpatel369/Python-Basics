#paint job estimator
space=float(input("enter the area required for wall in square feet:"))
prize=float(input("enter the prize of the paint per gallon :"))

def main(space,prize):
    paint_required=space/112
    hours_required=paint_required*8
    cost=prize*paint_required
    labour_charge=hours_required*35
    total_cost=cost+labour_charge
    print("The no.of gallons of paint required is",paint_required)
    print("The no.of  hour required is", hours_required)
    print("The cost of paint required is $",cost)
    print("The labour charges is $", labour_charge)
    print("The total is $", total_cost)

main(space,prize)


    

    
    
