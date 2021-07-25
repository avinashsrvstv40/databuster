class student:
    college = 'XYZ' # class variable
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print("Name of the student is ", self.name)
        print("Roll no of the student is ", self.rollno)
        print("college name is ", student.college)

s1 = student("Ash", 12123)
s1.display()

s2 = student("Opera", 3423)
s2.display()