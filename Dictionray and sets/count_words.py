#4. Write a Python program that asks the user to enter a string,
#and return him a dictionary whose keys are the characters in the
#string entered and the values are the number of occurrences of the
#characters in the string. Example if the entered string is s = 'language',
#the program returns the dictionary.
#d = {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'e': 1}
Text = input("Enter any one word:")
mydict=dict({})

for x in Text:
    mydict[x] = Text.count(x)
print(mydict)


