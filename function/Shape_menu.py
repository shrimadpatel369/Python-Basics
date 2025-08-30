#menu
Shape = int(input("Enter the number from 1 to 8:"))
def main():
    calculation()
def calculation():
    if Shape == 1:
        Square()
    elif Shape == 2:
        rectangle()
    elif Shape == 3:
        circle()
    elif Shape == 4:
        triangle()
    elif Shape == 5:
        cube()
    elif Shape == 6:
        cuboid()
    elif Shape == 7:
        cylinder()
    elif Shape == 8:
        semicircle() 
    else:
        print("Error")
    
def Square():
    length = int(input("Enter the length of square:"))
    print("The area of Square is ",length * length)
def rectangle():
    length = int(input("Enter the length of rectangle:"))
    breath = int(input("Enter the breath of rectangle:"))
    print("The area of Rectangle is ",length * breath)
def circle():
    radius = int(input("Enter the radius of circle:"))
    print("The area of Circle is", 22/7 * radius ** 2)
def triangle():
    base = int(input("Enter the base of triangle:"))
    height = int(input("Enter the height of triangle:"))
    print("The area of Triangle is ",1/2 * base * height)
def cube():
    length = int(input("Enter the length of cube:"))
    print("The area of cube is ",length * 3)
def cuboid():
    height = int(input("Enter the height of cuboid:"))
    length = int(input("Enter the length of cuboid:"))
    breath = int(input("Enter the breath of cuboid:"))
    print("The area of cuboid is ",length * breath * height)
def cylinder():
    radius = int(input("Enter the radius of cylinder:"))
    print("The area of cylinder is ",22/7 * radius **2)
def semicircle():
    radius = int(input("Enter the radius of semicircle:"))
    print("The area of semicircle is ",22/7 * radius **2/2)
    
main()


    
