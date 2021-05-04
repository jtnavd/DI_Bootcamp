import script.Dog

class PetDog(Dog):
    def __init__(self, trained):
        self.trained = False
    
    # train function
    def train(self):
        self.trained = True
        self.bark()

# # train: prints the output of bark and switches the trained boolean to True


#     # def play(self):

#     # def do_a_trick(self):

# new_dog1.train()

# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other dogs (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.