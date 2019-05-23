from population import *

MUTATION_RATE = 0.01
POPULATION_SIZE = 200

print('Welcome to the Genetic String Generator.')
target = input('Enter a string to be generated:\n')
print('---------------')

Population(target, MUTATION_RATE, POPULATION_SIZE)
