#4. Delete a list of keys from a dictionary.
sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"
}
# Keys to remove
#keys = ["name", "salary"]
sample_dict.pop("name","salary")
print(sample_dict)
