"Using property function"

class Details:

    def __init__(self):
        self._age = 0

    def get_age(self):
        print("getter method callled")
        return self._age
    
    def set_age(self, a):
        print("setter method is called")
        self._age = a

    def del_age(self):
        print("delete method is called")
        del self._age

    age = property(get_age, set_age, del_age)

mark = Details()
mark.age = 10
print(mark.age)
del mark.age



"Using property decorator"

class Details1:

    def __init__(self):
        self._age = 0

    @property
    def age(self):
        print("getter method is called")
        return self._age

    @age.setter
    def age(self, a):
        print("Setter method is called")
        self._age = a

    @age.deleter
    def age(self):
        print("Delete method is called")
        del self._age

mark1 = Details1()
mark1.age = 10
print(mark1.age)
del mark1.age
