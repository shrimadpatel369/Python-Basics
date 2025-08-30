#Convert two list into a dictionary.
Keys = ["Ten", "Twenty", "Thirty"]
Values = [10, 20, 30]
mydict = {
}
for i in range (len(Keys)):
                mydict.update({Keys[i]:Values[i]})
print(mydict)

