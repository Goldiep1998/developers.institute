# class Family():

#     def __init__(self, members):
#        self.members = members 

#     def store_info(self, lastname):
#         for item in self.members:
#             item.update({"last_name":lastname})

#     def born(self, baby):
#         self.members.append(baby)
#         print(f"Congradulations on your baby, {self.members[2]['name']}!")
        
#     def is_18(self):
#         if self.members[0]['age'] > 18:
#            return True
#         else:
#             return False

#     def __repr__(self):
#       

    
# f = Family([ {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False} ])
# f.store_info("Smith") 
# f.born({"name": "Henry", "age": 0, "gender": "male", "is_child": True})
# f.is_18()
# f.repr()

    #2

class Family():
    
    def __init__(self, family):
       self.family = family

    def presentation(self):
        full_family = ""
        for member in self.family:
            full_family = member["name"] + " : " + str(member["age"])
            print(full_family)

    def add_child(self, child):
        self.family.append(child)  

jones = Family([{"name": "Ben", "age": 70, "gender": "male", "is_child": False}, {"name": "Heather", "age": 70, "gender": "female", "is_child": False}, 
{"name": "Barney", "age": 45, "gender": "male", "is_child": False}])       

jones.presentation()

class TheIncredibles(Family):

    def __init__(self, family):
        super().__init__(family)    
    
       
    def use_power(self, name):
        for member in self.family:
            if member['name'] == name:
                if member['age'] and member ['age'] < 18:
                    raise Exception("You have no power!") 
        else:
           print(self.family['power'])



    def i_presentation(self):
        full_family = ""
        for member in self.family:
            full_family = member["incredible name"] + " : " + member["power"]
            print(full_family)
            
        

incredibles = Family([{"name": "Bob", "age": 40, "gender": "male", "is child": False, "power": "strength", "incredible name": "mr incredible"}, 
{"name": "Helen", "age": 37, "gender": "female", "is child": False,"power": "flexable", "incredible name": "elastagirl"},
{"name": "Violet", "age": 14,"gender": "female", "is child": True , "incredible name": "none", "power": "Invisibility"},
{"name": "Dash", "age": 10, "gender": "male", "is child": True, "incredible name": "none", "power": "speed"}])

# TheIncredibles.use_power("Bob")

incredibles.add_child({"name": "Jack", "age": "0", "gender": "male", "is_child": True, "power": "uknown", "incredible name": "none"})
  
TheIncredibles.i_presentation(incredibles)

