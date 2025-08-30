#3. Write a Python program that asks the user to enter a text
#and return him a dictionary whose keys are the words of the
#text entered and the values are the reverse of the words that
#make up the text. Example for the text T = "Python is easy",
#the program must return the dictionary.
#d = {'Python': 'nohtyp', 'is': 'si', 'easy': 'ysae'}
n = str(input("Enter any text:"))
listword = n.split(" ")
my_dict = ({})
for word in listword:
    reverseword = word[::-1]
    my_dict[word] = reverseword
print(my_dict)

