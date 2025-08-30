#This program checks wheather it is a triangle or not
x=int(input('type an angle of triangle:'))
y=int(input('type an angle of triangle:'))
z=int(input('type an angle of triangle:'))

if x>0 or y>0 or z>0:
    print('Triangle is not proper')
elif  x+y+z==180:
    print('Triangle is valid')
else:
        print('Triangle is not valid')
    
