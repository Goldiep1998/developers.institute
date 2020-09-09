#1

# class Cat():
#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
           


#     def find_oldest(*cat_ages):
#         oldest_c = 0
#         for age in cat_ages:
#             if age > oldest_c:
#                 oldest_c = age
#         print(f"The oldest cat is {oldest_c} years old.")

# c1 = Cat("Fluffy", 2)
# c2 = Cat("Tabby", 6)
# c3 = Cat("Scruffy", 1)
                   
# find_oldest(c1.age, c2.age, c3.age)
    
#2

# class Dog():

#     def __init__(self, namedog, heightdog):
#         self.name = namedog
#         self.height = heightdog
        
#     def talk(self):
#         print("woof!")


#     def jump(self):
#         jump = self.height*2
#         print(jump)

#     def print_names(self):
#         print(f"{self.name} {self.height}")

#     def biggest(self, *dogs):
#         dogslist = list(dogs)
#         tallest = 0
#         for dogs in doglist:
#             if dog.height > tallest:
#                 tallest = dog
#         return tallest
       
    
# d1 = Dog("Rover", 30)
# d1.talk()
# d1.jump()

# davids_dog = Dog("Rex", 50)
# davids_dog.print_names()

# sarahs_dog = Dog("Teacup", 20)
# sarahs_dog.print_names()

# biggest = biggest(sarahs_dog,davids_dog,d1)
# print(f"The biggest dog is {biggest}")

#3 

# class Song():
    
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
    
#     def sing_a_song(self):
#          for i in self.lyrics:
#             print(i)


# happy_birthday = Song(["Happy birthday to you.", "Happy birthday to you.", "Happy to blank, happy birthday to you"])
# happy_birthday.sing_a_song()

#4 nOT REALLY WORKING

class Zoo():
    def __init__(self, zoo_name, animals):
        self.zoo_name = zoo_name
        self.animals = animals
        self.animal_pen = {}

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)
    
    def sell_animals(self, animal_sold):
        print(f"Goodbye, {animal_sold}!")
        self.animals.remove(animal_sold)
    
    def sort_animals(self):
        self.animals.sort()
        i = 1
        current_letter = self.animals[0][0]
        self.animals_pen[i] = []
        for animal in self.animals:
            if animal[0] != current_letter:
                current_letter = animal[0]
                i += 1
                self.animals_pen[i] = [animal]
            else:
                self.animals_pen[i].append(animal)
    
    def get_pen(self):
        print(animals_pen)


animal_list = ["pig","monkey","lion"]
la_zoo = Zoo("Las Vagas zoo",animal_list)
la_zoo.add_animal("tiger")
la_zoo.sell_animals("pig")
la_zoo.get_animals()













# from random import randint

# class Math():
#     def __init__(self, num):
#         self.num = num

#     def add(self):
#         self.added_num = self.num + randint(0,25)  
#         return self.added_num

#     def multiply(self):
#         self.multiplied_num = self.num * randint(0,25)
#         return self.multiplied_num
