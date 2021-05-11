class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} barking!')

    def speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.speed() > other_dog.speed():
            print(f'{self.name} win the fight!')
        elif self.speed() < other_dog.speed():
            print(f'{other_dog.name} win the fight!')
        else:
            print('Its a tie!')

dog_1 = Dog("Scoobedo", 6, 28)
dog_2 = Dog("Milou", 5, 14)
dog_3 = Dog("Idefix", 7, 10)
dog_1.speed()
dog_2.speed()
dog_3.speed()
dog_1.fight(dog_2)
dog_1.fight(dog_3)
dog_2.fight(dog_1)
dog_2.fight(dog_3)
dog_3.fight(dog_1)
dog_3.fight(dog_2)