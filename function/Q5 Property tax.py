#property tax
x=float(input("enter the toatl value of property:"))
def property_tax():
    property_tax=(x*60)/100
    assessment_value=property_tax*0.0072
    print("the cost of property tax is",property_tax)
    print("The cost of property tax and assessment value is",property_tax,"and",assessment_value,"respectively")
property_tax()    
    
