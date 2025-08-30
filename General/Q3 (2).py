
#Q3. Admission Price (Using While Loop)
#prize defined
baby_prize=0.00
childern_prize=14.00
adult_prize=23.00
seniorcitizen_prize=18.00
#age defined
baby_limit=2
childern_limit=12
adult_limit=65

total=0
age=input("enter your age of the member of the group :")

while age!="":
    age=int(age)
    
    #it will calculate the cost
    if age<=baby_limit:
        total=total+baby_prize
        
    elif age<=childern_limit:
        total=total+childern_prize
        
    elif age<=adult_limit:
        total=total+adult_prize
        
    else:
        total=total+seniorcitizen_prize
        
    age=input("enter your age of the member of the group :")
    
print("the cost for the guest is",total)
    
        
    





    
    
    
    
