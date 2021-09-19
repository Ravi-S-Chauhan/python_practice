class Student:
    def __init__(self,name,roll):
        self.name= name
        self.roll = roll

    def show(self):
        print(self.name,self.roll)
        print()

    class laptop():
        def __init__(self,brand,cpu):
            self.brand = brand
            self.cpu = cpu
        def show(self):
            print(self.brand,self.cpu)

s1 = Student("ravi",14)
s1.show()
lap = s1.laptop("acer","i5")
lap.show()


