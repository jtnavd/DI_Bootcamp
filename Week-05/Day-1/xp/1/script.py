
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cat_info (self):
        print(f"The oldest cat is {self.name}, and is {self.age} years old.")

    def cat_name(self, new_name):
        self.name = new_name
        print("my name ")


cat1 = Cat("Garfield",9)
cat2 = Cat("Tom",3)
cat3 = Cat("Jerry",7)

cat1.cat_info()
cat2.cat_info()
cat3.cat_info()
# r1.introduceSelf()
# r2.introduceSelf()