class person:
    def __init__(self, name):
        self.name = name    #Instance variable - self.name & local variable - name
    def display(self):
        print("Hello", self.name)

person("Avinash").display()