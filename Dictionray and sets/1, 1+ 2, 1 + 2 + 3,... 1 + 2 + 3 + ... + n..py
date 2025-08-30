#1. Write a program in Python that asks the user to enter an integer n and
#return a dictionary whose keys are the integers 1, 2, 3, ... n and
#whose values are the sums 1, 1+ 2, 1 + 2 + 3,... 1 + 2 + 3 + ... + n.
#(Using Function and Dictionary)
Range = int(input("Enter any one number:"))
mydict = ({})
def main():
    calculation()
def calculation():
    for i in range (1,Range+1):
        y = 0
        for m in range (1,Range+1):
            y += m
            mydict[m]= y
    print(mydict)
    
main()



