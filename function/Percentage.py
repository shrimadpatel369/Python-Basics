#percentage using functions
def avg(n1,n2,n3):
    return(n1+n2+n3)/300 * 100


num1 = int(input("Enter the marks of subject 1:"))
num2 = int(input("Enter the marks of subject 2:"))
num3 = int(input("Enter the marks of subject 3:"))

main_result = avg(num1 , num2 , num3)

print("The percentage is",main_result)

        

