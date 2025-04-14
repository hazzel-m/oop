class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def display_info(self):
        return f"{self.name} is {self.age} years old"

class Elephant(Animal):
    def __init__(self, name, age, make_sound):  
        super().__init__(name, age)
        self.make_sound = make_sound

    def trumpet(self):
        return f"{self.name} trumpets!"

class Lion(Animal):
    def __init__(self, name, age, make_sound):
        super().__init__(name, age)
        self.make_sound = make_sound

    def roar(self):
        return f"{self.name} roars!"
    

lion = Lion("Simba", 12, "Roar")
elephant = Elephant("Dumbo", 5, "Trumpet")


zoo = [lion, elephant]

for animal in zoo:
    print(animal.display_info())
    print(animal.make_sound)  
    print()





