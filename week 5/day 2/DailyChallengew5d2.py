
import random
class Gene():
    def __init__(self):
        self.value = random.choice([True, False])
    def mutate(self):
        self.value = not self.value
    def __repr__(self):
        return "1" if self.value else "0"
    def __str__(self):
        return f"the value of this gene is: {self.__repr__()}"
class Chromosome():
    def __init__(self):
        self.value = [Gene() for i in range(3)]
    def mutate(self):
        for gene in self.value:
            if random.choice([True, False]):
                gene.mutate()
    def __repr__(self):
        return str(self.value)
class DNA():
    def __init__(self):
        self.value = [Chromosome() for i in range(3)]
    def mutate(self):
        for chromosome in self.value:
            if random.choice([True, False]):
                chromosome.mutate()
    def __repr__(self):
        return str(self.value)
class Organism():
    def __init__(self, dna, probability_to_mutate):
        self.dna = dna
        self.probability_to_mutate = probability_to_mutate
    def mutate(self):
        if random.random() <=self.probability_to_mutate:
            self.dna.mutate()
    def __repr__(self):
        return str(self.dna)
class Evolution():
    def __init__(self, num_of_organisims):
        self.population = [Organism(DNA(), 0.8) for i in range(num_of_organisims)]
        self.generations = 0
    def check_chromosome(self, chromosome):
        for gene in chromosome:
            if not gene.value:
                return False
        return True
    def check_dna(self, dna):
        for chromosome in dna.value:
            if not self.check_chromosome(chromosome.value):
                return False
        return True
    def check_population(self):
        for organism in self.population:
            if self.check_dna(organism.dna):
                return True
            return False
    def big_bang(self):
        while not self.check_population():
            print(self.generations)
            for organism in self.population:
                organism.mutate()
            self.generations += 1
        print(f"Completed in {self.generations} generations")