class Threesum:
    def __init__(self, lst):
        self.numbers = lst

    def triplet(self):
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                for k in range(j + 1, len(self.numbers)):
                    if (i != j != k) and (
                        self.numbers[i] + self.numbers[j] + self.numbers[k] == 0
                    ):
                        return self.numbers[i], self.numbers[j], self.numbers[k]
        return "Doesn't exist from the given list"


obj1 = Threesum([5, -3, 10, 100, 34, 65, -69, -14, -56])
print(obj1.triplet())
