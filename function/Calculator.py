#calculator
Perform = int(input("Enter from 1 to 4 what you want to perform(add, subtract, multiply, divide ):"))
Number1 = int(input("Enter any one number:"))
Number2 = int(input("Enter any one number:"))
def main():
    calculation()
def calculation():
    if Perform == 1 :
        addition()
    elif Perform == 2:
        subtraction()
    elif Perform == 3:
        multiplication()
    elif Perform == 4:
        division()
    else:
        print("error")
def addition():
    result = Number1 + Number2
    print(result)
def subtraction():
    result = Number1 - Number2
    print(result)
def multiplication():
    result = Number1 * Number2
    print(result)
def division():
    result = Number1 / Number2
    print(result)
main()
