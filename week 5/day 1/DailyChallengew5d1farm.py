from farm import farm

macdonald = Farm("Mcdonald's")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
macdonald.display_info()

print(macdonald.get_animal_types())