class water_animal:
    def printing(self):
        print("This is water animal")
    
class land_animal:
    def display(self):
        print("This is land animal")

class frog(water_animal, land_animal):
    pass

f1 = frog()
f1.display()
f1.printing()