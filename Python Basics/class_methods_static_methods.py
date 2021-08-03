from datetime import date

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Hi! My name is {self.first_name} {self.last_name}. I am {self.age} years old"

    @classmethod
    def anonymous(cls, first_name, last_name, year):
        return cls(first_name, last_name, date.today().year - year)

    @staticmethod
    def isAge(age):
        if age > 21:
            return "You are old"

print(Person("Dan", "Marley", 25).introduce())
print(Person("Dan", "Marley", 25).get_full_name())

print(Person.anonymous("Jon", "Doe", 1995).introduce())
print(Person.anonymous("Jon", "Doe", 1995).get_full_name())

print(Person.isAge(24))