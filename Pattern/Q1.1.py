#Q1. Pattern (Using  Nested Loop): 
# we need to write the code to print the pattern
num=10
for num in range(1,num,2):
          for i in range(1,num+1,2):
                    print(i,end='   ')
          print('')
