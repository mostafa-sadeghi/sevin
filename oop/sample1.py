class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        if self.gender == "boy":
            print(f"{self.name}, good boy EatUp!!")
        else:
            print(f"{self.name}, good girl EatUp!!")


    def bark(self, loud):
        if loud:
            print(self.name,"WOOF WOOF WOOF")
        else:
            print(self.name,"WOOF")

    
class Beagle(Dog):
    def __init__(self, name, age, gender, hunting):
        super().__init__(name, age, gender)
        self.hunting = hunting

    def hunt(self):
        print(f"{self.name} is hunting so good")

b1 = Beagle("jessi", 5, "girl", True)
b1.eat()
b1.hunt()