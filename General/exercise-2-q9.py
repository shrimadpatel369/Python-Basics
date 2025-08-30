#This program check whether it is vowel or consonant
x=input('type any alphabet:')
vowel=['a','e','i','o','u']
vowel1=['A','E','I','O','U']
if x in vowel:
    print(x,'is a vowel')
elif x in vowel1:
    print(x,'is a vowel')
else:
    print(x,'is a consonant')
