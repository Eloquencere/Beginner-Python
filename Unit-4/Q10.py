class strev:
    def __init__(self, string):
        self.string = string

    def rev(self):
        x = (self.string).split()
        print(" ".join(x[::-1]))


obj1 = strev("hello .py")
obj1.rev()
