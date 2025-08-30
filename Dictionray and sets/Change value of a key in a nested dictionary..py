#5. Change value of a key in a nested dictionary.
sample_dict = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 500}
}
#Expected Output:
#{
#'emp1': {'name': 'Jhon', 'salary': 7500},
#'emp2': {'name': 'Emma', 'salary': 8000},
#'emp3': {'name': 'Brad', 'salary': 8500}
#}
sample_dict.update({'emp3':{'salary',8500}})
print(sample_dict)
