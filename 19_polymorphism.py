class Animal(object):
    def __init__(self, name='') -> None:
        self.name = name

    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        print("Meow!")


class Dog(Animal):
    def talk(self):
        print("Woof!")


a = Animal()
a.talk()
c = Cat("Micky")
c.talk()
d = Dog("Golden Retriver")
d.talk()
