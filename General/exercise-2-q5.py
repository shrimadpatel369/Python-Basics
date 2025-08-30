#This program check whether the triangle is equilateral,isosceles or scalene
side1=float(input('type a side of triangle: '))
side2=float(input('type a side of triangle: '))
side3=float(input('type a side of triangle: '))
if side1<=0 or side2<=0 or side3<=0:
    print('triangle is not valid')
elif side1== side2== side3:
    print('Equilateral Triangle')
elif side1==side2 or side2==side3 or side3==side1:
    print('IsosceleusTriangle')
else:
    print('scalene Triangle')
