class Employee:
    company = "ITserve"

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


_a = Employee("Safikul", 29)
_b = Employee("Bellal", 24)

print(_a.name, _a.age)
print(_b.name, _b.age)

print(Employee.company)
print(_a.__class__.company)
print(_b.__class__.company)

# ----------------------------------------- #
# class Employee:
#     pass


# employee = Employee()
# employee.name = "Safikul"
# employee.age = 29

# print(f"{employee.name} is {employee.age} years old")
# print("{0} is {1} years old".format(employee.name, employee.age))
