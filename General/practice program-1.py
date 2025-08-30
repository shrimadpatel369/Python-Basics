#This program is about roulette colors
x=int(input('no. of pockets-->'))
if x==0:
      print('green')
elif x>=1 and x<=10:
      if x%2==0:
            print('black')
      else:
            print('red')
elif x>=11 and x<=18:
      if x%2==0:
            print('red')
      else:
            print('black')
elif x>=19 and x<=28:
      if x%2==0:
            print('black')
      else:
            print('red')
elif x>=29 and x<=36:
      if x%2==0:
            print('red')
      else:
            print('black')
else:
      print('error')
            
            
      

            
      

            
            

      
