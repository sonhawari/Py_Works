class Animal():
    def __init__(self):
        print("animal created")
    def whoAmi(self):
        print("animal")

    def eat(self):
        print("eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self):
        print("dog created")

mya = Anima()
mya.whoAmi()
mya.eat()
