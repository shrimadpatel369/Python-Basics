#3. Initialize dictionary with default values.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dict1={}
print(employees)
for i in range (len(employees)):
    #print(i)
    select_employee = int(input("Select any one employee(0,1):"))
    if select_employee == 0:
        dict1.update({"Kelly":defaults})
        print(dict1)
    elif select_employee == 1:
        dict1.update({"Emma":defaults})
        print(dict1)
        
