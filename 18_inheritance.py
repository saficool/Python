class Animal:
    def __init__(self) -> None:
        print("Animal Class Created")

    def whoAmi(self):
        print("Animal")

    def eat(self):
        print('Eating')


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
        print('Dog Class Created')

    def whoAmi(self):
        print("Dog")

    def bark(self):
        print('Woof!')


dog = Dog()
dog.whoAmi()
dog.eat()
dog.bark()
