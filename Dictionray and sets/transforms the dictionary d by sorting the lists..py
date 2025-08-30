#7. Given a dictionary d whose key values are lists. Write a Python program that transforms the dictionary d by sorting the lists. Example for the dictionary.
d = {'a1': [21, 17, 22, 3], 'a2': [11, 15, 8, 13], 'a3': [7, 13, 2, 11], 'a4': [22,14,7,9]}
#Expected Output:
#d = {'a1': [3, 17, 21, 22], 'a2': [8, 11, 13, 15], 'a3': [2, 7, 11, 13], 'a4': [7, 9, 14, 22]}
for key,value in d.items():
    value.sort()
    d[key] = value
    print(d)
