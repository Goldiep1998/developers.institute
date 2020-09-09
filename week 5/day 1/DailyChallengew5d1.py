class Farm():
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}
                
    
    def add_animal(self, animal, amount=1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.add_animal[animal] = amount

    def display_info(self):
        print(f"{self.farm_name}'s Farm")
        for key, value in self.animals.items():
    		print(f"{key}\t\t\t: {value}")
		print("\tE-I-E-I-O")
​
	def get_animal_types(self):
		animals = list(self.animals.keys())
		animals.sort()
		return animals


        
        
