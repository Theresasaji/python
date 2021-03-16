class Rectangle:
    def __init__(self,length ,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print("Area of Rectangle: "+ str(area) + "m^2")

    def __lt__(self, other):
       a1 = self.length * self.width
       a2 = other.length * other.width
       if a1 < a2:
          print("The greater is the second one")
       else:
          print("The greter is the first one")
leng1 = int(input("Enter length of First Rectangle:"))
wid1 = int(input("Enter bredth of First Rectangle:"))
leng2 = int(input("Enter length of Second Rectangle:"))
wid2 = int(input("Enter bredth of Second rectangle:"))

rect1 = Rectangle(leng1,wid1)
rect2 = Rectangle(leng2,wid2)
print("FIRST RECTANGLE\n")
rect1.area()
print("\nSECOND RECTANGLE\n")
rect2.area()
print(rect1 < rect2)