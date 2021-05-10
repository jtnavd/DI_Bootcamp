
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(self.name + ' goes woof!')
    def jump(self):
        print(f"{self.name}, is {self.height}cm, he can jump {self.height * 2} high " )

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

davids_dog.jump(), davids_dog.bark()
sarahs_dog.jump(), sarahs_dog.bark()

if sarahs_dog.height > davids_dog.height:
    print(f'{sarahs_dog} is bigger than {davids_dog}')
else:
    print(f'{davids_dog} is bigger than {sarahs_dog}')