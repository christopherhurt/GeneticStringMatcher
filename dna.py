import random


class DNA:

    def __init__(self, sequence, target, chars):
        self.sequence = sequence
        self.target = target
        self.chars = chars
        self.fitness = 0

    def calc_fitness(self):
        for x in range(0, len(self.target)):
            if self.sequence[x] == self.target[x]:
                self.fitness += 1
        self.fitness = pow(5, self.fitness)

    def apply_mutation(self, mutation):
        for x in range(0, len(self.sequence)):
            if random.random() < mutation:
                self.sequence = self.sequence[:x] + random.choice(self.chars) + self.sequence[x+1:]  # FIX

    def pass_genes(self, parent_num):
        if parent_num == 1:
            return self.sequence[:int(len(self.sequence)/2)]
        else:
            return self.sequence[int(len(self.sequence)/2):]
