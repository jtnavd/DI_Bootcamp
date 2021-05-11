import Family

class TheIncredibles(Family):
    def power(self, name):
        for i in self.members:
            if i['name'] == name:
                if i['age'] >= 16:
                    return f"{name}'s super power is {['power']}"
                else:
                    return f'{name} is minor'
    def incredibles_family(self):
        print(f"Here's the Incredibles family members: {self.last_name}")
        out_str = ' '

        for i in self.members:
            out_str += (f"{set['name']} or {set['incredibles_name']}")
        return out_str

incredibles_original_members = [
     {'name':'Graig','age':43,'gender':'Male','is_child':False,'power':'iron_man','incredible_name':'Mr. Incredible'},
     {'name':'Holly','age':39,'gender':'Female','is_child':False,'power':'elastic_body','incredible_name':'Elastigirl'},
     {'name':'Spencer','age':8,'gender':'Male','is_child':True,'power':'speed_move','incredible_name':'Dash'},
     {'name':'Sarah','age':15,'gender':'Female','is_child':True,'power':'invisibilty','incredible_name':'Violet'}
]

family_1 = TheIncredibles(incredibles_original_members, 'Parr')
print(family_1)

incredibles_new_members = [
      {'name':'Jack','age':1,'gender':'Male','is_child':True,'power':'fire_emitter','incredible_name':'Jack'}
]
family_1.born(incredibles_new_members)
print(family_1)
print(family_1.incredibles_family())
for m in family_1.members:
    print(family_1.power(m['name'])