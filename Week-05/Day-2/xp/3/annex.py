import Dog
from random import choice

class PetDog(Dog):
    def __init__(self,name,age, weight,trained=False):
        super().__init__(name,age,weight)
        self.trained = trained
    
    def train(self):
        self.bark(self)
        self.trained = True

    def play(self, *args):
        list_dog = [self.name]
        for i in args:
            list_dog.append(i.name)
        print('\n'.join(list_dog)+'play together')

    def do_a_trick(self):
        trick_list = [' do a barrel roll',' stands on back legs',' gives paw', ' plays dead']
        if self.trained:
            print(f'\n{self.name}{choice(trick_list)}\n')

dog_4=PetDog('Robert',6,16)
dog_5=PetDog('Nikita',12,22,True)
dog_6=PetDog('Bradd',5,12,True)
dog_5.play(dog_6)
dog_6.trained()
dog_6.do_a_trick()