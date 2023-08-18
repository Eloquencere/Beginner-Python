class strings:
    def __init__(self):
        self.str1 = ""

    def get_String(self, s):
        self.str1 = s

    def print_String(self):
        print((self.str1).upper())


obj1 = strings()
obj1.get_String("Batman")
obj1.print_String()
