#This program is about shipping charges
x=float(input('the weight of package-->'))
if x==0:
      print('$0 is the shipping charge')
elif x>=1 and x<=2:
      print('$1.50 is the shipping charge')
elif x>=3 and x<=6:
      print('$3.00 is the shipping charge')
elif x>=7 and x<=10:
      print('$4.00 is the shipping charge')
elif x>=11 :
      print('$4.75 is the shipping charge')
else:
      print('error')
            
