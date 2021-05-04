class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    # Barkin function
    def bark(self):
        print(f"{self.name} is barking !")
    # Run Speed function
    def run_speed(self):
        speed = (self.weight / self.age) * 10
        print(speed)
        return speed
    # Fight function
    def fight(self, dog_speed):    
        is_stronger = dog_speed * self.weight
        print(is_stronger)
        return is_stronger
        if self.is_stronger(True):
            print(f"{self.name} won the fight!")


new_dog1 = Dog("Scoo", 4, 13)
new_dog2 = Dog("Bee", 6, 9)
new_dog3 = Dog("Doo", 7, 16)
other_dog = Dog("Bulldog", 5, 11)

new_dog2.run_speed()
other_dog.run_speed()

print(new_dog1.fight(new_dog1.run_speed()))

# Implement the following methods in the Dog class: 
# bark: returns a string which states: “<dog_name> is barking”.        
# run_speed: returns the dogs running speed (weight/age*10).
# fight :takes a parameter which value should be another dog called other_dog, returns a string stating which dog won the fight. 
# The winner should be the dog with the higher run_speed x weight.
# Create 3 dogs and run them through your class.


