class Zoo():
    def __init__(self, name, animal=[]):
        self.name = name
        self.animal = animal

    def add_animal(self, animal_added):
        if animal_added not in self.animal:
            self.animal.append(animal_added)
    
    def find_animal(self):
        print(self.animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animal:
            set.animal.remove(animal_sold)
    
    def sort_animals(self):
        self.animal.sort()
        category_list = {}
        key = 0
        for i in self.animal:
            if not category_list:
                key +=1
                category_list[1]=[i]
            elif a[0] in category_list.get(key)[0][0]:
                category_list[key].append(i)
            else:
                key+=1
                category_list[key]=[a]
            
        print(category_list)
        return category_list

    def make_group(self, category_list):
        for a in category_list.values():
            print(a)

park = Zoo('Safari Ramat Gan')
park.add_animal('Elephant')
park.add_animal('Lion')



# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)