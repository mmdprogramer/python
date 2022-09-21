# this module is for Mathematics Calculation:
import math
###############
value_error = 'invalid number!!'
# Filtering floatable inputted numbers:
def numbers_filter(x):
    try:

        # if inputted number is floatable

        x=float(x)
        return x
    except:

        # else if inputted number is not floatable

        print(value_error)
        Start()
# classes of shapes:

# Rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = numbers_filter(length)
        self.width = numbers_filter(width)
    def perimeter(self):
        print('perimeter:',(self.length+self.length)+ (self.width+self.width))
    def area(self):
        print('area:',(self.length)*(self.width))

#Circle
class Circle:
    def __init__(self,radius):
        self.radius = numbers_filter(radius)
    def perimeter(self):
        print('perimeter:',(self.radius*2)*math.pi)
    def area(self):
        print('area:',(self.radius ** 2)*math.pi)

# Trapezius
class Trapezius:
    def __init__(self, side1,side2,side3,side4):
        self.side1 = numbers_filter(side1)
        self.side2 = numbers_filter(side2)
        self.side3 = numbers_filter(side3)
        self.side4 = numbers_filter(side4)
    def perimeter(self):
        print('perimeter:',self.side1+self.side2+self.side3+self.side4)
    def area(self):
        print('area:',((self.side1+self.side2) * self.side3)/2)

# Square
class Square:
    def __init__(self, side):
        self.side = numbers_filter(side)
    def perimeter(self):
        print('perimeter:',(self.side) * 4)
    def area(self):
        print('area:',(self.side) ** 2)

# triangle
class triangle:
    def __init__(self,side1,side2,side3):
        self.side1 = numbers_filter(side1)
        self.side2 = numbers_filter(side2)
        self.side3 = numbers_filter(side3)

    def perimeter(self):
        print('perimeter:',(self.side1)+(self.side2)+(self.side3))
    def area1(self):

        # { Heron's formula }

        s = (((self.side1) + (self.side2) + (self.side3)) / 2)
        area = math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
        Height = ((area*2)/self.side2)
        print('area:',area)
        print("Height:",Height)
    def area2(self):
        print('area:',(self.side1 * self.side2) / 2)

#############################################################################################

# inputs and returns

def Start():
    b=input('select 1_"triangle",2_"square",3_"trapezius",4_"circle",5_"rectangle":')
    if b=='1':
        a = input("you want Triangle's 1_'perimeter' or 2_'area'? :")
        if a == '2':
            a = input("do you know Triangle's Height? 1_'yes' 2_'no':")
            if a == '2':
                x = triangle(input("enter Triangle's side1:"), input('side2(base):'),
                             input('side3:'))
                x.perimeter()
                x.area1()
                Start()
            elif a == '1':
                x = triangle(input('enter Height:'), input('enter base:'), 0)
                x.area2()
                Start()
        elif a == '1':
            x = triangle(input("enter Triangle's first sides:"), input('side2(base):'),
                         input('side3:'))
            x.perimeter()
            x.area1()
            Start()
        if a != '1' and a != '2':
            print('invalid number!')
            Start()
    elif b=='2':
        x = Square(input("enter Square's side:"))
        x.perimeter()
        x.area()
        Start()
    elif b=='3':
        a = input("you want Trapezius's 1_'perimeter' or 2_'area'? :")
        if a == '2':
            x = Trapezius(input("enter base1:"), input('base2:'), input('height:'), 0)
            x.area()
            Start()
        elif a == '1':
            x = Trapezius(input("enter trapezius's side_1:"),input("enter trapezius's side_2:"),
                          input("enter trapezius's side_3:"),input("enter trapezius's side_4:"))
            x.perimeter()
            Start()
        elif a != '1' and a != '2':
            print('invalid number!!')
            Start()
    elif b=='4':
        x = Circle(input("enter Circle's radius:"))
        x.perimeter()
        x.area()
        Start()
    elif b=='5':
        x = Rectangle(input("enter Rectangle's length:"), input('enter width:'))
        x.perimeter()
        x.area()
        Start()
    else:
        print('invalid number!')
        Start()
Start()