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

park = Zoo('ramat_gan_safari')
park.add_animal('Giraffe')
park.add_animal('Elephant')
park.add_animal('Lion')
park.add_animal('Flaming')
park.add_animal('Parrot')
