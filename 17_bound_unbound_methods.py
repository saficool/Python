class Name:
    def __init__(self) -> None:
        self.name = "Safikul Islam"

    def getname(self):
        return self.name


name = Name()
print(name.getname())
print(Name.getname(name))
