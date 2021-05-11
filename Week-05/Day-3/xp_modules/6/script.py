from faker import Faker

users = []
faker = Faker()

for i in range(10):
    name= faker.name()
    address= faker.address()
    language= faker.language()
    set = {'name':name, 'address':address, 'language':language}
    print(set)
    users.append(set)