class person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Hello", self.name)

person("Avinash").display()