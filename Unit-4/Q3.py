class student:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.admission = ""

    def set(self, name, gender):
        self.name = name
        self.gender = gender

    def set(self, name, gender, admission):
        self.name = name
        self.gender = gender
        self.admission = admission

    def prt(self):
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("Admission number: ", self.admission)


obj1 = student()
obj1.set("Tejas", "Male", "MC17")
obj1.prt()
