class circle:
    def __init__(self, r):
        self.r = r
        self.pi = 3.14159

    def area(self):
        print(self.pi * self.r**2)

    def perimeter(self):
        print(2 * self.pi * self.r)


obj1 = circle(5)
obj1.area()
obj1.perimeter()
