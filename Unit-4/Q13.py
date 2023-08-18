class roman:
    def __init__(self):
        self.symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def conv(self, rom):
        self.rom = rom[::-1]
        sum = 0
        prev = 0
        for i in range(len(self.rom)):
            if self.symbols[self.rom[i]] < prev:
                sum -= self.symbols[self.rom[i]]
            else:
                sum += self.symbols[self.rom[i]]
            prev = self.symbols[self.rom[i]]
        return sum


obj1 = roman()
print(obj1.conv("MMXXIII"))
