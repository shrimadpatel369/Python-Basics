#2. Write a Python program that asks the user to enter a text
#and return a dictionary whose keys are the words of the text
#entered and the values are the lengths of the words that make
#up the text. Example for the text T = "Python is a programming language", 
#the program must return the dictionary.
#d = {'Python': 6, 'is': 3, 'a': 3, 'language': 7, 'de': 2, 'programming': 13}
T = input("Enter any one word:")
listWords = T.split(' ')
mydict=({})

for word in listWords:
    mydict[word] = len(word)
print(mydict)
