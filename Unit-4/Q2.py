class rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def disp(self):
        print("x=", self.x, ",", "y=", self.y)


obj1 = rocket(10, 56)
obj1.disp()
obj2 = rocket(9, -17)
obj2.disp()
obj3 = rocket(11, 22)
obj3.disp()
obj4 = rocket(-13, -7)
obj4.disp()
obj5 = rocket(4, -3)
obj5.disp()
