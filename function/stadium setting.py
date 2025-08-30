#stadium seating
class_a=int(input("enter the no.of tickets sold of class A:"))
class_b=int(input("enter the no.of tickets sold of class B:"))
class_c=int(input("enter the no.of tickets sold of class C:"))

def total_cost(class_a,class_b,class_c):
    amount_of_income=class_a*20+class_b*15+class_c*10
    print("The amount of income generated from tickets sales is $",amount_of_income)

total_cost(class_a,class_b,class_c)



