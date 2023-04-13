class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*(self.radius**2)
    def perimeter(self):
        return 2*3.14*self.radius
    def display(self):
        print(f"The area of the circle is ", self.area(), "and the perimeter is ", self.perimeter())

circleradius = Circle(float(input("Enter the radius here: ")))
circleradius.display()
