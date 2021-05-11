class Family():
    def __init__(self,member,last_name):
        self.member = member
        self.last_name = last_name

    def __repr(self):
        print(f'\nFamily members : {self.last_name}')
        out_str = ''
        for i in self.member:
            out_str += (f"{set['name']}\n")
        return out_str

    def born(self, new_member):
        print(f'add new member to family: {self.last_name}')
        for i in self.member:
            self.member.append(i)
            print(f"{set['name']} is now a member of the family")

    def is_major(self, name):
        for i in self.member:
            if i['name'] == name:
                if i['age'] >= 18:
                    return True
                else:
                    return False
        return f"{name} is still minor"

original_members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

family_1 = Family(original_members, 'Smith')

new_members = [
    {'name':'John','age':0,'gender':'Male','is_child':True},
    {'name':'Lara','age':0,'gender':'Female','is_child':True}
]

print(family_1)
print("is Michael older than 18 : "+ str(family_1.is_major('Michael')))
print("is Lara older than 18 : "+ str(family_1.is_major('Lara')))
