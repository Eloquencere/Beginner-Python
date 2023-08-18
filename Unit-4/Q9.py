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


obj1 = Twosum(-4, [5, -3, 10, 100, 34, 65, -69, -14, -56])
print(obj1.duplet())
