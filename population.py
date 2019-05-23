import string
import math
from dna import *


class Population:

    def __init__(self, target, mutation, size):
        Population.chars = string.printable
        Population.target = target
        Population.pop = []
        Population.mut_pool = []
        self.mutation = mutation
        self.size = size
        self.generations = 0
        self.initialize_pop()
        self.run_alg()

    def initialize_pop(self):
        for _ in range(0, self.size):
            sequence = ''
            for _ in range(0, len(Population.target)):
                sequence += random.choice(Population.chars)
            Population.pop.append(DNA(sequence, Population.target, Population.chars))
            print(sequence)
        self.generations += 1
        print('---------------')

    def run_alg(self):
        while not Population.check_solution():
            Population.check_fit()
            self.create_mutation_pool()
            self.reproduce()
            self.generations += 1
            print('---------------')
        print(Population.target)
        print('Target string successfully generated in ' + str(self.generations) + ' generations!')

    @staticmethod
    def check_fit():
        for dna in Population.pop:
            dna.calc_fitness()

    def reproduce(self):
        Population.pop = []
        for _ in range(0, self.size):
            parent_1 = random.choice(Population.mut_pool)
            parent_2 = random.choice(Population.mut_pool)
            new_sequence = parent_1.pass_genes(1) + parent_2.pass_genes(2)
            new_dna = DNA(new_sequence, Population.target, Population.chars)
            new_dna.apply_mutation(self.mutation)
            Population.pop.append(new_dna)
            print(new_dna.sequence)

    @staticmethod
    def create_mutation_pool():
        Population.mut_pool = []
        max_fitness = 0
        for dna in Population.pop:
            if dna.fitness > max_fitness:
                max_fitness = dna.fitness
        for dna in Population.pop:
            pool_count = math.floor(dna.fitness / max_fitness * 100)
            for _ in range(0, pool_count):
                Population.mut_pool.append(dna)

    @staticmethod
    def check_solution():
        for x in range(0, len(Population.pop)):
            if Population.pop[x].sequence == Population.target:
                return True
        return False
