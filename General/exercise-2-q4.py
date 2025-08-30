#This program checks wheather it is a triangle or not
x=int(input('type a side of triangle:'))
y=int(input('type a side of triangle:'))
z=int(input('type a side of triangle:'))
if x<=0 or y<=0 or z<=0:
    print('Triangle is not valid')
elif x+y>z and y+z>x and z+x>y:
    print('Triangle is valid')
else:
    print('Triangle is not valid.......')
