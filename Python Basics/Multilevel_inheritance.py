class animal:
    def __init__(self, name):
        self.name = name

class dog(animal):
    def bark(self):
        print(self.name)

d = dog("yoshu")
d.bark()