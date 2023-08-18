class country:
    def __init__(self, name, pop, area):
        self.name = name
        self.population = pop
        self.area = area


obj1 = country("India", 1400000000, 420)
print(obj1.name)
print(obj1.population)
print(obj1.area)
