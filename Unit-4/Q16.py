class Twosum:
    def __init__(self, target, lst):
        self.numbers = lst
        self.target = target

    def duplet(self):
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if (i != j) and (self.numbers[i] + self.numbers[j] == self.target):
                    return i, j
        return "Doesn't exist from the given list"


obj1 = Twosum(50, [10, 20, 10, 40, 50, 60, 70])
print(obj1.duplet())
