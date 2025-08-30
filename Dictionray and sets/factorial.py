#5. Write a python program that asks the user to enter an integer n
#and return a dictionary whose keys are integers 1, 2, 3, ... n and
#whose values are 1! , 2! , 3! , ... , n! (Using Function and Dictionary).
Number = int(input("Enter any one number:"))
dict1={}
for Number in range(1,Number+1):
    y = 1
    for Number in range(1,Number+1):
        y *= Number
    dict1[Number] = y
print(dict1)
