#maximum of two values
int_1=int(input("enter the 1st variable:"))
int_2=int(input("enter the 2nd variable:"))

def max(int_1,int_2):
    if int_1>int_2:
        print("The number",int_1,"is greater than",int_2,".")
    elif int_1<int_2:
        print("The number",int_2,"is greater than",int_1,".")
    else:
        print("They are equal.")

max(int_1,int_2)

