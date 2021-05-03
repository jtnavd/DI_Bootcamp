class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

cat_list = []
cat_list.append(Bengal)
cat_list.append(Chartreux)
cat_list.append(Siamese)

print(Pets.walk(self))
# Create a list of all of the pets. Name the list my_cats = [].
# Instantiate the Pet class with all your cats. Use the my_pets variable.
# Take all the cats for a walk, use the walk method.