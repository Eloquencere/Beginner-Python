class rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print(self.l * self.b)

    def perimeter(self):
        print(2 * (self.l + self.b))


obj1 = rectangle(5, 3)
obj1.area()
obj1.perimeter()
