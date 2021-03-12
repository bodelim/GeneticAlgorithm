import numpy
import pandas as pd
import random
import ga

gene = 7
pop = 10
population = []

def init_pop(gene, pop):
    for j in range(pop):
        chromosome = []
        for i in range(gene): # chromosome에 gene난수를 7개 담아줌
            chromosome.append(numpy.random.randint(1,100))
        population.append(chromosome)
    return pd.DataFrame(population)

print(init_pop(gene, pop))
print(population[1][1])


num_generations = 5

num_parents_mating = 4
for generation in range(num_generations):
     # Measuring the fitness of each chromosome in the population.
     fitness = ga.cal_pop_fitness(equation_inputs, new_population)
    # Selecting the best parents in the population for mating.
     parents = ga.select_mating_pool(new_population, fitness, 
                                       num_parents_mating)
 
     # Generating next generation using crossover.
     offspring_crossover = ga.crossover(parents,
                                        offspring_size=(pop_size[0]-parents.shape[0], num_weights))
 
     # Adding some variations to the offsrping using mutation.
     offspring_mutation = ga.mutation(offspring_crossover)
# Creating the new population based on the parents and offspring.
     new_population[0:parents.shape[0], :] = parents
     new_population[parents.shape[0]:, :] = offspring_mutation